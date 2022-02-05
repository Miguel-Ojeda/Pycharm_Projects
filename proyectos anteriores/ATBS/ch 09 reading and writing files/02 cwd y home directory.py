from pathlib import Path
import os   # para cambiar de directory

# Obtener el current working directory... Path.cwd()
print('El directorio actual para este programa es...')
print(Path.cwd())

# Peligroso, no conviene cambiar el cwd mientras un programa no está en marcha..
# por eso pathlib no incorpora la función
os.chdir(Path('C:/Windows'))
print(Path.cwd())

# Obtener el home directory... Path.home()
print('Home directory es', f'"{Path.home()}"')










