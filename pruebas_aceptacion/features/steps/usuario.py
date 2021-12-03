from behave import when, then, given
from unittest import TestCase

import time


@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@given(u'presiono el botón "Nuevo"')
def step_impl(context):
    context.driver.find_element_by_link_text('Nuevo').click()


@given(u'capturo el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_name('first_name').send_keys(nombre)


@given(u'capturo el primer apellido "{primer_apellido}"')
def step_impl(context, primer_apellido):
    context.driver.find_element_by_name('last_name').send_keys(primer_apellido)


@given(u'capturo el segundo apellido "{segundo_apellido}"')
def step_impl(context, segundo_apellido):
    context.driver.find_element_by_name(
        'segundo_apellido').send_keys(segundo_apellido)


@given(u'capturo el usuario "{username}"')
def step_impl(context, username):
    context.driver.find_element_by_name('username').send_keys(username)


@given(u'capturar la contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_name('password').send_keys(password)


@when(u'presiono el botón "Guardar"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/form/button').click()


@then(u'puedo ver al usuario "{username}" en la lista de usuarios.')
def step_impl(context, username):
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[4].text for row in rows[1:]]
    test = TestCase()
    test.assertIn(username, usuarios)


@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    rows = context.driver.find_elements_by_tag_name('ul')
    resultados = [row.find_elements_by_tag_name(
        'li')[0].text for row in rows[0:]]
    print(resultados)
    test = TestCase()
    test.assertIn(mensaje, resultados)
    time.sleep(2)
