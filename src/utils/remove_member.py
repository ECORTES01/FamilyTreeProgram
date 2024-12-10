from models.family_tree import FamilyTree

def remove_member(tree, name):
    """
    Removes a person and their descendants from the family tree.

    :param tree: The FamilyTree instance.
    :param name: The name of the person to be removed.
    :return: Success message or error message.
    """
    # Attempt to remove the person
    if tree.remove_person(name):
        return f"{name} and their descendants have been successfully removed from the tree."
    else:
        return f"Failed to remove {name}. Ensure the name exists in the family tree."

# Example Usage
if __name__ == "__main__":
    # Create a FamilyTree instance
    family_tree = FamilyTree()

    # Add a root member and a child for demonstration
    family_tree.add_person(None, Person("John Doe", "1950-01-01", "Root", ["Patriarch"]))
    family_tree.add_person("John Doe", Person("Jane Doe", "1980-05-15", "Daughter", ["Gardener"]))

    # Remove a member
    result = remove_member(family_tree, "John Doe")
    print(result)  # Output: John Doe and their descendants have been successfully removed from the tree.
