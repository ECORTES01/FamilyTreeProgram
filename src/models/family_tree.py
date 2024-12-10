class FamilyTree:
    def __init__(self):
        """Initializes an empty family tree."""
        self.members = {}  # Dictionary to store members by name
        self.root = None  # The root member of the tree

    def add_person(self, parent_name, person):
        """
        Adds a new person to the family tree under the specified parent.

        :param parent_name: The name of the parent. None if the person is the root.
        :param person: The Person object to add.
        :return: True if the person was added successfully, False otherwise.
        """
        if parent_name is None:
            # Adding the root member
            if not self.root:
                self.root = person
                self.members[person.name] = person
                return True
            else:
                print("Root already exists. Provide a parent.")
                return False

        # Adding a non-root member
        if parent_name in self.members:
            parent = self.members[parent_name]
            if not hasattr(parent, "children"):
                parent.children = []  # Initialize children if not already present
            parent.children.append(person)
            self.members[person.name] = person
            return True
        else:
            print(f"Parent {parent_name} not found.")
            return False

    def remove_person(self, name):
        """
        Removes a person and all their descendants from the family tree.

        :param name: The name of the person to remove.
        :return: True if removal was successful, False otherwise.
        """
        if name in self.members:
            if self.root and self.root.name == name:
                # If removing the root, reset the tree
                self.root = None
                self.members.clear()
            else:
                self._remove_subtree(name)
            return True
        else:
            print(f"Person {name} not found.")
            return False

    def _remove_subtree(self, name):
        """
        Recursively removes a person and their descendants.

        :param name: The name of the person to remove.
        """
        person = self.members.pop(name)
        if hasattr(person, "children"):
            for child in person.children:
                self._remove_subtree(child.name)

    def search_person(self, name):
        """
        Searches for a person in the family tree by their name.

        :param name: The name of the person to search for.
        :return: The Person object if found, None otherwise.
        """
        return self.members.get(name, None)

    def sort_members(self, key="name"):
        """
        Sorts the members of the family tree by a specified attribute.

        :param key: The attribute to sort by ("name", "birth_date", "relationship").
        :return: A list of Person objects sorted by the specified attribute.
        """
        if key not in ["name", "birth_date", "relationship"]:
            print("Invalid key for sorting.")
            return []
        return sorted(self.members.values(), key=lambda person: getattr(person, key, None))
