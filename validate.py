#!/usr/bin/python

import json, sys, os

def main(args):
    data = json.loads(args)

    print_data(data)
    output_data(data)

    return validate(data)


def print_data(data):
    print(data)
    for k, v in data.items():
        print(type(k),k)
        print(type(v),v)

def output_data(data):
    with open("/tmp/dump.txt", "w") as f:
        for k, v in data.items():
            f.write("{}={}\n".format(k,v))

def validate(data):
    return 'id' in data


if __name__ == '__main__':
    args = sys.argv
    print(args)

    if len(args) == 0:
        sys.exit(9)

    ans = main(args[1])

    if ans:
        sys.exit(0)
    else:
        sys.exit(9)
