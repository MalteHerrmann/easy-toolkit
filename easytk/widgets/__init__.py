"""
The widgets, that can be added to an `easytk` window, are defined in this
module. All widgets are subclasses of the abstract class `EasyWidget`, which
defines common methods and attributes, e.g. for adding the widget to the
main window.

It should be noted, that these widgets are not directly usable, but rather
should be added using the `add_*` methods of the `easytk.Window` class.
"""

from easytk.widgets.easy_checkbutton import EasyCheckbutton
from easytk.widgets.easy_combobox import EasyCombobox
from easytk.widgets.easy_entry import EasyEntry
from easytk.widgets.easy_file_dialog import EasyFileDialog
from easytk.widgets.easy_label import EasyLabel
from easytk.widgets.easy_listbox import EasyListbox
from easytk.widgets.easy_text import EasyText
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.return_buttons import EasyReturnWidget

# TODO: Enable widget resizing/filling to container
# TODO: Allow multiple columns next to each other (ideally with definable proportions)
# TODO: Add more widgets
# TODO: Move widgets to own file
# TODO: Add methods to enable / disable the widgets
# TODO: Change default anchors to "w"? Or add "label_anchor" attribute?
# TODO: Add user stories tests
# TODO: Use ttk styles?
