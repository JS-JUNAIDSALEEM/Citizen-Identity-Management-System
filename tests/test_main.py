
import unittest
import main
import os
import tempfile

class TestCitizenSystem(unittest.TestCase):

    def setUp(self):
        self.old_location = os.getcwd()
        self.temp_folder = tempfile.TemporaryDirectory()
        os.chdir(self.temp_folder.name)

        self.test_citizens = {
            "35201-1234567-1": {
                "name": "Ali Khan",
                "father_name": "Ahmed Khan",
                "dob": "15-08-1995",
                "address": "Lahore",
                "status": "Active",
                "pin": "1234"
            }
        }

    def tearDown(self):
        os.chdir(self.old_location)
        self.temp_folder.cleanup()

# Test valid CNIC
    def test_valid_cnic(self):
        self.assertTrue(main.check_cnic("35201-1234567-1"))

# Test invalid CNIC
    def test_invalid_cnic(self):
        self.assertFalse(main.check_cnic("3520112345671"))

# Test valid citizen data
    def test_valid_citizens(self):
        self.assertTrue(main.validate_citizens(self.test_citizens))

# Test missing citizen fields
    def test_invalid_citizens(self):
        data = {
            "35201-1234567-1": {
                "name": "Ali Khan"
            }
        }

        self.assertFalse(main.validate_citizens(data))

# Test invalid PIN
    def test_invalid_pin(self):
        self.test_citizens["35201-1234567-1"]["pin"] = "12"

        self.assertFalse(main.validate_citizens(self.test_citizens))

# Test saving and loading JSON data
    def test_save_and_load_citizens(self):
        main.save_citizens(self.test_citizens)

        saved_citizens = main.load_citizens()

        self.assertEqual(saved_citizens, self.test_citizens)

# Test invalid JSON file
    def test_invalid_json(self):
        with open("citizens.json", "w") as file:
            file.write("{ invalid json")

        self.assertEqual(main.load_citizens(), main.citizens)


# Main block to run the tests

if __name__ == "__main__":
    unittest.main()