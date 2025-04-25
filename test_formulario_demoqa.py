from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def configurar_driver():
    """Inicializa el navegador Chrome."""
    service = Service(executable_path="C:\\Eliana\\ProyectoSelenium\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def completar_formulario(driver):
    """Completa y envía el formulario en DemoQA."""
    driver.get("https://demoqa.com/text-box")
    driver.find_element(By.ID, "userName").send_keys("Eliana Corujo")
    driver.find_element(By.ID, "userEmail").send_keys("eliana@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Montevideo, Uruguay")
    driver.find_element(By.ID, "permanentAddress").send_keys("Calle Falsa 123")
    driver.find_element(By.ID, "submit").click()

def verificar_resultado(driver):
    """Imprime el resultado después de enviar el formulario."""
    time.sleep(2)  # Espera breve para cargar resultado
    output = driver.find_element(By.ID, "output").text
    print("Resultado en pantalla:")
    print(output)

def main():
    """Función principal para ejecutar el flujo."""
    driver = configurar_driver()
    try:
        completar_formulario(driver)
        verificar_resultado(driver)
        input("Presiona ENTER para cerrar el navegador...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()





