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
