from selenium import webdriver


class __webdriver__VK():
    driver = webdriver.Chrome('webdriver/chromedriver.exe')
    hash = ''
    def __init__(self, hash):
        self.hash = hash
        self.driver.get("https://vk.com")
        self.buttonPresses('VkIdForm__signInButton')

    def driverHash(self):
        return self.hash

    def buttonPresses(self, button_class_name):
        self.driver.find_element_by_class_name(button_class_name).click()

    def inputKey(self, input_xpath_name, key):
        # print(self.driver.find_element_by_xpath(input_xpath_name))
        self.driver.find_element_by_xpath(input_xpath_name).send_keys(key)

    def content(self):
        return self.driver.find_element_by_tag_name("html").get_attribute("innerHTML")


VK = __webdriver__VK('hash')

VK.buttonPresses('VkIdForm__signInButton')
VK.inputKey('/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input', 'key')
# VK.buttonPresses('vkc__Button__primary')


# driver.quit()