#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genericlibs import *
import argparse


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("-i", "--inventory", action='store', default="in/example.yaml", help="Read the PV inventory")
    parser.add_argument("-o", "--output", action='store', default="out/example.xml", help="Return the alarms for the EPICS BEAST")
    parser.add_argument("-m", "--manual", action='store_true', help="Print the application manual")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print(args)
    #return {"net": args.net, "plot": args.plot, "dev": args.dev, "manual": args.manual, "check": args.check}
    return args


if __name__ == '__main__':
    args = menu()
    print(args)
    print(args.check)
