"""Casos independientes de login, catálogo y carrito."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import iniciar_sesion


def test_login_exitoso(driver):
    iniciar_sesion(driver)
    assert "/inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    assert driver.title == "Swag Labs"


def test_catalogo_visible(driver):
    iniciar_sesion(driver)
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert productos, "El inventario no contiene productos"
    primero = productos[0]
    nombre = primero.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primero.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre.strip(), "El primer producto no tiene nombre"
    assert precio.startswith("$"), "El primer producto no muestra precio"
    print(f"Primer producto: {nombre} | Precio: {precio}")


def test_agregar_primer_producto_al_carrito(driver):
    iniciar_sesion(driver)
    espera = WebDriverWait(driver, 10)
    primero = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    nombre = primero.find_element(By.CLASS_NAME, "inventory_item_name").text
    primero.find_element(By.CSS_SELECTOR, "button[id^='add-to-cart']").click()
    badge = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1", f"Se esperaba 1 producto, se obtuvo {badge.text}"
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    espera.until(EC.url_contains("/cart.html"))
    nombres = [e.text for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert nombre in nombres, f"No aparece en el carrito el producto {nombre}"
