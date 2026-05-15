from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    # Atributos de visibilidad privada
    __noheredado: bool = True
    # Atributos de visibilidad protegida
    _precio: float
    _ubicacion: dict[str, int]
    # Atributos de visibilidad pública
    marca: str
    ruedas: int
    @abstractmethod
    def trasladarse(self, dx: int, dy: int) -> dict[str, int]:
        """Actualiza la ubicacion del vehiculo en la pantalla.

        Args:
            dx (int): variación en coordenada horizontal
            dy (int): variación en coordenada vertical

        Returns:
            dict[int, int]: ubicacion hasta la que llegó
        """
        pass
