import os
import logging


cwd = os.getcwd()
folder = "logs"

fn = "logs.log"

if not os.path.exists(os.path.join(cwd, folder)):
    os.mkdir(os.path.join(cwd, folder))

dest = os.path.join(cwd, folder, fn)


logging.basicConfig(
    filename=dest,
    encoding="utf-8",
    level=logging.INFO,
    format="%(filename)s:%(module)s:%(funcName)s:%(lineno)d:%(levelname)s:%(message)s",
)
