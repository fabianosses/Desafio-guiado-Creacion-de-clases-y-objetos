class Te:


# atributo de clase
    duracion = 365

    sabores = {
        1 : {"Nombre": "Te negro", "Tiempo": 3, "Recomendacion": "Desayuno"} ,
        2 : {"Nombre": "Te verde", "Tiempo": 5, "Recomendacion": "Almuerzo"},
        3 : {"Nombre": "Agua de hierbas", "Tiempo": 6, "Recomendacion": "Once"}
    }

    precios = {
        300, 3000,
        500, 5000
    }

    @staticmethod
    def tiempo_preparacion(sabor: int):
        """Retorna el tiempo de preparación en minutos del Té y recomendación según sabor ingresado"""

        pedido = Te.sabores[sabor]

        return pedido["Nombre"], pedido["Tiempo"], pedido["Recomendacion"]

    @staticmethod
    def precio(formato:int):
        """Retorna precio para el formato indicado"""
        return Te.precios[formato]
