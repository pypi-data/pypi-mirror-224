"""Wrapper of CloudFormation modules that is executed in a subprocess."""
import random
import string
import time
from os import path
from typing import Any, Dict, List

import boto3
import botocore

from aws_orga_deployer.engines.wrappers import base

# CloudFormation capabilities passed to API requests
CFN_CAPABILITIES: List[str] = [
    "CAPABILITY_IAM",
    "CAPABILITY_NAMED_IAM",
    "CAPABILITY_AUTO_EXPAND",
]


def main() -> None:
    """Main function."""

    def check_stack_exists() -> bool:
        """Return True to the stack exists."""
        try:
            _stack = client.describe_stacks(StackName=stack_name)["Stacks"][0]
            _status = _stack["StackStatus"]
            # The stack has the status REVIEW_IN_PROGRESS when change sets
            # were created but the stack has not yet been created
            if _status == "REVIEW_IN_PROGRESS":
                return False
            return True
        except botocore.exceptions.ClientError as err:
            if "does not exist" in str(err):
                return False
            raise err

    def get_additional_boto3_params() -> Dict[str, Any]:
        """Retrieve and returns the list of additional parameters that must be
        passed to boto3 API requests.
        """
        if "additionalBoto3Parameters" in inputs.module_config:
            return inputs.module_config["additionalBoto3Parameters"]
        return {}

    def get_template_body() -> str:
        """Load the template whose filename is given in `templateFilename` and
        returns its content.
        """
        filename = inputs.module_config.get("templateFilename")
        if not isinstance(filename, str):
            raise ValueError('Module configuration must specify "templateFilename"')
        try:
            filepath = path.join(inputs.module_dir, filename)
            with open(filepath, "r", encoding="utf-8") as stream:
                return stream.read()
        except OSError as err:
            raise ValueError(f"Cannot read the template at {filepath}") from err

    def get_stack_status() -> str:
        """Returns the stack status."""
        _stack = client.describe_stacks(StackName=stack_name)["Stacks"][0]
        return _stack["StackStatus"]

    def get_stack_outputs() -> Dict[str, str]:
        """Returns the stack outputs."""
        time.sleep(2)
        _stack = client.describe_stacks(StackName=stack_name)["Stacks"][0]
        if not "Outputs" in _stack:
            return {}
        return {
            output["OutputKey"]: output["OutputValue"] for output in _stack["Outputs"]
        }

    def get_stack_resources() -> List[str]:
        """Returns the list of stack resources."""
        result = []
        paginator = client.get_paginator("list_stack_resources")
        pages = paginator.paginate(StackName=stack_name)
        for page in pages:
            for resource in page["StackResourceSummaries"]:
                result.append(resource["LogicalResourceId"])
        return result

    def prepare_stack_parameters() -> List[Dict[str, Any]]:
        """Generate and return a list of stack parameters from the input
        variables.
        """
        return [
            {
                "ParameterKey": name,
                "ParameterValue": ",".join(value) if isinstance(value, list) else value,
                "UsePreviousValue": False,
            }
            for name, value in inputs.variables.items()
        ]

    def delete_change_set() -> None:
        """Try to delete the change set, but ignore any exceptions raised by
        boto3.
        """
        try:
            client.delete_change_set(ChangeSetName=change_set_id)
        except botocore.exceptions.ClientError:
            pass

    # Read the inputs from the JSON file `input.json` and create a boto3 client
    # for the module region
    inputs = base.read_wrapper_inputs()
    # Create a boto3 client for CloudFormation with custom endpoint if needed
    endpoint_config = {}
    if "endpointUrls" in inputs.module_config:
        if "cloudformation" in inputs.module_config["endpointUrls"]:
            endpoint_url = inputs.module_config["endpointUrls"]["cloudformation"]
            endpoint_config = {"endpoint_url": endpoint_url}
    client = boto3.client(
        "cloudformation", region_name=inputs.region, **endpoint_config
    )
    # Retrieve the stack name
    stack_name = inputs.module_config.get("stackName")
    if not isinstance(stack_name, str):
        raise ValueError('Module configuration must specify "stackName"')
    # Check if the stack already exists
    stack_exists = check_stack_exists()
    #######################################
    # If the action is "create" or "update"
    if inputs.action in ("create", "update"):
        # Create a change set to identify the list of resources to add,
        # change or delete. The name of the change set is the name of the
        # stack, prepended by 5 random letters
        random_suffix = "".join(random.choices(string.ascii_lowercase, k=5))
        change_set_name = stack_name + "-" + random_suffix
        change_set_id = client.create_change_set(
            StackName=stack_name,
            TemplateBody=get_template_body(),
            UsePreviousTemplate=False,
            Parameters=prepare_stack_parameters(),
            Capabilities=CFN_CAPABILITIES,
            ChangeSetName=change_set_name,
            Description="Change set for AWS Orga Deployer",
            ChangeSetType="UPDATE" if stack_exists else "CREATE",
            IncludeNestedStacks=False,
            OnStackFailure="ROLLBACK" if stack_exists else "DELETE",
            **get_additional_boto3_params(),
        )["Id"]
        # Wait until the change set completes
        while True:
            time.sleep(3)
            change_set = client.describe_change_set(ChangeSetName=change_set_id)
            status = change_set["Status"]
            # Stop waiting if the change set has completed
            if status.endswith("COMPLETE"):
                break
            # Wait if the status is still pending or in progress
            if status.endswith("IN_PROGRESS") or status.endswith("PENDING"):
                continue
            # For any other status
            delete_change_set()
            # Retrieve the existing outputs if the stack already exists,
            # because outputs must be provided if command is "apply"
            if stack_exists:
                existing_outputs = get_stack_outputs()
            else:
                existing_outputs = None
            # If the change set fails because there are no changes to be
            # made, no need to continue
            if "information didn't contain changes" in change_set["StatusReason"]:
                base.write_wrapper_outputs(
                    made_changes=False,
                    result="No changes to be made",
                    detailed_results=None,
                    outputs=existing_outputs if inputs.command == "apply" else None,
                )
                return
            # Raise an error if the change set failed for another reason
            raise RuntimeError("Failed to evaluate the changes to be made")
        # Identify the resources to add, change or delete
        res_add = []
        res_change = []
        res_delete = []
        for change in change_set["Changes"]:
            if change["Type"] == "Resource":
                rsc_change = change["ResourceChange"]
                if rsc_change["Action"] == "Add":
                    res_add.append(rsc_change["LogicalResourceId"])
                elif rsc_change["Action"] == "Modify":
                    res_change.append(rsc_change["LogicalResourceId"])
                elif rsc_change["Action"] == "Remove":
                    res_delete.append(rsc_change["LogicalResourceId"])
        # If the command is preview, the outcomes must be named "to add",
        # "to change", "to delete" and there are no outputs to return
        if inputs.command == "preview":
            # Write the outputs
            base.write_wrapper_outputs(
                made_changes=True,
                result=(
                    f"{len(res_add)} resources to add, "
                    f"{len(res_change)} to change, "
                    f"{len(res_delete)} to delete"
                ),
                detailed_results={
                    "ResourcesToAdd": res_add,
                    "ResourcesToChange": res_change,
                    "ResourcesToDelete": res_delete,
                },
            )
        # If the command is preview, the outcomes must be named "added",
        # "changed", "deleted" and outputs must be returned
        elif inputs.command == "apply":
            # Execute the change set
            client.execute_change_set(ChangeSetName=change_set_id)
            # Wait until the stack updates completes
            while True:
                time.sleep(3)
                status = get_stack_status()
                if status.endswith("COMPLETE") and not "ROLLBACK" in status:
                    break
                # Wait if the status is still pending or in progress
                if status.endswith("IN_PROGRESS"):
                    continue
                # If the status is unknown, raise an error
                delete_change_set()
                raise RuntimeError("Failed to apply the changes to be made")
            # Write the outputs assuming that the changes made are those
            # identified in the change set
            base.write_wrapper_outputs(
                made_changes=True,
                result=(
                    f"{len(res_add)} resources added, "
                    f"{len(res_change)} changed, "
                    f"{len(res_delete)} deleted"
                ),
                detailed_results={
                    "ResourcesAdded": res_add,
                    "ResourcesChanged": res_change,
                    "ResourcesDeleted": res_delete,
                },
                outputs=get_stack_outputs(),
            )
        # Delete the change set and exit
        delete_change_set()
    #######################################
    # If the action is "destroy"
    elif inputs.action == "destroy":
        # Retrieve the list of existing resources if the stack exists
        if stack_exists:
            res_delete = get_stack_resources()
        else:
            res_delete = []
        # If the command is "preview", return the list of existing resources
        # as the list of resources to delete
        if inputs.command == "preview":
            base.write_wrapper_outputs(
                made_changes=len(res_delete) > 0,
                result=f"{len(res_delete)} resources to delete",
                detailed_results={"ResourcesToDelete": res_delete},
            )
        # If the command is "apply", delete the stack and return the list of
        # existing resources as the list of deleted resources
        elif inputs.command == "apply":
            # Delete the stack
            client.delete_stack(StackName=stack_name)
            # Wait for the stack deletion to complete
            while True:
                time.sleep(3)
                exists = check_stack_exists()
                if not exists:
                    break
                status = get_stack_status()
                if status.endswith("COMPLETE"):
                    break
                # Wait if the status is still pending or in progress
                if status.endswith("IN_PROGRESS"):
                    continue
                # If the status is unknown, raise an error
                raise RuntimeError("Failed to delete the stack")
            # Return the list of resources that existed before the stack
            # was deleted
            base.write_wrapper_outputs(
                made_changes=len(res_delete) > 0,
                result=f"{len(res_delete)} resources deleted",
                detailed_results={"ResourcesDeleted": res_delete},
            )


if __name__ == "__main__":
    main()
