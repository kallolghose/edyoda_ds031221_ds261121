import json

def read_json(filename):
    data = {}
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    print(data['computerdetails'])
    

def write_json(filename):
    dictionary = {
        "name": "kallol",
        "experience": 7,
        "contacts": {
            "country_code" : "+91",
            "home": "8014389430",
            "work": "7387160644"
        },
        "address": [
            {
                "city": "Shillong"
            },
            {
                "city": "NOIDA"
            }
        ]
    }

    with open(filename, "w") as op:
        json.dump(dictionary, op)


read_json("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/json_data.json")
write_json("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/json_data_write.json")
