import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('SSSD', 'exp', 100, 100)

    def test_init(self):
        self.assertEqual(self.hardware.name, 'SSSD')
        self.assertEqual(self.hardware.type, 'exp')
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_raises_exception(self):
        software = Software('test', 'light', 120, 50)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_install(self):
        software = Software('test', 'light', 80, 50)
        self.hardware.install(software)
        self.assertEqual(self.hardware.software_components, [software])

    def test_uninstall(self):
        software = Software('test', 'light', 80, 50)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.software_components, [])