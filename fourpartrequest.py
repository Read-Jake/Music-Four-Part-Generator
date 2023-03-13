import requests
import os
import json
import pickle

def requestfourpart(data, host = os.environ.get("LOCALHOST"), port="8080"):

    data = json.dumps(data)
    request = requests.post(f'http://{host}:8080', data=data)
    response = json.loads(request.text)

    return response


if __name__ == "__main__":
    soprano = [
        {"note": "C", "octave": 4},
        {"note": "D", "octave": 4},
        {"note": "E", "octave": 4},
        {"note": "D", "octave": 4},
        {"note": "C", "octave": 4}
    ]
    key = "C major"

    data = {
        "soprano": soprano,
        "key": key
    }

    chorale = requestfourpart(data)
    print(chorale)