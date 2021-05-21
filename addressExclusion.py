import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

class adress_Exclusion:

    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    sign_In = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
    time.sleep(3)

    email_Login = driver.find_element_by_id('email')
    email_Login.click()
    email_Login.send_keys('pereirateste@teste.com.br')

    password_login = driver.find_element_by_id('passwd')
    password_login.click()
    password_login.send_keys('123456')
    password_login.send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[3]/a/span').click()
    driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/ul/li[9]/a[2]').click()
    time.sleep(5)

    alert_Delete_Address = Alert(driver)
    alert_Delete_Address.accept()

    #tomada de decisão que verifica se  texto do elemento é diferente, e se for, retorna "Falha ao verificar texto do elemento"
    message_NoAddress = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]').text
    if message_NoAddress != 'No addresses are available. Add a new address':
        print('Falha ao verificar texto do elemento')
    else:
        print('Texto do elemento encontrado e verificado!')

    sign_Out = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
    sign_Out.click()

    driver.quit()

