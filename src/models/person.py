class Person:
    def __init__(self, name, birth_date, relationship, facts=None):
        """
        Initializes a new Person object.

        :param name: Full name of the person (str).
        :param birth_date: Date of birth (str, in 'YYYY-MM-DD' format).
        :param relationship: Relationship to the root person (str).
        :param facts: Optional list of interesting facts about the person (list of str).
        """
        self.name = name
        self.birth_date = birth_date
        self.relationship = relationship
        self.facts = facts if facts else []
        self.children = []  # List of child Person objects

    def add_fact(self, fact):
        """
        Adds a fact to the person's list of facts.

        :param fact: A short string describing a fact about the person (str).
        """
        self.facts.append(fact)

    def __str__(self):
        """
        String representation of the Person object for easy printing.
        """
        return f"{self.name} ({self.birth_date}) - {self.relationship}"
