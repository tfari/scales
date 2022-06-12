# scales
 Display, listen, and manage a set of musical scales.

***scales*** understands flats, as {KEY}**B**, ex: ***BB*** (B flat), ***GB*** (G flat).

Whenever **SCALE_VALUES** is used, the format is {N1}-{N2}-{N3}, where **N**s are relative semitones, separated by 
"**-**" characters. ex: **2-3-5**.

 
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
## Requirements
### Modules
* click


## Further usage information
```shell
Usage: scales.py add [OPTIONS] SCALE_NAME SCALE_VALUES

  Add Scale. Scale Values should be only a sequence of numbers, separated by
  '-' characters.

Options:
  --help  Show this message and exit.

Examples:
  scales.py add "Fifths" 7-7-7-7-7-7
  scales.py add "My Scale" 2-2-7-4-3
```
```shell
Usage: scales.py edit [OPTIONS] SCALE_NAME SCALE_VALUES

  Edit scale with name SCALE_NAME to values SCALE_VALUES

Options:
  --help  Show this message and exit.

Examples:
  scales.py edit "My Scale" 1-2-3-4
```
```shell
Usage: scales.py list [OPTIONS] [KEY_NAME]

  List all saved scales using KEY_NAME as root key. If no KEY_NAME is passed,
  produce scales using C as root key.

Options:
  --help  Show this message and exit.

Examples:
  scales.py list
  scales.py list BB
```
```shell
Usage: scales.py random [OPTIONS] [KEY_NAME]

  Display a random scale on the key KEY_NAME. If no KEY_NAME is passed,
  produce scale using C as root key.

Options:
  --help  Show this message and exit.

Examples:
  scales.py random
  scales.py random Ab
```
```shell
Usage: scales.py remove [OPTIONS] SCALE_NAME

  Remove scale with name SCALE_NAME.

Options:
  --help  Show this message and exit.
 
Examples:
  scales.py remove "My Scale"
```
```shell
Usage: scales.py restore-data [OPTIONS]

  Restore data to factory settings.

Options:
  --help  Show this message and exit.

Examples:
  scales.py restore-data
```
```shell
Usage: scales.py scale [OPTIONS] SCALE_NAME [KEY_NAME]

  Display the Scale scale_name on the key KEY_NAME. If no KEY_NAME is passed,
  produce scale using C as root key.

Options:
  --help  Show this message and exit.

Examples:
  scales.py scale "My Scale"
  scales.py scale "My Scale" C
  scales.py scale "My Scale" Ab
```


