from collections import defaultdict

class RelationshipGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_relationship(self, person1, person2, relationship_type):
        self.graph[person1].append((person2, relationship_type))
        self.graph[person2].append((person1, relationship_type))

    def remove_relationship(self, person1, person2):
        self.graph[person1] = [rel for rel in self.graph[person1] if rel[0] != person2]
        self.graph[person2] = [rel for rel in self.graph[person2] if rel[0] != person1]

    def search_relationship(self, person1, person2):
        for rel in self.graph[person1]:
            if rel[0] == person2:
                return rel[1]
        return None

    def sort_relationships(self, person):
        if person in self.graph:
            return sorted(self.graph[person], key=lambda rel: rel[1])
        return []
