# Dockerfile
FROM python:3.9-slim

RUN groupadd -r ctfgroup && useradd -r -g ctfgroup ctf

WORKDIR /app

COPY . .

RUN chown -R ctf:ctfgroup /app

USER ctf

CMD ["python", "verify.py"]
