# Módulo para validaciones de negocio

from models.cotizante import Cotizante

class BusinessLogic:
    """Clase que contiene las validaciones principales para los cotizantes."""

    @staticmethod
    def validar_cotizante(cotizante: Cotizante) -> bool:
        """Valida si un cotizante cumple los requisitos para ser trasladado."""
        if not cotizante.nombre or not cotizante.cedula:
            return False  # Nombre y cédula son obligatorios
        if cotizante.fondo_actual == cotizante.fondo_destino:
            return False  # El fondo actual no debe ser igual al destino
        return True

    @staticmethod
    def validar_embargo(cotizante: Cotizante) -> bool:
        """Determina si un cotizante está marcado para embargo."""
        return cotizante.embargo
