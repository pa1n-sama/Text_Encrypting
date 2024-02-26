# Text Encryption and Decryption Application

This repository contains a simple yet effective text encryption and decryption application built with Python and Tkinter. The application offers a graphical user interface for easy interaction with the encryption/decryption functionalities.

## Features

- **Encryption**: Converts plain text into encrypted text using a randomly generated key.
- **Decryption**: Converts encrypted text back into plain text using the key stored in `Key.json`.
- **Graphical User Interface**: Provides a user-friendly interface to perform encryption and decryption operations.

## How It Works

The application consists of three main scripts:

1. **GUI Script**: Manages the application's graphical user interface, allowing the user to choose between encryption and decryption, input the text, and view the results.

2. **Key Generation Script**: Generates a random key mapping each character to another character and saves this key to `Key.json`. This key is essential for both encryption and decryption processes.

3. **Encryption/Decryption Script**: Performs the actual encryption and decryption of text using the generated key.

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the GUI script to start the application:
`main.json`
5. Follow the on-screen instructions to encrypt or decrypt text.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. We appreciate your contributions to making this application better!

## Acknowledgments

Thank you for checking out this application. If you have any suggestions or feedback, please open an issue or submit a pull request.

