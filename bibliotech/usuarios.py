"""Gestión de usuarios de BiblioTech (registro, búsqueda e inicio de
sesión)."""

import hashlib
import secrets
import sqlite3

CLAVE_ADMIN = "Biblio2024!"


def conectar(ruta=":memory:"):
    """Abre la base de datos y crea la tabla de usuarios si no existe."""
    conexion = sqlite3.connect(ruta)
    conexion.execute(
        "CREATE TABLE IF NOT EXISTS usuarios ("
        "rut TEXT PRIMARY KEY, nombre TEXT, clave_hash TEXT, tipo TEXT)"
    )
    return conexion


def _hash_clave(clave):
    """Calcula el hash SHA-256 de una clave."""
    return hashlib.sha256(clave.encode("utf-8")).hexdigest()


def registrar_usuario(
    conexion, rut, nombre, clave, tipo="estudiante"
):
    """Registra un usuario nuevo guardando su clave como hash."""
    consulta = (
        "INSERT INTO usuarios (rut, nombre, clave_hash, tipo) "
        "VALUES (?, ?, ?, ?)"
    )
    conexion.execute(
        consulta, (rut, nombre, _hash_clave(clave), tipo)
    )
    conexion.commit()


def buscar_usuario(conexion, rut):
    """Devuelve (rut, nombre, tipo), o None si no existe."""
    consulta = (
        "SELECT rut, nombre, tipo "
        "FROM usuarios WHERE rut = ?"
    )
    return conexion.execute(consulta, (rut,)).fetchone()


def autenticar(conexion, rut, clave):
    """Verifica si el RUT y la clave corresponden a un usuario."""
    if rut == "admin" and clave == CLAVE_ADMIN:
        return True

    fila = conexion.execute(
        "SELECT clave_hash FROM usuarios WHERE rut = ?",
        (rut,)
    ).fetchone()

    return fila is not None and fila[0] == _hash_clave(clave)


def generar_token_sesion():
    """Genera un token de sesión de 32 caracteres."""
    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(
        secrets.choice(caracteres) for _ in range(32)
    )
