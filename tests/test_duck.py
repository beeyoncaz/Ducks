"""
Test the GET and POST endpoints in duck.py. 
The FastAPI server needs to be up and running.

Use the Python requests library for this.

In one single test function, call the GET endpoint and assert the response is empty.
Then, create a new duck using the POST endpoint and assert the response status code.
Then, call the GET endpoint again and assert that the duck we created previously is in the response.

Use pytest from the command line to run the tests -> cd tests && pytest test_duck.py

push code to git
"""


import requests

def test_duck_workflow():
    base_url = "http://127.0.0.1:8000/ducks/"

    # Step 1: GET /ducks/ - assert it's empty
    response = requests.get(base_url) 
    assert response.status_code == 200 # status code for successful responses
    assert response.json() == []

     # Step 2: POST /ducks/ - create a new duck
    new_duck = {
        "breed": "Mandarin",
        "age": 3
    }
    response = requests.post(base_url, json=new_duck) # sends duck to server
    assert response.status_code == 200  # checks that the server responded with a status code of 200 indicating a success.
    
    # Step 3: GET /ducks/ again - assert the new duck exists
    response = requests.get(base_url)
    assert response.status_code == 200
    ducks = response.json()
    assert len(ducks) == 1
    assert ducks[0]["breed"] == "Mandarin"
    assert ducks[0]["age"] == 3 


#github actions for running tests on push