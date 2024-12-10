import unittest
from models.family_tree import FamilyTree
from models.person import Person

class TestFamilyTree(unittest.TestCase):

    def setUp(self):
        """Set up a sample family tree for testing."""
        self.family_tree = FamilyTree()

        # Add root member
        self.root_person = Person("John Doe", "1950-01-01", "Root", ["Patriarch"])
        self.family_tree.add_person(None, self.root_person)

        # Add child members
        self.child1 = Person("Jane Doe", "1980-05-15", "Daughter", ["Gardener"])
        self.family_tree.add_person("John Doe", self.child1)

        self.child2 = Person("Jake Doe", "1975-03-20", "Son", ["Engineer"])
        self.family_tree.add_person("John Doe", self.child2)

    def test_add_person(self):
        """Test adding a person to the family tree."""
        new_person = Person("Emily Doe", "2005-07-10", "Granddaughter", ["Student"])
        result = self.family_tree.add_person("Jane Doe", new_person)
        self.assertTrue(result)
        self.assertIn("Emily Doe", self.family_tree.members)

    def test_remove_person(self):
        """Test removing a person and their descendants."""
        result = self.family_tree.remove_person("Jane Doe")
        self.assertTrue(result)
        self.assertNotIn("Jane Doe", self.family_tree.members)
        self.assertNotIn("Emily Doe", self.family_tree.members)  # Assuming Emily was a child of Jane

    def test_search_person(self):
        """Test searching for an existing person."""
        result = self.family_tree.search_person("Jane Doe")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Jane Doe")

        # Test searching for a non-existent person
        result = self.family_tree.search_person("Nonexistent Person")
        self.assertIsNone(result)

    def test_sort_members(self):
        """Test sorting members by name."""
        sorted_members = self.family_tree.sort_members(key="name")
        sorted_names = [member.name for member in sorted_members]
        self.assertEqual(sorted_names, ["Jake Doe", "Jane Doe", "John Doe"])

        # Test sorting by birth_date
        sorted_members = self.family_tree.sort_members(key="birth_date")
        sorted_names = [member.name for member in sorted_members]
        self.assertEqual(sorted_names, ["John Doe", "Jake Doe", "Jane Doe"])

    def test_invalid_sort_key(self):
        """Test sorting with an invalid key."""
        with self.assertRaises(ValueError):
            self.family_tree.sort_members(key="invalid_key")

if __name__ == "__main__":
    unittest.main()
