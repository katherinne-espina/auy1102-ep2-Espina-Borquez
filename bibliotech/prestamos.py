"""Funciones para gestionar préstamos de libros."""

from datetime import timedelta


def calcular_fecha_devolucion(fecha_prestamo, tipo_usuario):
    """Devuelve la fecha límite de devolución de un libro."""
    if tipo_usuario == "estudiante":
        dias_prestamo = 7
    elif tipo_usuario == "docente":
        dias_prestamo = 14
    else:
        raise ValueError("Tipo de usuario no válido.")

    fecha_devolucion = fecha_prestamo + timedelta(
        days=dias_prestamo
    )

    if fecha_devolucion.weekday() == 5:
        fecha_devolucion += timedelta(days=2)
    elif fecha_devolucion.weekday() == 6:
        fecha_devolucion += timedelta(days=1)

    return fecha_devolucion


def calcular_multa(dias_atraso, tipo_usuario):
    """Calcula la multa por atraso, con un máximo de $10.000."""
    if dias_atraso < 0:
        raise ValueError("Los días no pueden ser negativos.")

    if tipo_usuario == "estudiante":
        tarifa_diaria = 500
    elif tipo_usuario == "docente":
        tarifa_diaria = 300
    else:
        raise ValueError("Tipo de usuario no válido.")

    return min(dias_atraso * tarifa_diaria, 10000)
