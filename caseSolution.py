"""
File: caseSolution.py
Author: Mirjam Liodden
Date: 18.11.2023

"""

import json

with open('response.json', 'r') as f:                     
    data = json.loads(f.read())
    f.close()

class_data = data['results']

print(class_data)