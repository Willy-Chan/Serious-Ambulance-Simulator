import json
import pandas as pd


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

stuff = open("data_log_willy.json", "r")
stufflist = []
for y,x in enumerate(stuff.readlines()):
    x = json.loads(x)
    x = flatten_json(x)
    row = []
    keys = []
    for key, value in x.items():
        if y == 0:
            keys.append(str(key))
        row.append(str(value))
    if keys:
        stufflist.append(keys)
    stufflist.append(row)

df = pd.DataFrame(stufflist)
df.to_csv('data_log_willy.csv')
