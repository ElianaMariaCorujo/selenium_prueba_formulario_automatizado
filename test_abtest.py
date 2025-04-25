from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Ruta correcta a chromedriver.exe
service = Service(executable_path="C:\\Eliana\\ProyectoSelenium\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# Ir a Google
driver.get("https://www.google.com")
print("Título de la página:", driver.title)

# Cerrar el navegador
driver.quit()
