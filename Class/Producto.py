class Producto:
    def __init__(self, codigo, nombre, codigo_barra, cantidad, cantidadxPaq, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.codigo_barra = codigo_barra
        self.cantidadxPaq = int(cantidadxPaq) # Convertir a entero, por que en la nomina es un string
        self.tipo = tipo
        self.cantidad = cantidad
        self.unidades = self.calc_unidades()  # Calcular las unidades al inicializar

    def __repr__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, codigo_barra={self.codigo_barra}, tipo={self.tipo}, cantidad={self.cantidad}), unidades={self.unidades}"
    
    def calc_unidades(self):
        return self.cantidad * self.cantidadxPaq