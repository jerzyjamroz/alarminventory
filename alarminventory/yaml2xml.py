#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
import yaml
import xml
# local functions
from genericlibs import *
# local runtime functions


def main(in_yl, out_xl):
    logging.info(__file__)
    # Get the script root location
    # root = __file__.replace(os.path.basename(__file__), "")
    # root = "."
    with open(in_yl) as infile:
        input_yf = yaml.load(infile)


#    with open(out_xl, 'w') as outfile:
#        xml.dump(tim_net_json, outfile)

    #logging.info(tim_net_json)


if __name__ == '__main__':
    main()

