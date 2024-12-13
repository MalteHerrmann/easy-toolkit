"""
This file includes a basic example to create a user interface
using the easytk package.

A window with a file selection is displayed and a `Selection`
button to return the selected filename or a `False` button.
"""

# ------------------------------
# Imports
#
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import easytk


# ------------------------------
# Functions
#
def main():
    """
    Main function to create the user interface.
    """
    # Create the main window
    window = easytk.Window("SelectionFalse")
    window.config(selection_text="Yep. Do it.")
    window.config(false_text="Nope")
    window.add_file_dialog("Test", default_value="Default", filetypes=[("Python files", "*.py")])
    window.add_entry("Example Input", default_value="Test Default")
    window.add_text("This is a lot of text over and over again"*5)
    window.add_text("This is a lot of text over and over again"*3, monospace=True)
    window.add_text("This is a lot of text over and over again"*3, export=True)
    returned_values = window.show()

    # Print the returned values
    print("These values were returned:\n", returned_values)


# ------------------------------
# Execution
#
if __name__ == "__main__":
    main()
