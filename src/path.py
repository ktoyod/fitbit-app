import os
from pathlib import Path


class MyPath(object):
    BASEPATH = os.environ['BASEPATH']
    RESULTSPATH = Path(BASEPATH).joinpath('results')
    HEARTPATH = Path(RESULTSPATH).joinpath('heart')
