#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import oyaml
# import yamlordereddictloader
# import dicttoxml
import xmltodict
from genericlibs import *


def _load_inv(suffix="_pvd."):
    _yaml = {}
    for fi in _ls:
        if suffix in fi:
            with open(_inv_dir + '/' + fi) as infile:
                ids_tmp = oyaml.load(infile, Loader=oyaml.FullLoader)
                _yaml = {**_yaml, **ids_tmp}
    return _yaml


def _check_dev(prefix, pvarg):
    _yaml = _dev_yaml
    for devi in _yaml:
        if devi in prefix:
            if pvarg in _yaml[devi]:
                return True
    return False


def _add_pvd(prefix=""):
    _list = []
    _yaml = _pvd_yaml
    for pvdi in _yaml:
        if _check_dev(prefix, pvdi):
            _yaml[pvdi].update({"@name": pfx_put_sep(prefix) + pvdi})
            _list.append(_yaml[pvdi])
    return _list


def main(in_yl, out_xl):
    logging.info(__file__)
    global _inv_dir, _ls
    global _inv_yaml, _pvd_yaml, _dev_yaml, _out_list
    _inv_dir = os.path.dirname(in_yl)
    _ls = os.listdir(_inv_dir)

    with open(in_yl) as infile:
        _inv_yaml = oyaml.load(infile, Loader=oyaml.FullLoader)

    _pvd_yaml = _load_inv("_pvd.")
    _dev_yaml = _load_inv("_dev.")

    print(_inv_yaml)
    print(_dev_yaml)
    print(_pvd_yaml)

    _out_list = {}
    for invi in _inv_yaml:
        _out_list = _add_pvd(invi)

    print(_out_list)
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

