# !/usr/bin/env python

from sanic import Sanic
from src.views import wechat_bp

app = Sanic(__name__)
app.blueprint(wechat_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, workers=1)
