"""Reportes para la jefatura de la biblioteca."""

import json
import os


def calcular_indicador(formula, datos):
    """Calcula un indicador usando una fórmula y sus datos.

    Ejemplo:
    calcular_indicador(
        "prestamos / socios",
        {"prestamos": 120, "socios": 40}
    ) devuelve 3.0.
    """
    # No ejecutar fórmulas arbitrarias con eval().
    variables_permitidas = {
        nombre: valor
        for nombre, valor in datos.items()
        if isinstance(nombre, str)
        and isinstance(valor, (int, float))
    }

    try:
        import ast
        import operator

        operaciones = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }

        def evaluar(nodo):
            if isinstance(nodo, ast.Expression):
                return evaluar(nodo.body)

            if isinstance(nodo, ast.Constant):
                if isinstance(nodo.value, (int, float)):
                    return nodo.value
                raise ValueError("Valor no permitido.")

            if isinstance(nodo, ast.Name):
                if nodo.id not in variables_permitidas:
                    raise ValueError("Variable no permitida.")
                return variables_permitidas[nodo.id]

            if isinstance(nodo, ast.BinOp):
                operacion = operaciones.get(type(nodo.op))
                if operacion is None:
                    raise ValueError("Operación no permitida.")
                return operacion(evaluar(nodo.left), evaluar(nodo.right))

            raise ValueError("Fórmula no permitida.")

        arbol = ast.parse(formula, mode="eval")
        return evaluar(arbol)

    except (SyntaxError, TypeError, ValueError, ZeroDivisionError):
        raise ValueError("No se pudo calcular el indicador.") from None


def exportar_respaldo(nombre_archivo):
    """Copia la base de datos a la carpeta de respaldos."""
    os.system("cp biblioteca.db respaldos/" + nombre_archivo)


def leer_configuracion(ruta):
    """Lee la configuración del sistema desde un archivo JSON."""
    try:
        with open(ruta, encoding="utf-8") as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except (OSError, json.JSONDecodeError):
        return {}
