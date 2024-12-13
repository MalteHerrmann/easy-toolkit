# easytk

A simple API wrapper to create functional `tkinter` GUIs using only a few lines.

Since this is only using `tkinter`, which comes built-in with many Python installations,
it can be run from within different environments that may restrict the use of other GUI libraries,
e.g. within the Python REPL of software like [Blender](https://www.blender.org/).

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

## Dev Environment

You can access the dev environment using [Nix flakes](https://nixos.wiki/wiki/Flakes):

```bash
nix develop
```

This will install the dependencies and open a shell with the necessary environment variables set.
