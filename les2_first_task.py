from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

url = 'http://suninjuly.github.io/explicit_wait2.html'
wd = webdriver.Chrome()
wd.get(url)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def explicit_wait():
    try:
        WebDriverWait(wd, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
        wd.find_element(By.XPATH, "//button[@id='book']").click()

        num_value = calc(wd.find_element(By.XPATH, "//span[@id='input_value']").text)

        wd.find_element(By.CSS_SELECTOR, '#answer').send_keys(num_value)
        wd.find_element(By.CSS_SELECTOR, "button#solve").click()

        # ответ alert в консоль, чтобы не ставить time.sleep() для закрытия браузера.
        alert = wd.switch_to.alert
        print(alert.text)

    finally:
        wd.quit()


if __name__ == '__main__':
    explicit_wait()
