FROM ubuntu:24.04

RUN apt-get update 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get update && apt-get install -y python3

RUN useradd -U -m -s /bin/sh veight

RUN echo "NCW{603f1e4f172d5a4305e649aea9425636}" > /flag.txt
RUN chmod 400 /flag.txt
RUN chown root:root /flag.txt
COPY readflag /
RUN chmod +s /readflag

WORKDIR /home/veight

COPY chall.py .
COPY d8 .
COPY snapshot_blob.bin . 
COPY ./ynetd /usr/bin/ynetd

RUN chown root:veight /usr/bin/ynetd
RUN chmod 750 /usr/bin/ynetd

RUN chown -R root:veight /home/veight
RUN chmod -R 750 /home/veight

EXPOSE 11101

CMD ["/usr/bin/ynetd", "-u","veight", "-p", "11101", "/home/veight/chall.py"]
