import requests
import unittest
import json
import os
import time
import sys
import xml.etree.ElementTree as ET
import subprocess

"""
UNIT TESTS FOR ECSE 429 PROJECT A
ON LOCALHOST:4567 
API DOCUMENTATION CAN BE FOUND ON LOCALHOST:4567/docs
"""

# def refresh():
    

#     try:
#         # os.system("curl --location --request GET 'http://localhost:4567/shutdown'")
#         subprocess.run(["curl", "--location", "--request", "GET", "http://localhost:4567/shutdown"])
#     except requests.exceptions.RequestException as e:
#         print('shit')
    
#     subprocess.run(["java", "-jar", "../runTodoManagerRestAPI-1.5.5.jar"])
#     return
        

# def refresh():    
#     try:
#         requests.get("http://localhost:4567/shutdown")
#         os.system("sleep 2s")
#         os.system("java -jar ../runTodoManagerRestAPI-1.5.5.jar")
#     except requests.exceptions.RequestException as e:
#         print('shit')
    
#     return
    

# #check if http status code is 200 when service is running
# def test_http_returns_code_200():
#      response = requests.get("http://localhost:4567")
#      assert response.status_code == 200

""" localhost:4567/todos TESTS
------------------------------------------------------------------- """
    
# GET /todos 
def test_GET_todo():   
    """Test for GET /todo with JSON response
    Expecting: 200 OK """
    response = requests.get("http://localhost:4567/todos")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["todos"][0]["id"] == "1"
    


# GET /todos XML
def test_GET_todo_XML():
    """Test for GET /todo with XML response
    Expecting: 200 OK """
    response = requests.get("http://localhost:4567/todos",
        headers = {
            'Content-type': 'application/xml',
            'Accept': 'application/xml'
        }
    )
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    
    response_body_as_xml = ET.fromstring(response.content)
    xml_tree = ET.ElementTree(response_body_as_xml)
    todo = xml_tree.find("todo")
    assert todo.tag == "todo"
    

   
    
# HEAD /todos  
def test_HEAD_todo():
    """Test for HEAD /todo with Header response
    Expecting: 200 OK """
    response = requests.get("http://localhost:4567/todos")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Transfer-Encoding"] == "chunked"
    
    

# test POST /todos with title
def test_POST_todo_with_title():
    """Test for POST /todo with JSON request
    Expecting: 201 OK, JSON output [title] """
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

    

# test POST /todos returns wrror code without title (was not performed in exploratory testing)
def test_POST_todo_without_title():
    """Test for POST /todo with JSON request
    Expecting: 400 """
    json_input = {
            
            "description": "project"
            
        }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos", request_json)
    assert response.status_code == 400
    
""" localhost:4567/todos/:id TESTS
------------------------------------------------------------------- """

# GET /todos/:id
def test_GET_todo_id():
    """Test for GET /todo/:id with JSON ouput
    Expecting: 200 OK, JSON output [title] and [id] """
    response = requests.get("http://localhost:4567/todos/1")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["todos"][0]["id"] == "1"
    assert response_body["todos"][0]["title"] == "scan paperwork"


# GET /todos/:id with XML
def test_GET_todo_id_XML():
    """Test for GET /todo/:id with XML request
    Expecting: 200 OK, Header, XML response """
    response = requests.get("http://localhost:4567/todos/1",
        headers = {
            'Content-type': 'application/xml',
            'Accept': 'application/xml'
        }
    )
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    
    response_body_as_xml = ET.fromstring(response.content)
    xml_tree = ET.ElementTree(response_body_as_xml)
    todo = xml_tree.find("todo")
    assert todo.tag == "todo"
    


# HEAD /todos/:id:
def test_HEAD_todo_id():
    """Test for HEAD /todo/:id 
    Expecting: 200 OK, Header """
    response = requests.get("http://localhost:4567/todos/1")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Transfer-Encoding"] == "chunked"
    
    
