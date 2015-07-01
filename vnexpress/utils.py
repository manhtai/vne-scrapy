import json
from pprint import pprint


def _read_json(fp='items.json'):
    with open(fp, 'rb') as f:
        return json.load(f)


def _print_n(js, n=2):
    for i in range(n):
        pprint(js[i])

_print_n(_read_json())



