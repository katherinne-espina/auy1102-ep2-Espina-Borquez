
def calcular_fecha_devolucion(fecha_prestamo, tipo_usuario):
    """Devuelve la fecha límite de devolución de un libro."""
    if tipo_usuario == "estudiante":
        dias_prestamo = 7
    elif tipo_usuario == "docente":
        dias_prestamo = 14
    else:
        raise ValueError("Tipo de usuario no válido.")

    fecha_devolucion = fecha_prestamo + timedelta(days=dias_prestamo)

    if fecha_devolucion.weekday() == 5:
        fecha_devolucion += timedelta(days=2)
    elif fecha_devolucion.weekday() == 6:
        fecha_devolucion += timedelta(days=1)

    return fecha_devolucion
