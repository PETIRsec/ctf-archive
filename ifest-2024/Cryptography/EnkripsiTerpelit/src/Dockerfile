FROM ubuntu:22.04
env DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing && apt install libseccomp-dev xinetd python3 python3-pip -y
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN pip install pycrypto pycryptodome
env TERM=linux
env TERMINFO=/etc/terminfo
WORKDIR /home/ctf

COPY serper.py .
COPY flag.txt .

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service enkripsiterpelit\n\ 
{\n\ 
    disable = no\n\ 
    socket_type = stream\n\ 
    protocol = tcp\n\ 
    wait = no\n\ 
    user = ctf\n\ 
    type = UNLISTED\n\ 
    port = 1043\n\ 
    bind = 0.0.0.0\n\ 
    server = /home/ctf/run\n\ 
}' > /etc/xinetd.d/ctf

RUN echo '#!/bin/bash\ncd /home/ctf && python3 serper.py' > /home/ctf/run
RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 550 /home/ctf/serper.py /home/ctf/flag.txt /home/ctf/run /etc/init.sh

RUN chown -R root:ctf /home/ctf
RUN service xinetd restart
