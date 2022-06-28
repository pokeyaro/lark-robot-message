#/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
from configs.settings import PATH
sys.path.append(PATH.ROOT)

from configs.settings import SERVE
from src import create_app

app = create_app()
app.debug = True

if __name__ == '__main__':
    app.run(host=SERVE.CONN.HOST, port=SERVE.CONN.PORT)
