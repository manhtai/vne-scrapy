import json
from pprint import pprint


def _read_json(fp='items.json'):
    with open(fp, 'rb') as f:  # Python2
        return json.load(f)


def _print_n(js, n=2):
    for i in range(n):
        pprint(js[i])

_print_n(_read_json())


create_vnexpress = """
create table vnexpress (guid varchar(32) not null primary key,
url varchar(160),
date varchar(160),
intro varchar(300),
title varchar(160),
content text,
comments text,
tags varchar(160),
updated date);
"""
