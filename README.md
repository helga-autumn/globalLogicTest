# Global Logic Code Challenge
 
## Task
Create a function that returns the list of directions within the keyboard in order to enter the given text. 
Example: 
```
enter_text('hint1')
```

Should return: 
```
['down', 'select', 'right', 'select', 'right', 'right', 'right', 'right', 'right', 'select', 'down', 'left', 'select', 'up', 'up', 'right', 'right', 'select']
```

Advanced: implement the uppercase support. Selecting the 'shift' symbol on the keyboard makes only one next symbol to be uppercase	Given: Map of symbols on the keyboard:

Keymap:
```
keyboard = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'shift',
'h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6', ' ',
'o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'backspace',
'v', 'w', 'x', 'y', 'z', '-', '_', '@', '.', '0', 'enter'
]
```

Note: Starting position is always the first symbol ('a').

## Solution
The word for `enter_text(word)` function parameter will be populated from user input.
Keymap is converted to nested list for easier navigation to which direction we should move in order to get needed character. 
Converted Keymap:
```
keyboard = [
  ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'shift'],
  ['h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6', ' '],
  ['o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'backspace'],
  ['v', 'w', 'x', 'y', 'z', '-', '_', '@', '.', '0', 'enter']
]
```
The conception of shortest path to next character is basically taken from Taxicab geometry https://en.wikipedia.org/wiki/Taxicab_geometry

## Execution
The code is written using Python3 and can be executed from terminal.
Clone the repo, navigate to directory with script generateKeyboardDirections.py, make sure that latest python installed and PATH variables defined properly and run
```
$ python generateKeyboardDirections.py
```
