from models.person import Person
from models.family_tree import FamilyTree
from models.relationship_graph import RelationshipGraph
from gui import FamilyTreeApp

if __name__ == "__main__":
    # FamilyTree Example
    family_tree = FamilyTree()
    root_person = Person("John Doe", "1950-01-01", "Root", "Patriarch of the family")
    family_tree.add_person(None, root_person)

    child = Person("Jane Doe", "1980-05-15", "Daughter", "Loves gardening")
    family_tree.add_person("John Doe", child)

    print("Search Jane Doe:", family_tree.search_person("Jane Doe"))
    print("Sorted Members by Name:", family_tree.sort_members(key="name"))

    # RelationshipGraph Example
    graph = RelationshipGraph()
    graph.add_relationship("John Doe", "Jane Doe", "Parent-Child")
    print("Relationship:", graph.search_relationship("John Doe", "Jane Doe"))

    # Launch GUI
    app = FamilyTreeApp()
    app.run()
