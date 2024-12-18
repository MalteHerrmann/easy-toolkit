"""
This file includes a basic example to create a user interface
using the easytk package.
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
    window = easytk.Window("Selection")
    window.config(selection_text="Return filename.")
    window.add_file_dialog("Test", default_value="Default", filetypes=[("Python files", "*.py")])
    returned_values = window.show()

    # Print the returned values
    print("These values were returned:\n", returned_values)


# ------------------------------
# Execution
#
if __name__ == "__main__":
    main()
