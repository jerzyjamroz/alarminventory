#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


from .alarminventory import main

__name__ = "alarminventory"
__version__ = '0.0.1'
__author__ = 'Jerzy Jamroz'
__license__ = "GPL v2"
__summary__ = "Alarm inventory for EPICS alarm system"
