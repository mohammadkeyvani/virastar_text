#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Elf'

import os

class Config:
    def __init__(self):
        self.applications_root = os.path.join(os.path.dirname(__file__), "")
        self.web = {
            'port': 7474,
            'server_ip': '127.0.0.1',
        }