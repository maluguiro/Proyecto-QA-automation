# Proyecto QA Automation — Talento Tech

Pre-entrega de automatización funcional sobre [SauceDemo](https://www.saucedemo.com/), utilizando Python, Selenium WebDriver y Pytest.

## Objetivo
Automatizar tres flujos: inicio de sesión válido, verificación del catálogo y agregado del primer producto al carrito.

## Tecnologías
Python, Selenium WebDriver, Pytest, pytest-html, Git y GitHub.

## Estructura
- `tests/test_saucedemo.py`: tres pruebas independientes.
- `utils/helpers.py`: función reutilizable de inicio de sesión.
- `conftest.py`: navegador aislado por test y captura ante fallos en la fase de ejecución.
- `pytest.ini`: opciones para ejecutar y generar reporte HTML y log.
- `requirements.txt`: dependencias.
- `reports/`: reporte HTML, log y capturas cuando se ejecuten las pruebas.

## Instalación (Windows, PowerShell)
Requiere Python 3.10 o superior y Google Chrome.

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecución
```powershell
python -m pytest
```
Se genera `reports/reporte.html` y `reports/ejecucion.log`. Los fallos durante la ejecución del test generan capturas en `reports/screenshots/`.

## Casos de prueba
| ID | Caso | Verificaciones |
|---|---|---|
| QA-001 | Login | URL `/inventory.html`, encabezado `Products` y título `Swag Labs` |
| QA-002 | Catálogo | Encabezado, menú, filtro, producto visible y nombre/precio del primero |
| QA-003 | Carrito | Agregar primer producto, badge con valor 1 y producto presente en carrito |

Cada test inicia su propio navegador y realiza login de manera independiente.

## Estado de la entrega
**Código inicial publicado; ejecución real pendiente.** No se incluyen resultados simulados. Antes de entregar al docente, ejecutar los tests, revisar fallos y publicar el reporte HTML y el log reales.
