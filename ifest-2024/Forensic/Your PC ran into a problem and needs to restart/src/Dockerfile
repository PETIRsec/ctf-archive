FROM ubuntu:22.04
env DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing && apt install libseccomp-dev xinetd python3 python3-pip -y
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN pip install timedinput
env TERM=linux
env TERMINFO=/etc/terminfo
WORKDIR /home/ctf

COPY main.py .
COPY flag.txt .

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service bsod\n\ 
{\n\ 
    disable = no\n\ 
    socket_type = stream\n\ 
    protocol = tcp\n\ 
    wait = no\n\ 
    user = ctf\n\ 
    type = UNLISTED\n\ 
    port = 11511\n\ 
    bind = 0.0.0.0\n\ 
    server = /home/ctf/run\n\ 
}' > /etc/xinetd.d/ctf

RUN echo '#!/bin/bash\ncd /home/ctf && python3 main.py' > /home/ctf/run
RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 550 /home/ctf/main.py /home/ctf/run /etc/init.sh

RUN chown -R root:ctf /home/ctf
RUN service xinetd restart