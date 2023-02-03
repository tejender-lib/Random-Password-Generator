import tkinter as tk
import random
import string

def generate_password():
    # Generate a password with the length specified in the length_entry widget
    password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=int(length_entry.get())))

    # Clear the password_entry widget and insert the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Open the file "passwords.txt" in append mode and write the generated password to it
    with open("passwords.txt", "a") as file:
        global counter
        counter += 1
        file.write(f"Password {counter}: {password}\n")

# Create the Tkinter root widget and set the title
root = tk.Tk()
root.title("Random Password Generator")
counter = 0
# Open the file "passwords.txt" in read mode
try:
    with open("passwords.txt", "r") as file:
        # Read all the lines in the file
        lines = file.readlines()
        if lines:
            # Get the last line in the file
            last_line = lines[-1]
            # Extract the password count from the last line
            counter = int(last_line.split(":")[0].split()[-1])
except FileNotFoundError:
    pass

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
