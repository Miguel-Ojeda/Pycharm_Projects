"""
Create a new LogFile class that expects to be initialized with a filename.

Inside of __init__, open the file for writing and assign it to an attribute, file, that sits on the instance.

Check that it’s possible to write to the file via the file attribute.
"""

class LogFile:
    def __init__(self, file_name):
        self.file = open(file_name, 'w', encoding='utf-8')


log_1 = LogFile('files/log_1.txt')

log_1.file.write('Esto es una línea\ny aquí la otra.')
log_1.file.close()