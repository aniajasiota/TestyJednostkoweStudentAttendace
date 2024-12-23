import unittest

# rozbić na kilka osobnych testów

class TestAttendanceManager(unittest.TestCase):
    def setUp(self):
        from main import AttendanceManager
        self.manager = AttendanceManager()

    def test_add_attendance(self):
        self.manager.add(date="2024-11-25", user_id=1, was=True)
        self.assertIn(1, self.manager.all_attendance)
        self.assertTrue(self.manager.all_attendance[1]["2024-11-25"])

    def test_edit_attendance(self):
        self.manager.add(date="2024-11-25", user_id=1, was=False)
        self.manager.edit(date="2024-11-25", user_id=1, was=True)
        self.assertTrue(self.manager.all_attendance[1]["2024-11-25"])

    def test_delete_attendance(self):
        self.manager.add(date="2024-11-25", user_id=1, was=True)
        self.manager.delete(date="2024-11-25", user_id=1)
        self.assertNotIn("2024-11-25", self.manager.all_attendance.get(1, {}))

    def test_generate_report(self):
        self.manager.add(date="2024-11-25", user_id=1, was=True)
        report = self.manager.generate_report()
        self.assertIn("Attendance Report:", report)
        self.assertIn("2024-11-25: True", report)


if __name__ == '__main__':
    unittest.main()