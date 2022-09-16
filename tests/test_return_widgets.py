"""
Unit-testing module for the `easytk` return widgets.
"""

# --------------------
# Imports
#
import easytk


# --------------------
# Tests
#
def test_selection_should_return_tuple():
    expected = "Test123"
    window = easytk.Window("Selection", testing=True)
    window.add_file_dialog("Test File", default_value=expected)
    window.show()
    window.return_widget.get_return_values()
    returned = window.return_values
    assert returned == (expected, )


def test_selection_false_should_return_False():
    window = easytk.Window("SelectionFalse", testing=True)
    window.add_file_dialog("Press No.", default_value="Test123")
    window.show()
    window.return_widget.no_clicked()
    returned = window.return_values
    assert returned is False


def test_yes_no_should_return_True():
    window = easytk.Window("YesNo", testing=True)
    window.add_label("Press Yes.")
    window.show()
    window.return_widget.yes_clicked()
    returned = window.return_values
    assert returned is True


def test_yes_no_should_return_False():
    window = easytk.Window("YesNo", testing=True)
    window.add_label("Press No.")
    window.show()
    window.return_widget.no_clicked()
    returned = window.return_values
    assert returned is False

