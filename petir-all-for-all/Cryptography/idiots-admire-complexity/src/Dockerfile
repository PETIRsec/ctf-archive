FROM debian:latest

RUN apt-get update && apt-get install -y xinetd python3 python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN pip install pycryptodome --break-system-packages
RUN pip install cypari==2.4.1 --break-system-packages

RUN useradd -U -m -s /bin/bash ctf

COPY ./xinetd.conf /etc/xinetd.conf
RUN chmod 644 /etc/xinetd.conf

COPY ./server.py /home/ctf/server.py
COPY ./run.sh /home/ctf/run
COPY ./flag.txt /home/ctf/flag.txt
COPY ./startchall.sh /usr/bin/startchall
COPY ./xinetd /etc/xinetd.d/xinetd

RUN chown -R root:ctf /home/ctf && chmod -R 550 /home/ctf
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

CMD ["/usr/bin/startchall"]
