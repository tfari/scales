"""
Display, listen, and manage a set of musical scales.
"""
import os
import string
import sys
import json
import random

from typing import Optional

import click


# SET UP
random.seed()
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FILEPATH = f'{SCRIPT_PATH}/data.json'
KEYS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
FLAT_TRANSLATION_MAP = {'DB': 'C#', 'EB': 'D#', 'GB': 'F#', 'AB': 'G#', 'BB': 'A#'}


SCALE_MAP = {}
FACTORY_SCALE_MAP = {
    'Major': [2, 2, 1, 2, 2, 2, 1],
    'Minor': [2, 1, 2, 2, 1, 2, 2]
    # Harmonic Minor TODO
}

# SET UP

def __error_echo(err_msg: str, fatal: bool = False) -> None:
    """ Echo for errors, if fatal, exit application. Red foreground color."""
    click.secho(f'[!]{"FATAL ERROR: " if fatal else ""}{err_msg}', fg='red')
    if fatal:
        sys.exit(1)

def __info_echo(msg: str) -> None:
    """ Echo for successful operations. Yellow foreground color. """
    click.secho(f'[*] {msg}', fg='yellow')

def __echo(msg: str, fg_color: str = 'green') -> None:
    """ Normal echo, white foreground color by default. """
    click.secho(msg, fg=fg_color)

#

def _key_translate(key_name: str) -> Optional[str]:
    """
    Given key_name, return None if non exists, the translated key_name if it is a flat key, the key_name itself
    otherwise.
    """
    key_name = key_name.upper()
    if key_name in KEYS:
        return key_name
    elif key_name in FLAT_TRANSLATION_MAP.keys():
        return FLAT_TRANSLATION_MAP[key_name]
    else:
        return None


def _scale_make(root_key: str, scale_values: list[int]) -> list[str]:
    """ Make a scale from a root_key and scale_values  """
    index = KEYS.index(root_key)
    scale = [KEYS[index]]
    for sv in scale_values:
        index += sv
        scale.append(KEYS[index % len(KEYS)])

    return scale
#

@click.group()
def scales() -> None:
    """ Display, listen, and manage a set of musical scales. """
    global SCALE_MAP
    __load_data()


def __load_data() -> None:
    """ Load data.json file, if it doesn't exist, create a new one, if it is broken throw a fatal error. """
    global DATA_FILEPATH, SCALE_MAP
    try:
        SCALE_MAP = json.load(open(DATA_FILEPATH, 'r', encoding='utf-8'))
    except FileNotFoundError:
        __error_echo(f'Could not find data.json at: "{DATA_FILEPATH}".')
        __restore_data()
        __load_data()
    except json.JSONDecodeError as e:
        __error_echo(f'Broken data.json file, with error: {str(e)}', fatal=True)

@click.command('restore-data')
def restore_data() -> None:
    """ Restore data to factory settings. """
    __restore_data()

def __restore_data() -> None:
    """ Restore data to factory settings. We need this indirection because of how click works. """
    __info_echo('Restored data.json to factory settings.')
    __save_data(FACTORY_SCALE_MAP)


def __save_data(scale_map: dict) -> None:
    """ Write JSON file scale_map on DATA_FILEPATH """
    json.dump(scale_map, open(DATA_FILEPATH, 'w', encoding='utf-8'), indent=4)


@click.command('list')
@click.argument('KEY_NAME', required=False, default='C')
def list_scale_data(key_name: str = 'C') -> None:
    """ List all saved scales using KEY_NAME as root key. If no KEY_NAME is passed, produce scales using C as root
    key. """
    global SCALE_MAP
    key_name_final = _key_translate(key_name)
    if not key_name_final:
        __error_echo(f'Could not understand key: {key_name}')
    else:
        __info_echo(f'Listing {len(SCALE_MAP)} scales:')
        for scale_name in SCALE_MAP.keys():
            __echo(f'Scale: "{scale_name}" - '
                   f'Values: "{"-".join([str(sv) for sv in SCALE_MAP[scale_name]])}" - '
                   f'Example ({key_name.upper()}) - {"-".join(_scale_make(key_name_final, SCALE_MAP[scale_name]))}')

