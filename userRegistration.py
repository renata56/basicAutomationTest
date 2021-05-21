import time
import selenium.webdriver.support.event_firing_webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class user_Registration:

    driver = webdriver.Edge(r'C:\webdriver\bin\msedgedriver.exe')
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    sign_In = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
    time.sleep(6)
    create_Email = driver.find_element_by_id('email_create')
    create_Email.click()
    create_Email.send_keys('teste@teste.com.br')
    create_Email.send_keys(Keys.ENTER)

    time.sleep(12)
    select_Gender = driver.find_element_by_xpath('//*[@id="id_gender1"]')
    select_Gender.click()

    first_Name = driver.find_element_by_id('customer_firstname')
    first_Name.click()
    first_Name.send_keys('Roberto')

    last_Name = driver.find_element_by_id('customer_lastname')
    last_Name.click()
    last_Name.send_keys('Silva Pereira')

    password = driver.find_element_by_xpath('//*[@id="passwd"]')
    password.click()
    password.send_keys('123456')

    day_Birth = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select/option[7]')
    day_Birth.click()

    month_Birth = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[2]/div/select/option[5]')
    month_Birth.click()

    year_Birth = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select/option[29]')
    year_Birth.click()

    check_Newsletter = driver.find_element_by_xpath('//*[@id="newsletter"]')
    check_Newsletter.click()

    check_Partners = driver.find_element_by_xpath('//*[@id="optin"]')
    check_Partners.click()

    company = driver.find_element_by_id('company')
    company.click()
    company.send_keys('')

    address_Street = driver.find_element_by_id('address1')
    address_Street.click()
    address_Street.send_keys('fillmore street')

    address_Options = driver.find_element_by_id('address2')
    address_Options.click()
    address_Options.send_keys('Apartment 205')

    city = driver.find_element_by_id('city')
    city.send_keys('San Francisco')

    state = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select/option[6]')
    state.click()

    postalCode = driver.find_element_by_id('postcode')
    postalCode.click()
    postalCode.send_keys('94123')

    phone = driver.find_element_by_id('phone')
    phone.click()
    phone.send_keys('415 555-1212')

    mobile_Phone = driver.find_element_by_id('phone_mobile')
    mobile_Phone.click()
    mobile_Phone.send_keys('415 555-3030')

    submitAccount = driver.find_element_by_xpath('//*[@id="submitAccount"]').click()

    welcome_Print = driver.save_screenshot('screenshot.png')

    #tenta verificar se o elemento existe na página, se não existir, envia um e-mail dizendo q o teste falhou, se encontrar,
    #escreverá no terminal "o elemento foi encontrado", finalmente, ele irá sair da conta e fechará o browser.
    try:
        welcome_Account = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/p')

    except Exception as e:
        texto_Email = ('O elemento não foi encontrado, por favor, verificar!. Att, Teste automação')

        de = ''
        senha = ''
        copias = ['']
        para = ", ".join(copias)

        message = MIMEMultipart()
        message['From'] = de

        message['Subject'] = 'Automação teste'

        # Corpo do E-mail com anexos
        message.attach(MIMEText(texto_Email, ''))

        session = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Usuário do Gmail com porta
        session.starttls()  # Habilita a segurança
        session.login(de, senha)  # Login e senha de quem envia o e-mail
        texto = message.as_string()
        session.sendmail(de, copias, texto)
        session.quit()
    else:
        print('O elemento foi encontrado')

    finally:
        sign_Out = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        sign_Out.click()
        pass
    driver.quit()
