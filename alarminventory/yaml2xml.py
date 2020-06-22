#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import oyaml
import xmltodict
from genericlibs import *


def _load_inv(suffix="_pvd."):
    _yaml = {}
    for fi in LS:
        if suffix in fi:
            with open(INV_DIR + '/' + fi) as infile:
                ids_tmp = oyaml.load(infile, Loader=oyaml.FullLoader)
                _yaml = {**_yaml, **ids_tmp}
    return _yaml


def _check_dev(prefix, pvarg):
    _yaml = DEV_YAML
    for devi in _yaml:
        if devi in prefix:
            if pvarg in _yaml[devi]:
                return True
    return False


def _add_pvd(prefix=""):
    __list = []
    __pvd_yaml = PVD_YAML
    for devi in __pvd_yaml:
        if devi in prefix:
            for pvdi in __pvd_yaml[devi]:
                if _check_dev(prefix, pvdi):
                    __pvd_yaml[devi][pvdi].update({"@name": pfx_put_sep(prefix) + pvdi})
                    __list.append(__pvd_yaml[devi][pvdi])

    return __list


def _make_as_sys(as_str):
    _list = []
    _tmp_list = []
    for dsi in INV_YAML[as_str]:
        _tmp_list = _add_pvd(pfx_put_sep(as_str)+dsi)
        force_append_list(_list, _tmp_list)
        _tmp_list.clear()
    return _list


def _make_component(sys_list):
    _dict = {"component": sys_list}
    return _dict


def _add_as_pv(as_str, as_list):
    _dict = {"@name": as_str, "pv": as_list}
    return _dict


def _add_root(body):
    _tree = INV_FILE.split("-")
    _root_dict = body.copy()
    for node in reversed(_tree):
        _root_dict = {'component': {"@name": node, "component": _root_dict["component"]} }
        #_root_dict = {'component': {"@name": node, _root_dict.copy()}}

    _root_dict["config"] = _root_dict.pop("component")
    return _root_dict


def main(in_yl, out_xl):
    # INIT
    logging.info(f"{__file__=}")
    global INV_DIR, LS, INV_FILE
    global INV_YAML, PVD_YAML, DEV_YAML
    INV_DIR = os.path.dirname(in_yl)
    INV_FILE = os.path.basename(in_yl).replace(".yaml", "")
    LS = os.listdir(INV_DIR)
    PVD_YAML = _load_inv("_pvd.")
    DEV_YAML = _load_inv("_dev.")

    with open(in_yl) as infile:
        INV_YAML = oyaml.load(infile, Loader=oyaml.FullLoader)

    logging.info(f"{INV_DIR=}")
    logging.info(f"{LS=}")
    logging.info(f"{INV_FILE=}")
    logging.info(f"{INV_YAML=}")
    logging.info(f"{PVD_YAML=}")
    logging.info(f"{DEV_YAML=}")

    # BODY
    _sys_list_tmp = []
    for asi in INV_YAML:
        _onesys_list_tmp = _make_as_sys(asi)
        _onesys_header_list_tmp = [_add_as_pv(asi, _onesys_list_tmp)]
        _sys_list_tmp = _sys_list_tmp + _onesys_header_list_tmp

    _comp_sys_dict = _make_component(_sys_list_tmp)
    _out_dict = _add_root(_comp_sys_dict)

    with open(out_xl, 'w') as outfile:
        outfile.write(xmltodict.unparse(_out_dict, encoding='utf-8', pretty=True))

    logging.info(_out_dict)


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

