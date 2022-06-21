# scales
 Display, listen, and manage a set of musical scales. (On Linux/OSx you need the `sox` package in order to be able 
 to listen to scales.)

***scales*** understands flats as {KEY}**B**, ex: ***BB*** (B flat), ***GB*** (G flat).

Whenever **SCALE_VALUES** needs to be passed, the format is {N1}-{N2}-{N3}, where **N**s are relative semitones from 
the previous key, (starting from either a passed **ROOT_KEY** or **C** if none is passed ) separated by "**-**" 
characters. Ex: "**2-3-5**" would be, (for C) : two semitones from C(aka: ***D***), then three semitones from D...
etc.

When listening to scales, using the ***scale*** command, notes are by default relative to middle A, aka, 440hz, 
though the user can set a different frequency for ***A*** to start counting from.


Scales comes with the following default scales:
* Major
* Minor (Shorthand for natural minor)
* Natural Minor
* Harmonic Minor
* Melodic Minor asc
* Melodic Minor desc
* Major Pentatonic
* Minor Pentatonic


All **SCALE_NAME**s are interpreted case-insensitive.

## Usage
```shell
Usage: scales.py [OPTIONS] COMMAND [ARGS]...

  Display, listen, and manage a set of musical scales.

Options:
  --help  Show this message and exit.

Commands:
  add           Add Scale.
  edit          Edit scale with name SCALE_NAME to values SCALE_VALUES
  list          List all saved scales using KEY_NAME as root key.
  random        Display a random scale on the key KEY_NAME.
  remove        Remove scale with name SCALE_NAME.
  restore-data  Restore data to factory settings.
  scale         Display the Scale scale_name on the key KEY_NAME.
```

### Command Usage
    All commands can be called with option "--help".

    add: add SCALE_NAME SCALE_VALUES
        SCALE_VALUES should be a sequence of numbers, representing semitones, separated by '-' characters.
        Ex:
              scales.py add "Fifths" 7-7-7-7-7-7
              scales.py add "My Scale" 2-2-7-4-3

    edit: edit SCALE_NAME SCALE_VALUES
        Edit scale with name SCALE_NAME to values SCALE_VALUES. SCALE_VALUES should be a sequence of numbers, 
        representing semitones, separated by '-' characters.
        Ex:
              scales.py edit "My Scale" 1-2-3-4

    list: list [KEY_NAME]
        List all saved scales using KEY_NAME as root key. If no KEY_NAME is passed, produce scales using C as root key.
        Ex:
            scales.py list
            scales.py list BB

    random: random [KEY_NAME]
        Display a random scale on the key KEY_NAME. If no KEY_NAME is passed, produce scale using C as root key.
        Ex:
            scales.py random
            scales.py random Ab
    
    remove: remove SCALE_NAME 
        Remove scale with name SCALE_NAME.
        Ex:
            scales.py remove "My Scale"

    restore-data: restore-data
        Restore data to factory settings.

    scale: scale SCALE_NAME [KEY_NAME]
        Display the Scale SCALE_NAME on the key KEY_NAME. If no KEY_NAME is passed, produce scale using C as root key.
        Ex:
            scales.py scale "My Scale"
            scales.py scale "My Scale" C
            scales.py scale "My Scale" Ab


## Requirements
### Modules
* click

### Sound
* Linux/OSx: you need package `sox`. In OSx you can use ***brew*** to get it.
