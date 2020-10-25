import requests
import json


#check if http status code is 200
def test_http_returns_code_200():
     response = requests.get("http://localhost:4567")
     assert response.status_code == 200
     
    
#GET /todos 
def test_GET_todo():
    response = requests.get("http://localhost:4567/todos")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["todos"][0]["title"] == "file paperwork"
    assert response_body["todos"][1]["title"] == "scan paperwork"
    
    
#HEAD /todos  
def test_HEAD_todo():
    response = requests.get("http://localhost:4567/todos")
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Transfer-Encoding"] == "chunked"
    

#test POST /todos with title
def test_POST_todo_with_title():
    json_input = {
            
            "title": "ecse 429",
            "description": "project"
            
        }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos", request_json)
    assert response.status_code == 201
    
    #check json output
    response_body = response.json()
    assert response_body["title"] == "ecse 429"
    

#test POST /todos returns wrror code without title
def test_POST_todo_without_title():
    json_input = {
            
            "description": "project"
            
        }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos", request_json)
    assert response.status_code == 400
    
    
#Osman code below

#Tests for GET /todos/:id VALID ID OF 1
def test_GET_todo_id(): 
    response = requests.get("http://localhost:4567/todos/1")
    response_body = response.json()
    assert response.status_code == 200  
    assert response_body["todos"][0]["id"] == "1"

#Tests for GET /todos/:id VALID ID OF 1
def test_GET_todo_id_INVALID(): 
    response = requests.get("http://localhost:4567/todos/69")
    response_body = response.json()
    assert response.status_code == 404  

    
#Test for HEAD /todos/:id  with VALID id of 1
def test_HEAD_todo():
    response = requests.get("http://localhost:4567/todos/1")
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Transfer-Encoding"] == "chunked"

#test POST /todos/:id with title and description of VALID ID = 1
def test_POST_todo_with_title():
    json_input = {
            
            "title": "Testing Post with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    #create post request
    response = requests.post("http://localhost:4567/todos/1", request_json)
    assert response.status_code == 400

#Test for DELETE /todos/:id with INVALID ID of 7
def test_DELETE_invalidID():
    response = requests.delete("http://localhost:4567/todos/7")
    assert response.status_code == 404
    #404 NOT FOUND ERROR EXPECTED HERE

#Test for PUT /todos/:id with INVALID ID of 7
def test_PUT_invalidID():
    json_input = {
            
            "title": "Testing PUT with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    response = requests.put("http://localhost:4567/todos/7", request_json)
    assert response.status_code == 404
    #404 NOT FOUND ERROR EXPECTED HERE

#Test for PUT /todos/:id with VALID ID of 1
def test_PUT_invalidID():
    json_input = {
            
            "title": "Testing PUT with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    response = requests.put("http://localhost:4567/todos/1",request_json)
    assert response.status_code == 200
  
