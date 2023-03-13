from FourPart.Four_Part import FourPart
import json
import sys


def fourpartresponse():

    request_data = json.loads(sys.argv[1])
    soprano = request_data.get('soprano')
    key = request_data.get('key')
    canto = []
    for note in soprano:
        canto.append((note['note'], note['octave']))

    chorale = FourPart(canto=canto, key=key)

    response = {
        "soprano": request_data.get('soprano'),
        "alto": [],
        "tenor": [],
        "bass": [],
        "chords": [],
        "key": key,
    }
    for note in range(len(canto)):
        response["alto"].append({"note": chorale.alto[note][0], "octave": chorale.alto[note][1]})
        response["tenor"].append({"note": chorale.tenor[note][0], "octave": chorale.tenor[note][1]})
        response["bass"].append({"note": chorale.bass[note][0], "octave": chorale.bass[note][1]})
        response["chords"].append(chorale.chords[note])


    print(json.dumps(response))

    sys.stdout.flush()

if __name__ == "__main__":
    fourpartresponse()