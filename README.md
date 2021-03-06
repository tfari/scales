# scales
 Display, listen, and manage a set of musical scales. (On Linux/OSx you need the `sox` package in order to be able 
 to listen to scales.)

***scales*** understands flats as {KEY}**B**, ex: ***BB*** (B flat), ***GB*** (G flat).

Whenever **SCALE_VALUES** needs to be passed, the format is {N1}-{N2}-{N3}, where **N**s are relative semitones from 
the previous key, (starting from either a passed **ROOT_KEY** or **C** if none is passed ) separated by "**-**" 
characters. Ex: "**2-3-5**" would be, (for C) : two semitones from C (aka: ***D***), then three semitones from D...
etc.

When listening to scales using the ***scale*** command, notes are relative to middle A by default, aka: 440.0hz, 
though the user can set a different frequency for ***middle-A*** by passing [ROOT-FREQ] (a float) after [KEY_NAME].


***scales*** comes with the following default scales:
* Major
* Minor (Shorthand for natural minor)
* Natural Minor
* Harmonic Minor
* Melodic Minor asc
* Melodic Minor desc
* Major Pentatonic
* Minor Pentatonic


All **SCALE_NAME**s and **KEY_NAME**s are interpreted case-insensitive.

## Usage
```
Usage: scales.py [OPTIONS] COMMAND [ARGS]...

  Display, listen, and manage a set of musical scales.

Options:
  --help  Show this message and exit.

Commands:
  add           Add Scale.
  edit          Edit scale with name SCALE_NAME to values SCALE_VALUES
  find          Find similar scales with root key ROOT_KEY, and a list of KEYS.
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
    
    find: find ROOT_KEY KEYS
        Find similar scales with root key ROOT_KEY, and a list of KEYS. KEYS should be a sequence of KEY_NAMES,  
        separated by '-' characters. Program will display an ordered list of all scales by matching KEYS.
        Ex:
             scales.py find C# D# A# G# F

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

    scale: scale SCALE_NAME [KEY_NAME] [ROOT_FREQ]
        Display the Scale SCALE_NAME on the key KEY_NAME. If no KEY_NAME is passed, produce scale using C as root key.
        If ROOT_FREQ is not passed, default middle-A to 440.0hz
        Ex:
            scales.py scale "My Scale"
            scales.py scale "My Scale" C
            scales.py scale "My Scale" Ab
            scales.py scale "My Scale" C 432
            scales.py scale "My Scale" D 982.54


## Requirements
* python 3.9 (due to type hinting)

### Modules
* click

### Sound
* Linux/OSx: you need package `sox`. In OSx you can use ***brew*** to get it.
