"""Fixture de navegador y evidencia automática de fallos."""
from pathlib import Path
import logging
import pytest
from selenium import webdriver

CAPTURAS = Path(__file__).parent / "reports" / "screenshots"


@pytest.fixture
def driver(request):
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    yield navegador
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        CAPTURAS.mkdir(parents=True, exist_ok=True)
        ruta = CAPTURAS / f"{request.node.name}.png"
        navegador.save_screenshot(str(ruta))
        logging.error("Prueba fallida. Captura: %s", ruta)
    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    setattr(item, f"rep_{reporte.when}", reporte)
