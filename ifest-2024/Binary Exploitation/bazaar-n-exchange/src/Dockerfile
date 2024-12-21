FROM debian:latest

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m -s /bin/bash ctf

COPY ./xinetd.conf /etc/xinetd.conf 
RUN chmod 644 /etc/xinetd.conf

COPY ./startchall.sh /usr/bin/startchall 
COPY ./xinetd /etc/xinetd.d/xinetd 

COPY ./chall /home/ctf 
COPY ./chall.c /home/ctf 
COPY ./flag.txt /home/ctf/flag.txt 
COPY ./run.sh /home/ctf/run 

RUN chown -R root:ctf /home/ctf && chmod -R 550 /home/ctf 
RUN chown root:root /home/ctf/flag.txt && chmod 444 /home/ctf/flag.txt && chown root:root /home/ctf/chall.c && chmod 444 /home/ctf/chall.c
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

CMD ["/usr/bin/startchall"]