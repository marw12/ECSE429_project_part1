import requests


#check if http status code is 200
def test_get_todo_returns_code_200():
     response = requests.get("http://localhost:4567")
     assert response.status_code == 200
     
     
     
def test_get_todo():
    response = requests.get("http://localhost:4567/todos")
    response_body = response.json()
    assert response_body["todos"][0]["title"] == "file paperwork"