@click.command('scale')
@click.argument('SCALE_NAME')
@click.argument('KEY_NAME', required=False, default='C')
def display_scale(scale_name: str, key_name: str = 'C') -> None:
    """ Display the Scale scale_name on the key KEY_NAME. If no KEY_NAME is passed, produce scale using C as root
    key. """
    global SCALE_MAP
    scale_name_real = [sn for sn in SCALE_MAP.keys() if sn.upper() == scale_name.upper()]
    if not scale_name_real:
        __error_echo(f'Could not find scale: "{scale_name}"')
    else:
        scale_name_real = scale_name_real[0]
        key_name_final = _key_translate(key_name)
        if not key_name_final:
            __error_echo(f'Could not understand key: {key_name}')
        else:
            __echo(f'"{scale_name_real}" scale in "{key_name.upper()}" : '
                   f'{"-".join(_scale_make(key_name_final, SCALE_MAP[scale_name_real]))}')

@click.command('random')
@click.argument('KEY_NAME', required=False, default='C')
def random_scale(key_name: str = 'C') -> None:
    """ Display a random scale on the key KEY_NAME. If no KEY_NAME is passed, produce scale using C as root key. """
    scale_name = random.choice(list(SCALE_MAP.keys()))
    key_name_final = _key_translate(key_name)
    if not key_name_final:
        __error_echo(f'Could not understand key: {key_name}')
    else:
        __echo(f'"{scale_name}" scale in "{key_name.upper()}" : '
               f'{"-".join(_scale_make(key_name_final, SCALE_MAP[scale_name]))}')

@click.command('add')
@click.argument('SCALE_NAME')
@click.argument('SCALE_VALUES')
def add_scale(scale_name: str, scale_values: str) -> None:
    """ Add Scale. Scale Values should be only a sequence of numbers, separated by '-' characters. """
    wrong_chars = [sv for sv in scale_values if sv not in string.digits and sv != '-']
    if wrong_chars:
        __error_echo(f'Unexpected character(s) in scale_values: "{", ".join(wrong_chars)}"')
    else:
        scale_name_real = [sn for sn in SCALE_MAP.keys() if sn.upper() == scale_name.upper()]
        if scale_name_real:
            __error_echo(f'Scale name: "{scale_name}" already exists.')
        else:
            sv_ints = [sv for sv in scale_values.split('-')]
            for sv in sv_ints:
                if not sv or sv not in string.digits:
                    __error_echo(f'Invalid scale_values: "{scale_values}"', fatal=True)
            SCALE_MAP[scale_name] = [int(sv) for sv in sv_ints]
            __save_data(SCALE_MAP)
            __info_echo(f'Added scale: "{scale_name}" with values: {sv_ints}')

@click.command('remove')
@click.argument('SCALE_NAME')
def remove_scale(scale_name: str) -> None:
    """ Remove scale with name SCALE_NAME. """
    scale_name_real = [sn for sn in SCALE_MAP.keys() if sn.upper() == scale_name.upper()]
    if not scale_name_real:
        __error_echo(f'Scale name: "{scale_name}" does not exist.')
    else:
        scale_name_real = scale_name_real[0]
        SCALE_MAP.pop(scale_name_real)
        __save_data(SCALE_MAP)
        __info_echo(f'Removed scale: "{scale_name}"')

@click.command('edit')
@click.argument('SCALE_NAME')
@click.argument('SCALE_VALUES')
def edit_scale(scale_name: str, scale_values: str) -> None:
    """ Edit scale with name SCALE_NAME to values SCALE_VALUES """
    scale_name_real = [sn for sn in SCALE_MAP.keys() if sn.upper() == scale_name.upper()]
    if not scale_name_real:
        __error_echo(f'Scale name: "{scale_name}" does not exist.')
    else:
        sv_ints = [sv for sv in scale_values.split('-')]
        for sv in sv_ints:
            if not sv or sv not in string.digits:
                __error_echo(f'Invalid scale_values: "{scale_values}"', fatal=True)
        SCALE_MAP[scale_name] = [int(sv) for sv in sv_ints]
        __save_data(SCALE_MAP)
        __info_echo(f'Edited scale: "{scale_name}" with values: {sv_ints}')


if __name__ == '__main__':
    scales.add_command(list_scale_data)
    scales.add_command(restore_data)
    scales.add_command(display_scale)
    scales.add_command(random_scale)
    scales.add_command(add_scale)
    scales.add_command(remove_scale)
    scales.add_command(edit_scale)
    scales()
