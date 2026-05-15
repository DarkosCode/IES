from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, precio: float, combustible: int = 100):
        self.marca = marca
        self.ruedas = 4
        self._precio = precio
        self._ubicacion = {"x": 0, "y": 0}
        self.__combustible = combustible
    def trasladarse(self, dx: int, dy: int) -> dict[str, int]:
        if(self.__combustible >= max(abs(dx), abs(dy))):
            self._ubicacion["x"] += dx # x = x + dx
            self._ubicacion["y"] += dy
            self.__combustible -= max(abs(dx), abs(dy)) # c = c - v
        else:
            # Código defectuoso visto en clase
            #for _ in range(self.__combustible):
            #    self._ubicacion["x"] += -1 if dx < 0 else 1
            #    self._ubicacion["y"] += -1 if dy < 0 else 1
            # es defectuoso porque
            # (1) el automóvil se pasa si hay más combustible que o dx o dy,
            # (2) el cálculo -1 if dx < 0 else 1 vale lo mismo en cada paso
            # de la iteración, costando recursos de procesamiento,
            # (3) ídem problema con -1 if dy < 0 else 1.
            
            # \ permite dividir una línea de código larga en múltiples
            # no se puede comentar a la derecha de un \
            self._ubicacion["x"] += \
                -1 if dx < 0 else 1 * min(self.__combustible, abs(dx))
            self._ubicacion["y"] += \
                -1 if dy < 0 else 1 * min(self.__combustible, abs(dy))
            self.__combustible = 0
        return self._ubicacion
    