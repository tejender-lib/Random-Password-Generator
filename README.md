<h1> Random-Password-Generator </h1>
<h3>Introduction:</h3>
This project is a simple graphical user interface (GUI) application that generates random passwords and stores them in a text file.
The password length can be specified by the user and the generated password will be displayed in the password field. The passwords 
are stored in a text file "passwords.txt" with their respective password count.

<h3> Components: </h3>
The following components make up the Random Password Generator application:

<h3>Tkinter GUI library:</h3> Tkinter is used to create the GUI for the application. It provides various widgets such as labels,
entries, buttons, etc. that are used to create the user interface.

<h3>Random library:</h3> The random library is used to generate the random passwords. It provides the "choices" function that can be used
to generate random characters from a given set of characters.

<h3>String library:</h3> The string library is used to provide the set of characters that can be used to generate the random password.
It provides the "ascii_uppercase", "ascii_lowercase", "digits", and "punctuation" constants that are used to generate the password.

<h2>Code Explanation:</h2>
The following is a brief explanation of the code:

1. The "generate_password" function generates a password with the length specified in the "length_entry" widget.
The password is generated using the "choices" function from the random library, which generates random characters from a given
set of characters.

2. The generated password is then inserted into the "password_entry" widget and written to the "passwords.txt" file along with
its password count.

3. The "passwords.txt" file is opened in read mode and its last line is read to extract the password count. If the file does not exist,
a new file will be created when the password is generated for the first time.

4. The Tkinter GUI is created using various widgets such as labels, entries, and buttons. The "length_entry" widget is used to specify
the password length, the "generate_button" triggers the "generate_password" function, and the "password_entry" displays the
generated password.

<h3>Example:</h3>
When the application is run, a GUI window will be displayed as shown below. The user can specify the password length and click the
"Generate" button to generate a random password. The generated password will be displayed in the "Password" field and stored in the
"passwords.txt" file.

<h3>Conclusion:</h3>
The Random Password Generator is a simple and easy-to-use application for generating and storing random passwords.
It can be used for personal or educational purposes and can be further extended to meet specific requirements. The application is
developed using the Tkinter GUI library, the random library, and the string library, which makes it a useful demonstration of the
functionality of these libraries.



