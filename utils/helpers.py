"""Funciones reutilizables para las pruebas de SauceDemo."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


def iniciar_sesion(driver):
    """Inicia sesión y espera a que el inventario esté disponible."""
    driver.get(URL)
    espera = WebDriverWait(driver, 10)
    espera.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    espera.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    espera.until(EC.url_contains("/inventory.html"))
    espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
