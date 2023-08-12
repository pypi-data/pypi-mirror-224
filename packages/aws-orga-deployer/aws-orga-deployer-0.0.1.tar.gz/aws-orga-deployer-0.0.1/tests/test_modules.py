"""Test the module `aws_orga_deployer.modules`."""
# COMPLETED
import unittest

from aws_orga_deployer import config, modules
from tests import mock


class TestModules(unittest.TestCase):
    """Test the modules."""

    def setUp(self):
        """Load the modules."""
        mock.mock_cli_arguments(package_filename="package1.yaml")
        modules.load_modules()

    def test_modules(self):
        """Check that the modules are loaded."""
        self.assertIn("python1", config.MODULES)
        self.assertEqual(config.MODULES["python1"].engine, "python")

    def test_module_hash(self):
        """Check that the module "python1" has a module hash."""
        module_hash = config.MODULES["python1"].module_hash
        self.assertRegex(module_hash, "^[a-f0-9]{32}$")

    def test_patterns(self):
        """Check that the hash configuration file is correctly used."""
        self.assertEqual(
            config.MODULES["python1"].included_patterns,
            ["*.py"],
        )
        self.assertEqual(
            config.MODULES["python1"].excluded_patterns,
            ["~*.py"],
        )
