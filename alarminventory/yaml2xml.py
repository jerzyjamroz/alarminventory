#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
import yaml
#import xml
import dicttoxml
import xmltodict
import xmlplain
import xml.etree.ElementTree as ET
# local functions
from genericlibs import *
# local runtime functions


def main(in_yl, out_xl):
    logging.info(__file__)

    with open(in_yl) as infile:
        input_yaml = yaml.load(infile)

    print(input_yaml)

    with open("in/example.xml") as infile:
        xml_dict = xmltodict.parse(infile.read())

    print(xml_dict)
    #output = xmlplain.obj_from_yaml(input_yaml)
    #output = input_yaml
    #output = xmlplain. (input_yaml)
    #print(output)
    #output_xml = dicttoxml(input_yaml, custom_root='test', attr_type=False)
    output_xml = dicttoxml.dicttoxml(xml_dict)
    output_xml_str = ET.tostring(output_xml, encoding='unicode', method='xml')
    print("-------------------------------------------------------")
    print(type(output_xml_str))
    print(output_xml_str)
    #with open(out_xl, 'w') as outfile:
    #    xmlplain.xml_from_obj(output, outfile, pretty=True)
        #xml.dump(output, outfile)

    #with open(out_xl, 'w') as outfile:
    #    outfile.write(str(output_xml))
    #    #xml.dump(output, outfile)
    with open(out_xl, 'w') as outfile:
        outfile.write(str(output_xml_str))

    logging.info(output_xml)


if __name__ == '__main__':
    main()

