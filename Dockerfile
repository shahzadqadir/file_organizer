FROM python:3.13.15

RUN pip install termcolor

RUN apt update && \
    apt install -y vim && \
    apt install -y net-tools

RUN useradd -m -s /usr/bin/bash script

WORKDIR /home/script

USER script
