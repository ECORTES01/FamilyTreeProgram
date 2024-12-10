from models.relationship_graph import RelationshipGraph

def sort_relationships(graph, person):
    """
    Sorts the relationships of a specified person by relationship type.

    :param graph: The RelationshipGraph instance.
    :param person: The name of the person whose relationships are to be sorted.
    :return: A list of sorted relationships, or an error message if the person is not found.
    """
    if person not in graph.graph:
        return f"Error: {person} not found in the relationship graph."

    # Sort relationships by relationship type
    sorted_rels = graph.sort_relationships(person)
    return [f"{rel[0]} ({rel[1]})" for rel in sorted_rels]

# Example Usage
if __name__ == "__main__":
    # Create a RelationshipGraph instance
    relationship_graph = RelationshipGraph()

    # Add relationships for demonstration
    relationship_graph.add_relationship("John Doe", "Jane Doe", "Parent-Child")
    relationship_graph.add_relationship("John Doe", "Jake Smith", "Colleague")
    relationship_graph.add_relationship("John Doe", "Emily Doe", "Spouse")

    # Sort relationships for a person
    result = sort_relationships(relationship_graph, "John Doe")
    print("Sorted relationships for John Doe:", result)
