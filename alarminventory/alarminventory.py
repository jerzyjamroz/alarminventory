#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from genericlibs import *
from menu import *

# Local runtime modules
import yaml2xml


# =========================================


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # Assure py3
    assure_py3()

    # Get the cli params
    cli_params = menu()
    if cli_params.manual:
        print(open('README.md').read())

    # Interface
    interface = {"input": cli_params.input,
                 "output": cli_params.output,
                 "ids": cli_params.ids,
                 #"plot": cli_params.inventory.replace(".", "_plot."),
                 }


    # declare meta list to log the program progress
    logging.info("cli_params " + str(cli_params))
    logging.info("interface " + str(interface))
    #if cli_params.net:
    #    tnet.main(inventory_jl=interface["inventory"], network_jl=interface["network"], pvs_jl=interface["pvs"])
    yaml2xml.main(in_yl=interface["input"], out_xl=interface["output"], ids_yl=interface["ids"])


if __name__ == '__main__':
    main()
