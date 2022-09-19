import tkinter as tk
from typing import List, Literal
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyListbox(EasyWidget):
    """
    Class to define a widget, that displays a `tkinter.Listbox`.
    """

    # TODO: use height parameter (=number of lines) for listbox (-> https://www.pythontutorial.net/tkinter/tkinter-listbox/)
    def __init__(
            self,
            main_window,
            values: List[str],
            description: str = "",
            select_mode: Literal['browse', 'single', 'extended', 'multiple'] = "browse",
            width: int = None,
            height: int = None,
            label_width: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: ANCHORS = "center",
            justify: JUSTIFICATIONS = "left",
            add_to_grid: bool = True
    ):
        """
        Creates a new `EasyListbox` object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify, width)
        self.entries = values.copy()
        self.select_mode = select_mode

        if select_mode not in ('browse', 'single', 'extended', 'multiple'):
            raise ValueError(f"Forbidden selection mode: '{select_mode}'.")

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # Label
        self.label_string_var = tk.StringVar()
        self.label_string_var.set(description)
        self.label = tk.Label(
            self.grid_object,
            textvariable=self.label_string_var,
            width=label_width,
            anchor=anchor,
            justify=justify
        )

        # Listbox
        self.object_var = tk.Variable()
        self.object_var.set(self.entries)
        self.object = tk.Listbox(
            self.grid_object,
            listvariable=self.object_var,
            selectmode=select_mode,
        )

        # Arrange widgets
        self.label.pack(side="left", padx=(0, self.padx))
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Remove label if label text is empty
        if description.strip() == "":
            self.label.pack_forget()

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if not add_to_grid:
            self.remove_from_grid()

    def set(self, value: str) -> None:
        """
        Sets the `EasyListbox` to the given `value`.
        """
        if not isinstance(value, str):
            value = str(value)

        for idx, entry in enumerate(self.entries):
            if entry == value:
                self.object.selection_clear(0, 'end')
                self.object.activate(idx)
                self.object.index(idx)
                self.object.selection_set(idx)
                break
        else:
            self.insert_value(value)
            self.set(value)

    def insert_value(self, value: str) -> None:
        """
        Adds a new `value` to the contents of the `EasyListbox`.
        """
        if not isinstance(value, str):
            value = str(value)

        if value not in self.entries:
            self.entries.append(value)
            self.object_var.set(self.entries)

    def set_values(self, values: List[str]) -> None:
        """
        Adjusts the selectable `values` in the `EasyListbox`.
        """
        self.entries = values
        self.object_var.set(self.entries)

    def get(self) -> str:
        """
        Returns the currently selected item(s) in the `EasyListbox`.

        If the `select_mode` is set to `multiple` or `extended`, all
        selected values are returned as a list. Otherwise, a single
        string is returned.
        """
        selected_values = [self.object.get(idx) for idx in self.object.curselection()]
        if self.select_mode in ["multiple", "extended"]:
            return_value = selected_values
        else:
            if len(selected_values) > 0:
                return_value = selected_values[0]
            else:
                return_value = ""

        return return_value
