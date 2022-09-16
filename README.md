# easytk

A simple API wrapper to create functional `tkinter` GUIs using only a few lines.

![Tests](https://github.com/MalteHerrmann/easy-toolkit/actions/workflows/easytk_tests.yml/badge.svg)

## Examples

1. Simple selection from a list

```python
import easytk

values = [1, 2, 3]
selected_item = easytk.select(values, title='Please select the desired value: ')
```

2. Ask user for a boolean value

```python
import easytk

true_or_false = easytk.ask_yes_no("Pose a question here.")
```
