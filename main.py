#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    """ PUT /api/v1/states/<state_id>
    """
    r = requests.put("http://127.0.0.1:5000/api/v1/states/{}".format("doesn_t_exist"), data=json.dumps({ 'name': "NewStateName" }), headers={ 'Content-Type': "application/json" })
    print(r.status_code)