#test POST /todos/:id with title and description of VALID ID = 1
def test_POST_todo_id_with_title_validID():
    """Test for POST /todo/:id with JSON request
    Expecting: 200 OK """
    json_input = {
            
            "title": "Testing Post with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    #create post request
    response = requests.post("http://localhost:4567/todos/1", request_json)
    assert response.status_code == 200

#Test for DELETE /todos/:id with INVALID ID of 7
def test_DELETE_invalidID():
    """Test for DELETE /todo/:id with Invalid ID request
    Expecting: 404 """
    response = requests.delete("http://localhost:4567/todos/7")
    assert response.status_code == 404
    

#Test for PUT /todos/:id with INVALID ID of 7
def test_PUT_invalidID():
    """Test for PUT /todo/:id with JSON request and Invalid ID
    Expecting: 404 """
    json_input = {
            
            "title": "Testing PUT with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    response = requests.put("http://localhost:4567/todos/7", request_json)
    assert response.status_code == 404
    

#Test for PUT /todos/:id with VALID ID of 1
def test_PUT_validID():
    """Test for PUT /todo/:id with JSON request and Valid ID
    Expecting: 200 OK """
    json_input = {
            
            "title": "Testing PUT with updated Title",
            "description": "updated Description"
            
        }
    request_json = json.dumps(json_input)
    response = requests.put("http://localhost:4567/todos/1",request_json)
    assert response.status_code == 200
    
""" localhost:4567/todos/:id/tasksof TESTS
------------------------------------------------------------------- """
# GET /todos/:id/tasksof
def test_GET_todo_id_taskof():
    """Test for GET /todo/:id/taskof wth Valid ID request
    Expecting: 200 OK, JSON response [id]"""
    response = requests.get("http://localhost:4567/todos/1/tasksof")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["projects"][0]["id"] == "1"
    
    
# GET /todos/:id/tasksof
def test_GET_todo_id_taskof_XML():
    """Test for GET /todo/:id/taskof wth Valid ID request
    Expecting: 200 OK, XML response"""
    response = requests.get("http://localhost:4567/todos/1/tasksof",
        headers = {
            'Content-type': 'application/xml',
            'Accept': 'application/xml'
        }
    )
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
       
    
    
# HEAD /todos/:id/tasksof
def test_HEAD_todo_id_taskof():
    """Test for HEAD /todo/:id/taskof wth Valid ID request
    Expecting: 200 OK, Header"""
    response = requests.get("http://localhost:4567/todos/1")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Transfer-Encoding"] == "chunked"
        

# POST /todos/:id/tasksof returns 404 with invalid id
def test_POST_todo_id_taskof_with_invalid_id():
    """Test for POST /todo/:id/taskof wth Invalid ID JSON request
    Expecting: 404 """
    json_input = {
            
            "id": "1"
            
        }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos/819/tasksof", request_json)
    assert response.status_code == 404
    
    
# POST /todos/:id/tasksof returns 404 with valid id
def test_POST_todo_id_taskof_with_valid_id():
    """Test for POST /todo/:id/taskof wth Valid ID JSON request
    Expecting: 201 """
    json_input = {
            
            "id": "1"
            
        }
    request_json = json.dumps(json_input)
    
    #create post request
    response = requests.post("http://localhost:4567/todos/3/tasksof", request_json)
    assert response.status_code == 201
    

# /todos/:id/tasksof/:id
def test_DELTE_todo_id_taskof_with_valid_id():
    """Test for DELETE /todo/:id/taskof wth Valid IDs
    Expecting: 200 """
    #create delete request
    response = requests.delete("http://localhost:4567/todos/2/tasksof/1")
    assert response.status_code == 200


# /todos/:id/tasksof/:id fails deleting instance that has already been deleted
def test_DELETE_todo_id_taskof_invalid_id():
    """Test for DELETE /todo/:id/taskof wth instance already created
    Expecting: 404 """
    #create delete request
    response = requests.delete("http://localhost:4567/todos/2/tasksof/1")
    assert response.status_code == 404    
    




    
    
    