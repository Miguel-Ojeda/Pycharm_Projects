# BTBS, ch 17 properties and dunder methods

'''
Si queremos 'esconder un atributo, podemos usar propiedades...
Son atributos a los que se le ha asignado métodos setter, getter y deleter...
Es una forma de esconder el atributo, para garantizar que no recibe un uso incorrecto
El getter es el método con el que el usuario accederá al valor
El setter es el método con el que el usuario cambiará el valor.... COmo es un método, aunque al usuario parezca
que está cambiando directamente el atributo, podremos hacer comprobaciones para asegurarnos de que no se le
asigna ningún valor incorrecto...
El deleter es el método que usaremos para borrar el objeto
'''

'''
Ejemplo, esconderemos un atributo someAttribute... el usaurio accedrá a somAtributte, pero realmente estará 
utilizando properties... veámoslo...'''

class ClassWithProperties:
    def __init__(self):
        self._someAttribute = 'some initial value'

    @property
    def someAttribute(self): # This is the "getter" method.
        print('Estamos en el getter')
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value): # This is the "setter" method.
        print('estamos en el setter')
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): # This is the "deleter" method.
        print('Estamos en el deletter')
        del self._someAttribute

'''El atributo real es objeto._someAtributte
Pero el usuario accederá a .someAttribute, pensando que está accediendo al atributo directamente
cuando en realidad está accediendo al atributo oculto, _someAtt... a través de los métodos'''

# Ejemplo
objeto = ClassWithProperties()
valor = objeto.someAttribute   # --> se imprime Estamos en el getter
objeto.someAttribute = 'cambiando a través del setter'  # --> se imprime, "Estamos en el setter"
del objeto.someAttribute   # se imprime, Estamos en el deletter


# Read-only properties
'''Es fácil, simplmente utilizaremos una propertie para esconder el valor que nos interesa, 
pero no crearemos los métodos setter ni deletter'''

class ClassWithReadOnlyAtt:
    def __init__(self):
        self._ReadOnly = 'secret staff'

    @property
    def ReadOnly(self): # This is the "getter" method.
        print('Estamos en el getter')
        return self._ReadOnly


objeto = ClassWithReadOnlyAtt()
valor = objeto.ReadOnly
print(valor)

# Intentamos cambiarlo
objeto.ReadOnly = 14  # --> AttributeError: can't set attribute 'ReadOnly'




