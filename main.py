#!/usr/bin/python3
"""Testing file
"""
import json
import requests

if __name__ == "__main__":
    r = requests.get("http://127.0.0.1:5000/api/v1/users")
    r_j = r.json()
    print(type(r_j))
    print(len(r_j))
