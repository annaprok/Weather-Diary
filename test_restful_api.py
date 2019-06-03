import apijson
import requests
import json
def test_getall():
    response = requests.get('http://127.0.0.1:5000/')
    print(response.json())
    assert response.status_code == 200





def test_add():
    response = requests.get('http://127.0.0.1:5000/add/0/0/good')
    print(response.json())
    assert response.json() == "Success! Id:0"



def test_delete():
    response = requests.get('http://127.0.0.1:5000/del/0')
    print(response.json())
    assert response.status_code == 200



def test_getbyid():
    response = requests.get('http://127.0.0.1:5000/1')
    print(response.json())
    assert response.status_code == 200



test_getall()
test_getbyid()
test_add()
test_delete()
