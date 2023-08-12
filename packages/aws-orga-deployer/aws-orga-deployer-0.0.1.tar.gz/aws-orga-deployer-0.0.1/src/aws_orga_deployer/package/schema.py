"""Define the schema of the package definition file."""
from typing import Dict

import jsonschema

from aws_orga_deployer import config
from aws_orga_deployer.engines import ENGINES


def validate(content: Dict) -> None:
    """Validate the content provided with the schema.

    Args:
        content: Dict to validate.

    Raise:
        ValidationError: If the schema is invalid.
    """
    schema = {
        "type": "object",
        "properties": {
            "packageConfiguration": {
                "description": "Package configuration settings",
                "type": "object",
                "properties": {
                    "s3Bucket": {
                        "description": "Name of the S3 bucket to store persistent data",
                        "type": "string",
                        "minLength": 3,
                    },
                    "s3Region": {
                        "description": "Region of the S3 bucket",
                        "type": "string",
                        "minLength": 3,
                    },
                    "s3Prefix": {
                        "description": "S3 prefix. Must ends with a slash if specified",
                        "type": "string",
                        "pattern": "^.+\\/$",
                    },
                    "concurrentThreads": {
                        "description": "Number of concurrent threads deploying modules",
                        "type": "number",
                        "minimum": 1,
                        "maximum": 50,
                    },
                    "assumeOrgaRoleArn": {
                        "description": (
                            "ARN of the IAM role to assume to query AWS Organizations"
                        ),
                        "type": "string",
                    },
                    "orgaCacheExpiration": {
                        "description": (
                            "Period in seconds during which the cache in S3 of"
                            " information on accounts and organizational units is"
                            " reused instead of querying AWS Organizations"
                        ),
                        "type": "number",
                        "minimum": 0,
                    },
                    "overrideAccountNameByTag": {
                        "description": (
                            "Tag key assigned to AWS accounts whose value is used to"
                            " override the account name"
                        ),
                        "type": "string",
                    },
                },
                "required": ["s3Bucket", "s3Region"],
            },
            "defaultModuleConfiguration": {
                "description": (
                    "Default configuration settings for all modules or modules of a"
                    " given engine"
                ),
                "type": "object",
                "propertyNames": {"enum": ["all", *ENGINES]},
                "patternProperties": {"^": {"type": "object"}},
                "additionalProperties": False,
            },
            "defaultVariables": {
                "description": (
                    "Default variables for all modules or modules of a given engine"
                ),
                "type": "object",
                "propertyNames": {"enum": ["all", *ENGINES]},
                "patternProperties": {"^": {"type": "object"}},
                "additionalProperties": False,
            },
            "modules": {
                "description": "Module deployments definition",
                "type": "object",
                "propertyNames": {"enum": [*config.MODULES]},
                "patternProperties": {
                    "^": {
                        "type": "object",
                        "properties": {
                            "configuration": {
                                "description": "Module configuration settings",
                                "type": "object",
                            },
                            "variables": {
                                "description": "Module variables",
                                "type": "object",
                            },
                            "variablesFromOutputs": {
                                "type": "object",
                                "patternProperties": {
                                    "^": {
                                        "type": "object",
                                        "properties": {
                                            "module": {
                                                "type": "string",
                                                "enum": [*config.MODULES],
                                            },
                                            "region": {"type": "string"},
                                            "accountId": {"type": "string"},
                                            "outputName": {"type": "string"},
                                        },
                                        "required": [
                                            "module",
                                            "region",
                                            "accountId",
                                            "outputName",
                                        ],
                                    }
                                },
                            },
                            "deployments": {
                                "description": "List of module deployments",
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "include": {
                                            "type": "object",
                                            "properties": {
                                                "accountIds": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^[0-9]{12}$",
                                                    },
                                                },
                                                "accountNames": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                                "accountTags": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^.+=.+$",
                                                    },
                                                },
                                                "ouIds": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                                "ouTags": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^.+=.+$",
                                                    },
                                                },
                                                "regions": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                            },
                                        },
                                        "exclude": {
                                            "type": "object",
                                            "properties": {
                                                "accountIds": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^[0-9]{12}$",
                                                    },
                                                },
                                                "accountNames": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                                "accountTags": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^.+=.+$",
                                                    },
                                                },
                                                "ouIds": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                                "ouTags": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "pattern": "^.+=.+$",
                                                    },
                                                },
                                                "regions": {
                                                    "type": "array",
                                                    "items": {"type": "string"},
                                                },
                                            },
                                        },
                                        "variables": {"type": "object"},
                                        "variablesFromOutputs": {
                                            "type": "object",
                                            "patternProperties": {
                                                "^": {
                                                    "type": "object",
                                                    "properties": {
                                                        "module": {
                                                            "type": "string",
                                                            "enum": [*config.MODULES],
                                                        },
                                                        "region": {"type": "string"},
                                                        "accountId": {"type": "string"},
                                                        "outputName": {
                                                            "type": "string"
                                                        },
                                                    },
                                                    "required": [
                                                        "module",
                                                        "region",
                                                        "accountId",
                                                        "outputName",
                                                    ],
                                                }
                                            },
                                        },
                                        "dependencies": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "module": {
                                                        "type": "string",
                                                        "enum": [*config.MODULES],
                                                    },
                                                    "region": {"type": "string"},
                                                    "accountId": {"type": "string"},
                                                },
                                                "required": [
                                                    "module",
                                                    "region",
                                                    "accountId",
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "required": ["deployments"],
                    }
                },
                "additionalProperties": False,
            },
        },
        "required": ["packageConfiguration", "modules"],
    }
    jsonschema.validate(instance=content, schema=schema)
