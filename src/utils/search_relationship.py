from models.relationship_graph import RelationshipGraph

def search_relationship(graph, person1, person2):
    """
    Searches for a relationship between two people in the RelationshipGraph.

    :param graph: The RelationshipGraph instance.
    :param person1: The name of the first person.
    :param person2: The name of the second person.
    :return: A string describing the relationship if found, or an error message if not found.
    """
    # Check if the relationship exists
    relationship = graph.search_relationship(person1, person2)
    if relationship:
        return f"Relationship between {person1} and {person2}: {relationship}"
    else:
        return f"No relationship found between {person1} and {person2}."

# Example Usage
if __name__ == "__main__":
    # Create a RelationshipGraph instance
    relationship_graph = RelationshipGraph()

    # Add relationships for demonstration
    relationship_graph.add_relationship("John Doe", "Jane Doe", "Parent-Child")
    relationship_graph.add_relationship("Jane Doe", "Jake Smith", "Spouse")

    # Search for a relationship
    result = search_relationship(relationship_graph, "Jane Doe", "Jake Smith")
    print(result)  # Output: Relationship between Jane Doe and Jake Smith: Spouse
