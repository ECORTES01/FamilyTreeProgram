from models.family_tree import FamilyTree

def search_member(tree, name):
    """
    Searches for a member in the family tree by their name.

    :param tree: The FamilyTree instance.
    :param name: The name of the person to search for.
    :return: A string containing the person's details if found, or an error message if not found.
    """
    person = tree.search_person(name)
    if person:
        return f"Found: {person.name} ({person.birth_date}) - {person.relationship}. Facts: {', '.join(person.facts)}"
    else:
        return f"Error: {name} not found in the family tree."

# Example Usage
if __name__ == "__main__":
    from models.person import Person

    # Create a FamilyTree instance
    family_tree = FamilyTree()

    # Add a person for demonstration
    family_tree.add_person(None, Person("John Doe", "1950-01-01", "Root", ["Patriarch"]))
    family_tree.add_person("John Doe", Person("Jane Doe", "1980-05-15", "Daughter", ["Gardener"]))

    # Search for a member
    result = search_member(family_tree, "Jane Doe")
    print(result)  # Output: Found: Jane Doe (1980-05-15) - Daughter. Facts: Gardener
