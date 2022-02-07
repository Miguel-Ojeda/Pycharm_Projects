"""
Ask the user for the name of a directory.
Iterate through each file in that directory (ignoring subdirectories),
getting (via os.stat) the size of the file and when it was last modified.

Create a JSON-formatted file on disk listing each filename, size, and modification timestamp.

Then read the file back in, and identify which files were modified most and least recently,
and which files are largest and smallest, in that directory.
"""

import os
from pathlib import Path
import json
# import arrow
import time


def save_stats_dir_json(directorio):
    directorio = Path(directorio)
    data = []
    for item in directorio.glob('*'):
        if item.is_dir():
            continue
        informacion = os.stat(item)
        info_dic = {'file': item.name,
                    'size': informacion.st_size,
                    'mod. time': informacion.st_mtime,
                    'mod. time string': time.asctime(time.localtime(informacion.st_mtime))}
        data.append(info_dic)
        print(info_dic)

    with open('files/dir_stat.json', 'w') as dir_info:
        json.dump(data, dir_info, indent='\t')


def display_stats_dir_json_v1(json_file):
    print(f'\n\nEstadísticas encontradas en el JSON:')
    with open(json_file) as jsonf:
        data = json.load(jsonf)
    max_size_item = min_size_item = most_recent_item = least_recent_item = data[0]

    for item in data[1:]:
        if item['size'] > max_size_item['size']:
            max_size_item = item
        elif item['size'] < min_size_item['size']:
            min_size_item = item
        if item['mod. time'] > most_recent_item['mod. time']:
            most_recent_item = item
        elif item['mod. time'] < least_recent_item['mod. time']:
            least_recent_item = item

    print(f'El elemento más pequeño es {min_size_item["file"]}",',
          f'ocupa {min_size_item["size"]:_} bytes')
    print(f'El elemento más grande es {max_size_item["file"]}",',
          f'ocupa {max_size_item["size"]:_} bytes')
    print(f'El elemento modificado hace más tiempo es {least_recent_item["file"]}",',
          f'fue modificado el {least_recent_item["mod. time string"]}.')
    print(f'El elemento modificado hace menos tiempo es {most_recent_item["file"]}",',
          f'fue modificado el {most_recent_item["mod. time string"]}.')


def display_stats_dir_json_v2(json_file):
    """
    Esta forma es más lenta pq recorre cada lista dos veces, una para encontrar el máximo
    otra para encontrar el mínimo.... La otra es mejor, pero pongo esta por mostrar
    otra forma
    """
    print(f'\n\nEstadísticas encontradas en el JSON V2:')
    with open(json_file) as jsonf:
        data = json.load(jsonf)

    size_list = []
    mod_time_list = []
    file_name_list = []
    for item in data:
        size_list.append(item['size'])
        mod_time_list.append(item['mod. time'])
        file_name_list.append(item['file'])

    min_size_index = size_list.index(min(size_list))
    max_size_index = size_list.index(max(size_list))
    min_mot_time_index = mod_time_list.index(min(mod_time_list))
    max_mot_time_index = mod_time_list.index(max(mod_time_list))

    print(f'El elemento más pequeño es {file_name_list[min_size_index]}",',
          f'ocupa {size_list[min_size_index]:_} bytes')
    print(f'El elemento más grande es {file_name_list[max_size_index]}",',
          f'ocupa {size_list[max_size_index]:_} bytes')
    print(f'El elemento modificado hace más tiempo es {file_name_list[min_mot_time_index]}",',
          f'fue modificado el {mod_time_list[min_mot_time_index]}')
    print(f'El elemento modificado hace menos tiempo es {file_name_list[max_mot_time_index]}",',
          f'fue modificado el {mod_time_list[max_mot_time_index]}')


directorio = 'C:/users/Miguel'
save_stats_dir_json(directorio)

display_stats_dir_json_v1('files/dir_stat.json')
display_stats_dir_json_v2('files/dir_stat.json')

