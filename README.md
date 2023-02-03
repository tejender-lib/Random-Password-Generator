# Random-Password-Generator
Introduction:
This project is a simple graphical user interface (GUI) application that generates random passwords and stores them in a text file.
The password length can be specified by the user and the generated password will be displayed in the password field. The passwords 
are stored in a text file "passwords.txt" with their respective password count.

Components:
The following components make up the Random Password Generator application:

Tkinter GUI library: Tkinter is used to create the GUI for the application. It provides various widgets such as labels,
entries, buttons, etc. that are used to create the user interface.

Random library: The random library is used to generate the random passwords. It provides the "choices" function that can be used
to generate random characters from a given set of characters.

String library: The string library is used to provide the set of characters that can be used to generate the random password.
It provides the "ascii_uppercase", "ascii_lowercase", "digits", and "punctuation" constants that are used to generate the password.

Code Explanation:
The following is a brief explanation of the code:

The "generate_password" function generates a password with the length specified in the "length_entry" widget.
The password is generated using the "choices" function from the random library, which generates random characters from a given
set of characters.

The generated password is then inserted into the "password_entry" widget and written to the "passwords.txt" file along with
its password count.

The "passwords.txt" file is opened in read mode and its last line is read to extract the password count. If the file does not exist,
a new file will be created when the password is generated for the first time.

The Tkinter GUI is created using various widgets such as labels, entries, and buttons. The "length_entry" widget is used to specify
the password length, the "generate_button" triggers the "generate_password" function, and the "password_entry" displays the
generated password.

Example:
When the application is run, a GUI window will be displayed as shown below. The user can specify the password length and click the
"Generate" button to generate a random password. The generated password will be displayed in the "Password" field and stored in the
"passwords.txt" file.

Conclusion:
The Random Password Generator is a simple and easy-to-use application for generating and storing random passwords.
It can be used for personal or educational purposes and can be further extended to meet specific requirements. The application is
developed using the Tkinter GUI library, the random library, and the string library, which makes it a useful demonstration of the
functionality of these libraries.



