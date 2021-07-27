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

stuff = open("data_log.json", "r")
stufflist = []
for x in stuff.readlines():
    x = flatten_json(json.loads(x))
    row = []
    for key, value in x.items():
        row.append(str(value))
    stufflist.append(row)

df = pd.DataFrame(stufflist)
df.to_csv('myfile.csv')
