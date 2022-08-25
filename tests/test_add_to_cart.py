import requests
from dotenv import load_dotenv
import os


def test_add_to_cart_unauthorized():
    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': '0e3ba491-ed54-4787-9d5e-01abe391d269;'})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_authorized():
    load_dotenv()
    auth_cookie_name = 'NOPCOMMERCE.AUTH'
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    response = requests.post('https://demowebshop.tricentis.com/login',
                             data={'Email': login, 'Password': password},
                             allow_redirects=False)
    auth_cookie_value = response.cookies.get(auth_cookie_name)
    print(auth_cookie_value)

    response = requests.post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
                             cookies={auth_cookie_name: auth_cookie_value})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
