from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, precio: float):
        self.marca = marca
        self.ruedas = 2
        self._precio = precio
        self._ubicacion = {"x": 0, "y": 0}
    # Sobreescritura del método abstracto. Hereda la documentación.
    def trasladarse(self, dx: int, dy: int) -> dict[str, int]:
        self._ubicacion["x"] += dx
        self._ubicacion["y"] += dy
        return self._ubicacion
    # Accesores o getters
    @property
    def precio(self) -> float:
        return round(max(0, self._precio), 2)
    @property
    def ubicacion(self) -> dict[str, int]:
        return self._ubicacion
    # Mutador o setter
    @precio.setter
    def precio(self, precio: float) -> None:
        if precio < 0:
            self._precio = 0
        else:
            self._precio = precio