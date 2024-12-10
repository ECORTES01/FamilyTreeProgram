from models.relationship_graph import RelationshipGraph

def add_relationship(graph, person1, person2, relationship_type):
    """
    Adds a relationship between two people in the RelationshipGraph.

    :param graph: The RelationshipGraph instance.
    :param person1: The name of the first person.
    :param person2: The name of the second person.
    :param relationship_type: A string describing the relationship (e.g., "Spouse", "Parent-Child").
    :return: Success message or error message.
    """
    if not person1 or not person2 or not relationship_type:
        return "Invalid input: Both person names and relationship type are required."

    # Add the relationship to the graph
    graph.add_relationship(person1, person2, relationship_type)
    return f"Relationship '{relationship_type}' successfully added between {person1} and {person2}."

# Example Usage
if __name__ == "__main__":
    # Create a RelationshipGraph instance
    relationship_graph = RelationshipGraph()

    # Add a relationship between two people
    result = add_relationship(relationship_graph, "John Doe", "Jane Doe", "Parent-Child")
    print(result)  # Output: Relationship 'Parent-Child' successfully added between John Doe and Jane Doe.
