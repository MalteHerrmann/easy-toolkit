"""
easytk | Malte Herrmann

This is a python module for creating easy to use GUI windows, which can
be instantiated with only a couple of high-level commands. To achieve this,
this module basically contains an API wrapper to the tkinter module.

To create a window, simply call the Window class with the wanted return value
type (e.g. "YesNo", "Selection", "OkCancel", "Message") and add the desired
widgets to it with the corresponding add_* methods.

    window = easytk.Window("YesNo")
    window.add_label("Test")
    window.add_entry("Test", default_value="Default")
    window.show()

Additionally, there are a few convenience functions for creating commonly
used user interfaces, like a simple yes/no dialogue, or a dropdown selection.

    yes_or_no = easytk.ask_yes_no("Simple yes/no question.")

"""

__version__ = "0.2.0"

# ------------------------------
# High level imports
#
from easytk.window import Window
