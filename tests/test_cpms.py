
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class TestCPMSModules(unittest.TestCase):

    def test_student_registration_module(self):
        file = ROOT / "student" / "registration.txt"
        self.assertTrue(file.is_file(), "Student module is missing")
        self.assertGreater(file.stat().st_size, 0, "Student module is empty")

    def test_company_management_module(self):
        file = ROOT / "company" / "company.txt"
        self.assertTrue(file.is_file(), "Company module is missing")
        self.assertGreater(file.stat().st_size, 0, "Company module is empty")

    def test_placement_drive_module(self):
        file = ROOT / "placement" / "drive.txt"
        self.assertTrue(file.is_file(), "Placement module is missing")
        self.assertGreater(file.stat().st_size, 0, "Placement module is empty")

if __name__ == "__main__":
    unittest.main()
