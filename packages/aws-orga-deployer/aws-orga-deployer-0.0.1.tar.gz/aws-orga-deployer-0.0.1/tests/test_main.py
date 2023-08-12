"""Test the CLI with mocked boto3."""
from moto import mock_organizations, mock_sts

from aws_orga_deployer import main
from tests import mock
from tests.mock import mock_others


@mock_organizations
@mock_sts
@mock_others
def main_test():
    """Create fake resources and run the main CLI function."""
    mock.create_fake_resources()
    main.main()


if __name__ == "__main__":
    main_test()
