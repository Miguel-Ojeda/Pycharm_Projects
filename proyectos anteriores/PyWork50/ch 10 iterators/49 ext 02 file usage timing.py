"""
Write a generator function, file_usage_timing, that takes a single directory name as an argument.
With each iteration, we get a tuple containing not just the current filename,
but also the three reports that we can get about a file’s most recent usage:
its access time (atime), modification time (mtime), and creation time (ctime).
Hint: all are available via the os.stat function.
"""

from pathlib import Path

def file_usage_timing(directorio):
    path_dir = Path(directorio)
    for item in path_dir.glob('*'):
        estadistica = item.stat()
        yield (estadistica.st_atime, estadistica.st_mtime, estadistica.st_ctime)



directorio = 'C:/Users/Angel Ojeda/Documents/Miguel'
for data in file_usage_timing(directorio):
    print(data)