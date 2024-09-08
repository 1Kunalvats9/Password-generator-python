import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())  # Get the password length from the entry box
        
        if length <= 0:
            result_label.config(text="Length must be a positive integer.")
            return
        
        # Define possible characters for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        result_label.config(text=f"Generated Password: {password}")
    
    except ValueError:
        result_label.config(text="Please enter a valid number for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Window size
root.geometry("400x200")

# Create the length input label and entry
label_length = tk.Label(root, text="Enter the length of the password:")
label_length.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
