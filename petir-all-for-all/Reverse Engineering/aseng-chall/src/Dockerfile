FROM ubuntu:latest

RUN apt-get update 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash peteer

WORKDIR /home/peteer

COPY ./flag.txt .
COPY ./chall .
COPY ./ynetd /usr/bin/ynetd

RUN chown -R root:peteer /home/peteer
RUN chmod -R 750 /home/peteer && chmod 440 flag.txt 
RUN chown root:peteer /usr/bin/ynetd
RUN chmod 750 /usr/bin/ynetd

EXPOSE 14821

CMD ["/usr/bin/ynetd", "-p", "14821", "/home/peteer/chall"]