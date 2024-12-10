from models.person import Person
from models.family_tree import FamilyTree

def add_member(tree, parent_name, name, birth_date, relationship, facts=None):
    """
    Adds a new member to the family tree under the specified parent.

    :param tree: The FamilyTree instance.
    :param parent_name: The name of the parent to whom the new member will be added.
    :param name: The name of the new person.
    :param birth_date: The birth date of the new person (YYYY-MM-DD).
    :param relationship: The relationship of the new person to the parent.
    :param facts: Optional list of facts about the person.
    :return: Success message or error message.
    """
    # Create a new Person object
    new_person = Person(name=name, birth_date=birth_date, relationship=relationship, facts=facts)

    # Attempt to add the person to the FamilyTree
    if tree.add_person(parent_name, new_person):
        return f"{name} has been successfully added under {parent_name}."
    else:
        return f"Failed to add {name}. Ensure the parent {parent_name} exists or specify None for the root."

# Example Usage
if __name__ == "__main__":
    # Create a FamilyTree instance
    family_tree = FamilyTree()

    # Add the root person
    print(add_member(family_tree, None, "John Doe", "1950-01-01", "Root", ["Patriarch of the family"]))

    # Add a child to the root person
    print(add_member(family_tree, "John Doe", "Jane Doe", "1980-05-15", "Daughter", ["Loves gardening"]))
