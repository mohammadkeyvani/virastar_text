# -*- coding: utf-8 -*-
# !/usr/bin/env python
from __future__ import unicode_literals

__author__ = 'Elf'

from base import WebBaseHandler
from hazm import *
import datetime
from api_virastar.model.db_model import *


class MainHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        self.write("success")
        pass

    def post(self, *args, **kwargs):
        token = self.get_argument("token", None)
        data = self.get_argument("data", None)
        if data == None or token == None:
            self.result['message'] = "لطفا پارامتر ها را درست ارسال کنید"
            self.result['status'] = 500
            self.result['value'] = ""
            self.write(self.result)
        else:
            try:
                user_ = Users().select().where(Users.token == token).get()
                date_now = datetime.datetime.now().date()
                if user_.date == date_now:
                    if user_.status == 20:
                        self.result['message'] = "درخواست های شما بیشتر از حد معمول است"
                        self.result['status'] = 500
                        self.write(self.result)
                    else:
                        normalizer = Normalizer()
                        data = normalizer.normalize(data)
                        count = user_.status + 1
                        Users.update(status=int(count)).where(Users.id == user_.id).execute()
                        self.result['message'] = "ok"
                        self.result['status'] = 200
                        self.result['value'] = data
                        self.write(self.result)

                else:
                    normalizer = Normalizer()
                    data = normalizer.normalize(data)
                    Users.update(status=1,date=date_now).where(Users.id == user_.id).execute()
                    self.result['message'] = "ok"
                    self.result['status'] = 200
                    self.result['value'] = data
                    self.write(self.result)

            except Exception as e:
                print(e)
                self.result['message'] = "توکن معتبر نیست"
                self.result['status'] = 500
                self.result['value'] = ""
                self.write(self.result)
