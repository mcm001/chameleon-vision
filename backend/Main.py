import tornado.ioloop
import logging
from app.ChameleonVisionApp import ChameleonApplication
from app.classes.SettingsManager import SettingsManager
from tornado.options import options
from app.handlers.VisionHandler import VisionHandler


def run_server():
    tornado.options.parse_command_line()
    app = ChameleonApplication()
    print(f"Serving on port {options.port}")
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    SettingsManager()

    VisionHandler().run()
    run_server()

    while True:
        pass
