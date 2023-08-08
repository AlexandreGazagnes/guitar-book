# import pytest

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# from selenium.webdriver.firefox.options import Options


# def test_selenium():
#     """ """

#     driver = webdriver.Firefox()
#     driver.get("http://www.python.org")
#     assert "Python" in driver.title
#     elem = driver.find_element(By.NAME, "q")
#     elem.clear()
#     elem.send_keys("pycon")
#     elem.send_keys(Keys.RETURN)
#     assert "No results found." not in driver.page_source
#     driver.close()

#     url = "https://www.idealista.com/venta-viviendas/barcelona/eixample/la-dreta-de-l-eixample/?ordenado-por=fecha-publicacion-desc"
#     options = Options()
#     options.headless = False
#     driver = webdriver.Firefox(
#         options=options, executable_path="/home/kevin/Desktop/Inmosoft/geckodriver"
#     )
#     driver.get(url)
#     time.sleep(10)
