import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image resizing
from models.person import Person
from models.family_tree import FamilyTree


class FamilyTreeApp:
    def __init__(self):
        self.tree = FamilyTree()
        self.window = tk.Tk()
        self.window.title("Family Tree")
        self.setup_gui()

    def setup_gui(self):
        """Sets up the GUI components."""
        # Resize and display the tree image
        try:
            original_image = Image.open("tree.png")  # Open the image
            resized_image = original_image.resize((300, 300))  # Resize to 300x300 pixels
            self.tree_image = ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage for tkinter
            tree_label = tk.Label(self.window, image=self.tree_image)
            tree_label.grid(row=0, column=0, columnspan=2)
        except Exception as e:
            print(f"Error loading image: {e}")
            tk.Label(self.window, text="Family Tree Program").grid(row=0, column=0, columnspan=2)

        # Labels and input fields
        tk.Label(self.window, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Birth Date (YYYY-MM-DD):").grid(row=2, column=0)
        self.birth_date_entry = tk.Entry(self.window)
        self.birth_date_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Relationship:").grid(row=3, column=0)
        self.relationship_entry = tk.Entry(self.window)
        self.relationship_entry.grid(row=3, column=1)

        tk.Label(self.window, text="Facts (comma-separated):").grid(row=4, column=0)
        self.facts_entry = tk.Entry(self.window)
        self.facts_entry.grid(row=4, column=1)

        tk.Label(self.window, text="Parent Name (optional):").grid(row=5, column=0)
        self.parent_entry = tk.Entry(self.window)
        self.parent_entry.grid(row=5, column=1)

        # Buttons
        tk.Button(self.window, text="Add Member", command=self.add_member).grid(row=6, column=0, columnspan=2)
        tk.Button(self.window, text="Display Family Tree", command=self.display_family_tree).grid(row=7, column=0, columnspan=2)
        tk.Button(self.window, text="Search Member", command=self.search_member).grid(row=8, column=0, columnspan=2)
        tk.Button(self.window, text="Remove Member", command=self.remove_member).grid(row=9, column=0, columnspan=2)
        tk.Button(self.window, text="Exit", command=self.window.quit).grid(row=10, column=0, columnspan=2)

        # Output area
        self.output_text = tk.Text(self.window, height=10, width=50)
        self.output_text.grid(row=11, column=0, columnspan=2)

    def add_member(self):
        """Adds a member to the family tree."""
        name = self.name_entry.get()
        birth_date = self.birth_date_entry.get()
        relationship = self.relationship_entry.get()
        facts = self.facts_entry.get().split(",")
        parent_name = self.parent_entry.get() or None

        if not name or not birth_date or not relationship:
            messagebox.showerror("Input Error", "Name, birth date, and relationship are required.")
            return

        person = Person(name, birth_date, relationship, facts)
        success = self.tree.add_person(parent_name, person)

        if success:
            messagebox.showinfo("Success", f"Added {name} to the family tree.")
            self.clear_inputs()
        else:
            messagebox.showerror("Error", f"Could not add {name}. Ensure the parent exists or set root correctly.")

    def display_family_tree(self):
        """Displays the family tree in the output area."""
        self.output_text.delete(1.0, tk.END)
        if not self.tree.root:
            self.output_text.insert(tk.END, "The family tree is empty.\n")
            return

        def traverse(node, level=0):
            self.output_text.insert(tk.END, f"{'  ' * level}{node.name} ({node.relationship})\n")
            if hasattr(node, "children"):
                for child in node.children:
                    traverse(child, level + 1)

        traverse(self.tree.root)

    def search_member(self):
        """Searches for a member in the family tree."""
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Input Error", "Please enter a name to search.")
            return

        person = self.tree.search_person(name)
        self.output_text.delete(1.0, tk.END)

        if person:
            self.output_text.insert(
                tk.END,
                f"Name: {person.name}\nBirth Date: {person.birth_date}\n"
                f"Relationship: {person.relationship}\nFacts: {', '.join(person.facts)}\n"
            )
        else:
            self.output_text.insert(tk.END, f"No member found with the name {name}.\n")

    def remove_member(self):
        """Removes a member from the family tree."""
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Input Error", "Please enter the name of the member to remove.")
            return

        success = self.tree.remove_person(name)
        if success:
            messagebox.showinfo("Success", f"{name} and their descendants have been removed from the tree.")
            self.clear_inputs()
            self.display_family_tree()  # Refresh the displayed tree
        else:
            messagebox.showerror("Error", f"Could not remove {name}. Ensure the name exists in the tree.")

    def clear_inputs(self):
        """Clears all input fields."""
        self.name_entry.delete(0, tk.END)
        self.birth_date_entry.delete(0, tk.END)
        self.relationship_entry.delete(0, tk.END)
        self.facts_entry.delete(0, tk.END)
        self.parent_entry.delete(0, tk.END)

    def run(self):
        """Runs the main GUI loop."""
        self.window.mainloop()


if __name__ == "__main__":
    app = FamilyTreeApp()
    app.run()
