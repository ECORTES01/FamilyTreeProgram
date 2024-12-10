from models.family_tree import FamilyTree

def sort_members(tree, key="name"):
    """
    Sorts the members of the family tree by a specified attribute.

    :param tree: The FamilyTree instance.
    :param key: The attribute to sort by ("name", "birth_date", "relationship").
    :return: A list of sorted member details, or an error message if the key is invalid.
    """
    valid_keys = ["name", "birth_date", "relationship"]
    if key not in valid_keys:
        return f"Error: Invalid key for sorting. Please use one of {valid_keys}."

    # Perform the sort
    sorted_members = tree.sort_members(key=key)
    return [f"{member.name} ({member.birth_date}) - {member.relationship}" for member in sorted_members]

# Example Usage
if __name__ == "__main__":
    from models.person import Person

    # Create a FamilyTree instance
    family_tree = FamilyTree()

    # Add members for demonstration
    family_tree.add_person(None, Person("John Doe", "1950-01-01", "Root", ["Patriarch"]))
    family_tree.add_person("John Doe", Person("Jane Doe", "1980-05-15", "Daughter", ["Gardener"]))
    family_tree.add_person("John Doe", Person("Jake Doe", "1975-03-20", "Son", ["Engineer"]))

    # Sort members by name
    result = sort_members(family_tree, key="name")
    print("Sorted by name:", result)

    # Sort members by birth date
    result = sort_members(family_tree, key="birth_date")
    print("Sorted by birth date:", result)
