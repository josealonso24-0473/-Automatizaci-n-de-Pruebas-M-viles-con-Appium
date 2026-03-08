# pon en un terminal parte esto: appium
# pon en otro terminal esto: python prueba_appium.py


from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time

# Configuración de capacidades
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.automation_name = "UiAutomator2"

# Evita que Appium reinicie apps
options.no_reset = True

# Abrir la app Settings (Configuración)
options.app_package = "com.android.settings"
options.app_activity = "com.android.settings.Settings"

# Conectar con Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Esperar a que abra
time.sleep(3)

print("La aplicación Settings se abrió correctamente")

# Obtener opciones de la pantalla
elementos = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")

for e in elementos:
    if e.text != "":
        print(e.text)

time.sleep(5)

# Cerrar sesión
driver.quit()