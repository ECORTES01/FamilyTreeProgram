from models.relationship_graph import RelationshipGraph

def remove_relationship(graph, person1, person2):
    """
    Removes a relationship between two people in the RelationshipGraph.

    :param graph: The RelationshipGraph instance.
    :param person1: The name of the first person.
    :param person2: The name of the second person.
    :return: Success message or error message.
    """
    if person1 not in graph.graph or person2 not in graph.graph:
        return f"Error: One or both of the individuals ({person1}, {person2}) do not exist in the graph."

    # Remove the relationship
    graph.remove_relationship(person1, person2)
    return f"The relationship between {person1} and {person2} has been successfully removed."

# Example Usage
if __name__ == "__main__":
    # Create a RelationshipGraph instance
    relationship_graph = RelationshipGraph()

    # Add relationships for demonstration
    relationship_graph.add_relationship("John Doe", "Jane Doe", "Parent-Child")
    relationship_graph.add_relationship("Jane Doe", "Jake Smith", "Spouse")

    # Remove a relationship
    result = remove_relationship(relationship_graph, "John Doe", "Jane Doe")
    print(result)  # Output: The relationship between John Doe and Jane Doe has been successfully removed.
