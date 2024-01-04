class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}"

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        return f"¡Aumento del {porcentaje}% aplicado! Nuevo salario: ${self.salario}"

# Crear instancias de la clase Empleado
empleado1 = Empleado("Juan Pérez", 50000)
empleado2 = Empleado("María García", 60000)

# Obtener información de los empleados
print(empleado1.obtener_informacion())
print(empleado2.obtener_informacion())

# Aplicar un aumento de salario al empleado1
print(empleado1.aumentar_salario(10))

# Obtener información actualizada del empleado1
print(empleado1.obtener_informacion())
