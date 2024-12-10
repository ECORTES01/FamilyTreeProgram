import unittest
from models.relationship_graph import RelationshipGraph

class TestRelationshipGraph(unittest.TestCase):

    def setUp(self):
        """Set up a sample relationship graph for testing."""
        self.graph = RelationshipGraph()

        # Add initial relationships
        self.graph.add_relationship("John Doe", "Jane Doe", "Parent-Child")
        self.graph.add_relationship("John Doe", "Emily Doe", "Spouse")
        self.graph.add_relationship("Jane Doe", "Jake Smith", "Colleague")

    def test_add_relationship(self):
        """Test adding a relationship between two people."""
        self.graph.add_relationship("Jane Doe", "Emily Doe", "Friend")
        self.assertIn(("Emily Doe", "Friend"), self.graph.graph["Jane Doe"])
        self.assertIn(("Jane Doe", "Friend"), self.graph.graph["Emily Doe"])

    def test_remove_relationship(self):
        """Test removing a relationship between two people."""
        self.graph.remove_relationship("John Doe", "Jane Doe")
        self.assertNotIn(("Jane Doe", "Parent-Child"), self.graph.graph["John Doe"])
        self.assertNotIn(("John Doe", "Parent-Child"), self.graph.graph["Jane Doe"])

    def test_search_relationship(self):
        """Test searching for a relationship between two people."""
        relationship = self.graph.search_relationship("John Doe", "Jane Doe")
        self.assertEqual(relationship, "Parent-Child")

        # Test searching for a non-existent relationship
        relationship = self.graph.search_relationship("John Doe", "Jake Smith")
        self.assertIsNone(relationship)

    def test_sort_relationships(self):
        """Test sorting relationships of a person by relationship type."""
        sorted_relationships = self.graph.sort_relationships("John Doe")
        sorted_types = [rel[1] for rel in sorted_relationships]
        self.assertEqual(sorted_types, ["Parent-Child", "Spouse"])  # Assuming alphabetical order

    def test_invalid_person_sort(self):
        """Test sorting relationships for a non-existent person."""
        sorted_relationships = self.graph.sort_relationships("Nonexistent Person")
        self.assertEqual(sorted_relationships, [])

if __name__ == "__main__":
    unittest.main()
