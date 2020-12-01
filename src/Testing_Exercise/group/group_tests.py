from .group_project import Person, Group
import unittest


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Alis', 'Wilson')

    def test_init(self):
        self.assertEqual(self.person.name, 'Alis')
        self.assertEqual(self.person.surname, 'Wilson')

    def test_add(self):
        self.other_person = Person('Evlampia', 'Sotirelis')
        self.new_person = self.person + self.other_person
        self.assertEqual(self.new_person.name, 'Alis')
        self.assertEqual(self.new_person.surname, 'Sotirelis')

    def test_repr(self):
        self.assertEqual(str(self.person), 'Alis Wilson')


class GroupTests(unittest.TestCase):
    def setUp(self):
        self.person1 = Person('Alis', 'Wilson')
        self.person2 = Person('Charly', 'Pit')
        self.person3 = Person('Vivian', 'Petkoff')
        self.group = Group('Dancers', [self.person1, self.person2, self.person3])
        self.person4 = Person('Aliko', 'Dangote')
        self.person5 = Person('Bill', 'Gates')
        self.group2 = Group('Singers', [self.person4, self.person5])
        self.new_group = self.group + self.group2

    def test_init(self):
        self.assertEqual(self.group.name, 'Dancers')
        self.assertEqual(self.group.people, ['Alis Wilson', 'Charly Pit', 'Vivian Petkoff'])

    def test_custom_add(self):
        self.assertEqual(self.new_group.people, ['Alis Wilson', 'Charly Pit', 'Vivian Petkoff', 'Aliko Dangote', 'Bill Gates'])

    def test_custom_len(self):
        self.assertEqual(len(self.group), 3)
        self.assertEqual(len(self.new_group), 5)

    def test_custom_repr(self):
        self.assertEqual(str(self.group), "Group Dancers with members Alis Wilson, Charly Pit, Vivian Petkoff")

    def test_custom_getitem(self):
        self.assertEqual(self.group[1], "Person 1: Charly Pit")
        self.assertIn('Alis', self.group[0])

    def test_get_item_index_error(self):
        with self.assertRaises(IndexError):
            result = self.group[4]

    def test_repr(self):
        self.assertIn("Dancers", repr(self.group))
        self.assertIn("Alis", repr(self.group))
        self.assertIn("Pit", repr(self.group))
        self.assertNotIn("Rayan", repr(self.group))


if __name__ == '__main__':
    unittest.main()