# Informe de calidad: BiblioTech

## Integrantes

| Nombre | Usuario de GitHub |
|---|---|
| | |
| | |

## Parte 1. Línea base

Resultado de cada herramienta ANTES de hacer cambios.

| Herramienta | Comando | Resultado (copiar la línea de resumen) |
|---|---|---|
| pytest | `python -m pytest -v` | |
| Flake8 | `python -m flake8 --count` | |
| Bandit | `python -m bandit -r bibliotech` | Alta: · Media: · Baja: |
| pip-audit | `python -m pip_audit -r requirements.txt --no-deps --disable-pip` | |

## Parte 2. Pruebas unitarias

### Defectos encontrados

| Función | Prueba que lo evidencia | Causa del defecto | Corrección aplicada |
|---|---|---|---|
| | | | |

### Pruebas agregadas

| Archivo | Nombre de la prueba | Qué caso o valor límite cubre |
|---|---|---|
| | | |

Resultado final de `python -m pytest -v`:

## Parte 3. Análisis estático (Flake8)

| Código | Archivo:línea | Qué significa | Cómo lo corrigieron |
|---|---|---|---|
| | | | |

Resultado final de `python -m flake8 --count`:

## Parte 4. Análisis de seguridad

### 4A. Bandit

| ID | Severidad / Confianza | Archivo:línea | Riesgo concreto en BiblioTech | Corrección aplicada |
|---|---|---|---|---|
| | | | | |

Pruebas de seguridad agregadas (nombre y qué demuestran):

### 4B. pip-audit

| Paquete | Versión original | N° de vulnerabilidades | Versión actualizada |
|---|---|---|---|
| | | | |

### 4C. Revisión manual

Problema de seguridad que las herramientas NO reportaron, dónde está, por qué es un riesgo y cómo lo corrigieron:

## Parte 5. Pruebas de carga y estrés

Criterio de aceptación: con 30 usuarios simultáneos, el 95% de las búsquedas responde en menos de 500 ms y no hay errores.

### 5A. Línea base (antes de corregir)

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 10 | | | | |
| 30 | | | | |
| 60 | | | | |

### 5B. Diagnóstico y corrección

¿Qué observaron en las peticiones por segundo al aumentar los usuarios? ¿Qué línea de `carga/servidor.py` causaba el problema y por qué? ¿Cómo lo corrigieron?

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 30 (después de corregir) | | | | |

### 5C. Prueba de estrés

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 100 | | | | |
| 300 | | | | |
| 500 | | | | |
| 10 (después del estrés) | | | | |

Punto de quiebre, cómo falla el sistema (lentitud o errores 503) y si se recupera:

## Parte 6. Pipeline de calidad

Enlace a la ejecución en verde de GitHub Actions:

## Parte 7. Análisis

### 7.1 Análisis estático y dinámico
Diferencien análisis estático y dinámico. Clasifiquen las cuatro herramientas usadas y den un defecto de este examen que solo podía encontrarse con cada tipo de análisis.

### 7.2 Pruebas de regresión
¿Qué es una prueba de regresión? Indiquen qué pruebas cumplieron ese rol durante la Parte 4 y qué habría pasado sin ellas.

### 7.3 Pruebas de integración, carga y estrés
a) Propongan una prueba de integración para BiblioTech: qué módulos probarían juntos, con qué herramienta y con qué criterio de aceptación medible.
b) Con los resultados de su Parte 5, expliquen la diferencia entre la prueba de carga y la prueba de estrés que ejecutaron. ¿Por qué el defecto del servidor no podía detectarse con pruebas unitarias? Con sus números, ¿qué le recomendarían a la biblioteca para el inicio de semestre?

### 7.4 Evaluación de herramientas

| Herramienta | Qué detecta | Etapa del ciclo de vida / del pipeline donde actúa | Qué NO detecta (limitación) | Costo de no usarla |
|---|---|---|---|---|
| pytest | | | | |
| Flake8 | | | | |
| Bandit | | | | |
| pip-audit | | | | |
| Prueba de carga (`prueba_carga.py`) | | | | |

### 7.5 Recomendación
Si el equipo de BiblioTech solo pudiera mantener dos puertas de calidad en su pipeline, ¿cuáles elegirían y en qué orden? Justifiquen con los conceptos de detección temprana y mejora continua.
