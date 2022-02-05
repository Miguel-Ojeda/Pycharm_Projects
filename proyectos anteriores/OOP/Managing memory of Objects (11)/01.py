class Student:
    def __init__(self, name):
        self.name = name
        print('Creating Student object', self.name)

    def __del__(self):
        print('In the __del__ method for student:', self.name)


# Teacher class
class Teacher():
    def __init__(self):
        print('Creating the Teacher object')
        self.oStudent1 = Student('Joe')
        self.oStudent2 = Student('Sue')
        self.oStudent3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')


# Instantiate the Teacher object (that creates Student objects)
oTeacher = Teacher()
# Delete the Teacher object
# observar que al borrar el objeto teacher se va a invocar el método del del profesor
# además se van a reducir un reference_count de sus variables... de sus estudiantes..
# en este caso, como solo tenían un referencia, pues tb. se va a invocar su método __del__()
# del oTeacher

# otra forma
# teacher2 = oTeacher() # segunda referencia a la instancia
# del oTeacher   # aquí no pasa nada, pq queda otra referencia a la instancia
# print("Borrada la primera referencia")
# print("Ahora voy a borrar  la segunda referencia")
# del teacher2
# print("Borrada la segunda referencia")

# oTeacher = 9
# había una referencia, con lo que, al utilizar la variable para apuntar a otro sitio, el refcount es 0
# y por tanto el objeto se destruye, invocando por tanto la función __del__()

# oTeacher.oStudent2 = oTeacher.oStudent2 = oTeacher.oStudent3 = 15

print("HOLA")
oTeacher.oStudent1 = oTeacher.oStudent2 = 15

print("ADIÓS")
