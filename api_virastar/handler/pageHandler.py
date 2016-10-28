# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Elf'

from base import WebBaseHandler
from api_virastar.model.db_model import *
import random
import json
class PageHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        self.render("main.html")

    def post(self, *args, **kwargs):
        email = self.get_argument("email", None)
        if email:
            check = email.find("@")
            if check != -1:
                try:
                    data = Users().select().where(Users.email==email).get()
                    self.result['message'] = "ایمیل شما قبلا استفاده شده"
                    self.write(json.dumps(self.result))

                except:
                    token = random.randint(10000000, 99999999)
                    try:
                        data = Users().create(email=email,token=token,status=0)
                        self.result['message'] = "توکن شما %d می باشد"  %token
                        self.write(json.dumps(self.result))
                    except:
                        self.result['message'] = self.result['message'] = "متاسفانه خطایی در سیستم وجود دارد."
                        self.write(json.dumps(self.result))
            else:
                self.result['message'] = "ایمیل شما معتبر نیست"
                self.write(json.dumps(self.result))

        else:
            print "error"
