FROM python:3.8-slim

RUN sed -i s/deb.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && apt update && \
    apt install --no-install-recommends  gcc libpq-dev libkrb5-dev -y && rm -rf /var/lib/apt/lists/*

WORKDIR /guoquan-apocalypse-app
COPY ./requirements.txt /guoquan-apocalypse-app/requirements.txt
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    cat requirements.txt | xargs -n 1 -L 1 pip install --no-cache-dir
# 代码放在镜像内
COPY . /guoquan-apocalypse-app
# 代码放在镜像外
VOLUME ["/guoquan-apocalypse-app"]

CMD [ "python", "-u", "main.py" ]
