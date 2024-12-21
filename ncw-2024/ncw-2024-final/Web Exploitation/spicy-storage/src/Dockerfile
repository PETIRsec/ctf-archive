FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential xxd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN useradd -U -m -s /bin/bash ctf

COPY flag.txt /
RUN mv /flag.txt /flag-`xxd -u -l 10 -p /dev/urandom`
RUN echo 'export HISTSIZE=0' >> /etc/bash.bashrc && echo 'export HISTFILESIZE=0' >> /etc/bash.bashrc && echo 'unset HISTFILE' >> /etc/bash.bashrc

WORKDIR /app
COPY src/ /app/
RUN chown -R ctf:ctf /app

RUN pip install --no-cache-dir -r requirements.txt

USER ctf

CMD ["python", "/app/app_web.py"]
