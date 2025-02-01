import unittest
from licensing_manager import LicensingManager

class TestLicensingManager(unittest.TestCase):

    def setUp(self):
        """Set up the LicensingManager for testing."""
        self.licensing_manager = LicensingManager()
        self.license_key_valid = "VALID-KEY-1234"
        self.license_key_invalid = "INVALID-KEY-5678"
    
    def test_grant_license(self):
        """Test the granting of a valid license."""
        success = self.licensing_manager.grant_license(self.license_key_valid)
        self.assertTrue(success)
        self.assertTrue(self.licensing_manager.is_license_valid(self.license_key_valid))

    def test_invalid_license(self):
        """Test for invalid license key validation."""
        success = self.licensing_manager.grant_license(self.license_key_invalid)
        self.assertFalse(success)
        self.assertFalse(self.licensing_manager.is_license_valid(self.license_key_invalid))
    
    def test_revoke_license(self):
        """Test revoking an existing license."""
        self.licensing_manager.grant_license(self.license_key_valid)
        revoked = self.licensing_manager.revoke_license(self.license_key_valid)
        self.assertTrue(revoked)
        self.assertFalse(self.licensing_manager.is_license_valid(self.license_key_valid))

    def test_check_expired_license(self):
        """Test that an expired license is properly identified as invalid."""
        # Assuming an expiration logic is implemented in LicensingManager
        self.licensing_manager.grant_license(self.license_key_valid, expiration=True)
        expired = self.licensing_manager.is_license_expired(self.license_key_valid)
        self.assertTrue(expired)

if __name__ == '__main__':
    unittest.main()
