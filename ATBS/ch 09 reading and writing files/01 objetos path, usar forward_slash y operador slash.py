from pathlib import Path

# La función Path nos devuelve un objeto (WindowsPath o PosixPath... dependiendo del SO) tipo path
# unidendo todos los items construye el path....
path1 = Path('spam', 'bacon', 'eggs')
print(path1) # spam\bacon\eggs
print(repr(path1))   # WindowsPath('spam/bacon/eggs')


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for item in myFiles:
    path = Path(r'C:\users\Miguel', item)
    print(path)


# Otra forma de conseguir lo mismo con el operador /
path_folder = path = Path(r'C:\users\Miguel')
for item in myFiles:
    path = path_folder / item
    print('Versión 2', path)


# CUIDADO, ES MEJOR SIEMPRE USAR CON Path el forwardslah!!!!
# Porque el backslash es un caracter válido para usar en nombres y carpetas en linux, macos,...
# Es mejor poner siempre el /, y ya la función Path hará lo correcto siempre!!!
# Lo anterior quedaría!!!
path_folder = path = Path(r'C:/users/Miguel')
for item in myFiles:
    path = path_folder / item
    print('Versión 3', path)
# Al imprimir nos aparece como es en nuestro sistema, Windows... independientemente de que escribiéramos /
# Versión 3 C:\users\Miguel\accounts.txt
# Versión 3 C:\users\Miguel\details.csv
# Versión 3 C:\users\Miguel\invite.docx

# Cuidado... no hacer nosotros la unión para conseguir el path
# con el operador + de las cadenas, o el join(), ya que no serviría!!
# Fallaría pq, aunque esté bien, este código sólo serviría en WINDOWS!!!!
homeFolder = r'C:\Users\Al'
subFolder = 'spam'
# homeFolder + '\\' + subFolder   -->  'C:\\Users\\Al\\spam'
# '\\'.join([homeFolder, subFolder]) --> 'C:\\Users\\Al\\spam'

# Con el oeprador / aplicable a paths esto está resuelto, pq actuará dependiendo del SO...
# Lo MISMO QUE ANTES; PERO BIEN!! SIRVE PARA CUALQUIER EQUIPO...
homeFolder = Path('C:/Users/Al')
nuevo_path = homeFolder / 'spam'
print(nuevo_path)

# Importante, este operador / para que funcione, el elemento de la izquierda debe ser un objeto path!!!!
# Esto fallaría... 'spam' / 'bacon' / 'eggs'


