
# Leasons API + Formating weird HTML text
# https://www.w3schools.com/html/html_entities.asp
# https://www.freeformatter.com/html-escape.html


import  requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
