import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()

parser.add_argument('--key', action="store", dest="key", default=None, type=str)
parser.add_argument('--val', action="store", dest="value", default=None, type=str)

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

json_string = None

if not os.path.exists(storage_path):
    with open(storage_path, "w") as f:
        f.write("")

with open(storage_path, 'r') as f:
    json_string = f.readline()

with open(storage_path, 'w') as f:
    if len(json_string) == 0:
        if args.value is None:
            pass
        else:
            notes = {args.key: [args.value, ]}
            json_string = json.dumps(notes)
            f.write(json_string)
    else:
        notes = json.loads(json_string)
        if args.value is None:
            if args.key in notes:
                for idx, el in enumerate(notes[args.key]):
                    if idx != len(notes[args.key]) - 1:
                        print(el, end=', ')
                    else:
                        print(el)
            else:
                print(None)
        else:
            if args.key in notes:
                notes[args.key].append(args.value)
            else:
                notes[args.key] = [args.value, ]
        json_string = json.dumps(notes)
        f.write(json_string)
