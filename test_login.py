import time
from selenium import webdriver
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()
options.add_extension("/home/demo/drivers/adblock.crx")

driver = webdriver.Chrome(options=options)

url = 'http://automationexercise.com/'
driver.maximize_window()

class TestClass():

    def test_login(self):
        try:
            driver.get(url)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            login_signup = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
            name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("test")
            email_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("bogdan+12@mail.com")
            sign_button = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
            time.sleep(5)
            text_check = driver.find_element(By.XPATH, "//b[normalize-space()='Enter Account Information']").click()
            gender_check = driver.find_element(By.XPATH, "//input[@id='id_gender1']").click()
            name = driver.find_element(By.XPATH, "//input[@id='name']").send_keys('Bogdan')
            password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Vestell1200")
            driver.execute_script("window.scrollBy(0, 100);")
            day_birth = driver.find_element(By.XPATH, "//select[@id='days']").send_keys(24)
            month_birth = driver.find_element(By.XPATH, "//select[@id='months']").send_keys(11)
            yer_birth = driver.find_element(By.XPATH, "//select[@id='years']").send_keys(1996)
            driver.execute_script("window.scrollBy(0, 100);")
            news_check_box = driver.find_element(By.XPATH, "//input[@id='newsletter']").click()
            driver.execute_script("window.scrollBy(0, 100);")
            partners_check_box = driver.find_element(By.XPATH, "//input[@id='optin']").click()
            user_name = driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys('testUser')
            last_name = driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("testLastname")
            company_name = driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("TestComp")
            address1 = driver.find_element(By.XPATH, "//input[@id='address1']").send_keys('123 Main st')
            address2 = driver.find_element(By.XPATH, "//input[@id='address2']").send_keys('007 Wall st')
            driver.execute_script("window.scrollBy(0, 100);")
            country = driver.find_element(By.XPATH, "//select[@id='country']").send_keys("United States")
            state = driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Alabama")
            city = driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Dnipro")
            zip = driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("49026")
            mobile_number= driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("+380988126744")
            create_button = driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
            confrimation = driver.find_element(By.XPATH, "//b[normalize-space()='Account Created!']").text
            assert confrimation == "ACCOUNT CREATED!"
            next_button = driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()
            logged_user = driver.find_element(By.XPATH, "//li[10]//a[1]")
            delete_button = driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
            delete_confirmation = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b').text
            assert delete_confirmation == "ACCOUNT DELETED!"
        except Exception as e:
            print(f"Произошла ошибка: {e}")