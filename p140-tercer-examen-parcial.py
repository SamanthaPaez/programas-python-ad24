# p140-tercer-examen-parcial 

class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        beca_status = "Becado" if self.becado else "Sin Beca"
        return f"Nombre: {self.nombre:<20} AñoNac: {self.año_nac:<5} Sexo: {self.sexo:<10} Becado: {beca_status}"

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def subtotal(self):
        total = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                total += self.costo
        return total

    def total_hombres(self):
        total = 0
        for jugador in self.jugadores:
            if jugador.sexo == "Hombre":
                total += 1
        return total

    def total_mujeres(self):
        total = 0
        for jugador in self.jugadores:
            if jugador.sexo == "Mujer":
                total += 1
        return total

    def mostrar_datos_generales(self):
        print(f"Nombre: {self.nombre:<10} Rango: {self.rango:<15} Costo: ${self.costo:,.2f}")

    def mostrar_jugadores(self):
        print(f"> {self.nombre} - {self.rango} - ({len(self.jugadores)})")
        for jugador in self.jugadores:
            print(jugador)
        print(f"- SubTotal : ${self.subtotal():,.2f}")

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_categorias(self):
        return len(self.categorias)

    def total_hombres(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.total_hombres()
        return total

    def total_mujeres(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.total_mujeres()
        return total

    def total_ingresos(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.subtotal()
        return total

    def mostrar_reporte(self):
        print("REPORTE DEL CLUB DEPORTIVO")
        print(f"Nombre: {self.nombre}")
        print(f"Propietario: {self.propietario}")
        print(f"Domicilio: {self.domicilio}\n")
        print(f"Total de Categorias: {self.total_categorias()}")
        print(f"Total de Hombres: {self.total_hombres()}")
        print(f"Total de Mujeres: {self.total_mujeres()}\n")

        print(">> Datos generales de las Categorías")
        for categoria in self.categorias:
            categoria.mostrar_datos_generales()
        
        print("\n>> Jugadores por Categoría:")
        for categoria in self.categorias:
            categoria.mostrar_jugadores()
        
        print(f"\n-> Total : ${self.total_ingresos():,.2f}")

# Creación de datos de prueba
academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

# Categorías y jugadores de prueba
categoria1 = Categoria("Junior A", "2006/2007/2008", 1250)
categoria1.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
categoria1.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", True))
categoria1.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

categoria2 = Categoria("Junior B", "2009/2010/2011", 850)
categoria2.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", False))
categoria2.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
categoria2.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

categoria3 = Categoria("Pony A", "2012/2013/2014", 700)
categoria3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
categoria3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
categoria3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))

# Agregar categorías a la academia
academia.agregar_categoria(categoria1)
academia.agregar_categoria(categoria2)
academia.agregar_categoria(categoria3)

# Imprimir reporte final
academia.mostrar_reporte()
