import tkinter as tk
from tkinter import ttk,messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Legal Consultation App")

# Create a list to store consultations
consultations = []

# Function to handle the "Submit" button click event
def submit_consultation():
    name = name_entry.get()
    question = question_entry.get()
    
    if name and question:
        consultation = f"Name: {name}\nQuestion: {question}\n"
        consultations.append(consultation)
        consultation_listbox.insert(tk.END, consultation)
        
        # Clear the input fields
        name_entry.delete(0, tk.END)
        question_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both Name and Question fields.")

# Function to clear the consultation list
def clear_consultations():
    consultations.clear()
    consultation_listbox.delete(0, tk.END)

def display_educational_content():
    educational_text.delete(1.0, tk.END)  # Clear existing content
    educational_text.insert(tk.END, """Legal Articles:
1. Understanding Contract Law
2. What to Know About Family Law
3. Basics of Intellectual Property

FAQs:
1. How to Choose a Lawyer?
2. What Are Your Rights in a Rental Agreement?
3. Steps to Estate Planning

Resources:
1. Legal Aid Organizations
2. State Bar Associations
3. Legal Glossary""")
    

# Create and configure input fields and labels
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

question_label = tk.Label(root, text="Question:")
question_label.pack()
question_entry = tk.Entry(root)
question_entry.pack()

# Create and configure "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_consultation)
submit_button.pack()

# Create and configure consultation listbox
consultation_listbox = tk.Listbox(root, height=10, width=50)
consultation_listbox.pack()

# Create and configure "Clear" button
clear_button = tk.Button(root, text="Clear Consultations", command=clear_consultations)
clear_button.pack()

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Create the "Educational Content" tab
educational_tab = ttk.Frame(notebook)
notebook.add(educational_tab, text="Educational Content")

educational_tab = ttk.Frame(notebook)
notebook.add(educational_tab, text="Educational Content")

# Add a Text widget to display educational content
educational_text = tk.Text(educational_tab, wrap=tk.WORD, height=10, width=50)
educational_text.pack()

load_educational_button = tk.Button(educational_tab, text="Load Educational Content", command=display_educational_content)
load_educational_button.pack()


root.mainloop()
