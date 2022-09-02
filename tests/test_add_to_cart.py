
import os
from faker import Faker
from utils.sessions import demoqa, reqres

faker = Faker()


def test_add_to_cart_unauthorized():
    response = demoqa().post('/addproducttocart/catalog/31/1/1',
                             cookies={'Nop.customer': '0e3ba491-ed54-4787-9d5e-01abe391d269;'})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_authorized():
    auth_cookie_name = 'NOPCOMMERCE.AUTH'
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    response = demoqa().post('/login',
                             data={'Email': login, 'Password': password},
                             allow_redirects=False)
    auth_cookie_value = response.cookies.get(auth_cookie_name)

    response = demoqa().post('/addproducttocart/catalog/31/1/1',
                             cookies={auth_cookie_name: auth_cookie_value})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_create_user():
    name = faker.first_name()
    job = faker.job()
    user_data = {'name': name, 'job': job}

    response = reqres().post('/users', data=user_data)

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_update_user():
    name = faker.first_name()
    job = faker.job()
    user_data = {'name': name, 'job': job}

    response = reqres().put('/users/2', json=user_data)
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job