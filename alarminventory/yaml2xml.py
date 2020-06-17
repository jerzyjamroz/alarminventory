#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import oyaml
# import yamlordereddictloader
# import dicttoxml
import xmltodict


def _load_inv(suffix="_pvd."):
    _yaml = {}
    for fi in _ls:
        if suffix in fi:
            with open(_inv_dir + '/' + fi) as infile:
                ids_tmp = oyaml.load(infile, Loader=oyaml.FullLoader)
                _yaml = {**_yaml, **ids_tmp}
    return _yaml


def main(in_yl, out_xl):
    logging.info(__file__)
    global _inv_dir, _ls
    _inv_dir = os.path.dirname(in_yl)
    _ls = os.listdir(_inv_dir)

    with open(in_yl) as infile:
        _inv_yaml = oyaml.load(infile, Loader=oyaml.FullLoader)

    _pvd_yaml = _load_inv("_pvd.")
    _dev_yaml = _load_inv("_dev.")

    print(_pvd_yaml)

    #with open(out_xl, 'w') as outfile:
    #    outfile.write(xmltodict.unparse(_yaml, encoding='utf-8', pretty=True))

    #logging.info(_yaml)


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

