PDF Manager

Description

PDF Manager is a graphical user interface (GUI) application designed to help users easily perform common operations on PDF files. It allows you to merge, split, annotate, and encrypt/decrypt PDFs efficiently. The application is built using Python, leveraging the Tkinter library for the GUI and PyPDF2 for PDF manipulations.

Features

Merge PDFs: Combine multiple PDF files into one document.

Split PDF: Extract individual pages or split a PDF into multiple files.

Annotate PDF: Add annotations or comments to your PDF pages.

Encrypt PDF: Protect your PDF with a password.

Decrypt PDF: Remove password protection from encrypted PDFs.

Requirements

Python 3.8 or above

PyPDF2 library

Tkinter (comes pre-installed with Python on most systems)

To install the required libraries, run:

pip install PyPDF2

How to Run

Clone the repository or download the source code.

Open a terminal/command prompt and navigate to the project directory.

Run the following command:

python pdf_manager.py

User Guide

Launch the application.

Select an operation (Merge, Split, Annotate, Encrypt, or Decrypt PDF) by clicking the corresponding button.

Follow the prompts to select files and provide necessary inputs, such as passwords or save locations.

Check the status bar at the bottom of the application for updates.

Screenshots

Coming soon

Design Highlights

Subtle and Aesthetic Theme: The application uses a modern, clean design with soft colors and intuitive layouts.

Responsive Layout: The UI is designed to be user-friendly and compact.

Code Overview

PyPDF2: Handles all PDF manipulations (merging, splitting, encrypting, etc.).

Tkinter: Provides the GUI framework for creating buttons, labels, and file dialogs.

Modular Design: Functions are divided based on operations for clarity and maintainability.

Future Enhancements

Add drag-and-drop functionality for easier file selection.

Enable preview of PDF pages before performing operations.

Provide more annotation options (highlight, underline, etc.).

