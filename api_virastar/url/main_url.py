__author__ = 'Elf'
from api_virastar.handler.mainHandler import MainHandler
from api_virastar.handler.pageHandler import PageHandler

url_pattern = [
    ("/", MainHandler),
    ("/main",PageHandler)
]
