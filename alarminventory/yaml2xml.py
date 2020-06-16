#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import oyaml
# import yamlordereddictloader
# import dicttoxml
import xmltodict


def main(in_yl, out_xl):
    logging.info(__file__)

    with open(in_yl) as infile:
        input_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    # print(input_yaml)

    with open("in/example.xml") as infile:
        xml_dict = xmltodict.parse(infile.read())

    # print(xml_dict)
    xml = dicttoxml.dicttoxml(xml_dict)
    print(xml)

    with open(out_xl, 'w') as outfile:
        outfile.write(xml.decode())

    # logging.info(output_xml)


def demo1_xml2xml():
    with open("../in/demo.xml") as infile:
        xml_dict = xmltodict.parse(infile.read())

    print(xml_dict)

    with open("../out/demo.xml", 'w') as outfile:
        outfile.write(xmltodict.unparse(xml_dict, encoding='utf-8', pretty=True))


def demo2_yaml2xml():
    with open("../in/example.yaml") as infile:
        input_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    with open("../out/demo.xml", 'w') as outfile:
        outfile.write(xmltodict.unparse(input_yaml, encoding='utf-8', pretty=True))


def demo3_xml2yaml():
    with open("../in/demo.xml") as infile:
        input_dict = xmltodict.parse(infile.read())

    #output_dict = json.loads(json.dumps(input_dict))
    #print(output_dict)

    with open("../out/demo.yaml", 'w') as outfile:
        yaml.dump(input_dict, outfile, default_flow_style=False, sort_keys=False)


def demo4_yaml2xml():
    with open("../in/demo.yaml") as infile:
        input_yaml = yaml.load(infile, Loader=yamlordereddictloader.Loader)

    with open("../out/demo.xml", 'w') as outfile:
        outfile.write(xmltodict.unparse(input_yaml, encoding='utf-8', pretty=True))


def demo5_yaml2xml_basic():
    with open("../in/demo.yaml") as infile:
        input_yaml = oyaml.load(infile, Loader=oyaml.FullLoader)

    with open("../out/demo.xml", 'w') as outfile:
        outfile.write(xmltodict.unparse(input_yaml, encoding='utf-8', pretty=True))


if __name__ == '__main__':
    # main()
    demo5_yaml2xml_basic()

