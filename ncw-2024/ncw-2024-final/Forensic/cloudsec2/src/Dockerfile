FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat python3 python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN useradd -U -m -s /bin/bash ctf
# RUN pip3 install pycryptodome --break-system-packages

COPY ./checker.py /home/ctf/questions.py
COPY ./run.sh /home/ctf/run

RUN chown -R root:ctf /home/ctf && chmod -R 550 /home/ctf

CMD socat TCP-L:23456,fork EXEC:"/home/ctf/run",reuseaddr,stderr