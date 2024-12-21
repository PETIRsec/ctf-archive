# Base image
FROM node:20

# Create app directory
WORKDIR /app/

# Install app dependencies
COPY app/ .
# COPY app/package*.json ./
RUN npm install
# RUN npm install express

# Install webpack globally
RUN npm install -g webpack@5.92.0 webpack-cli

# Run webpack build
RUN webpack

# Install pupetter
RUN apt-get update \
    && apt-get install -y wget supervisor gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable libxss1 libxshmfence-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


COPY config/supervisor.d /etc/supervisor/conf.d/supervisord.conf
COPY config/restart.sh /restart.sh
RUN chmod +x /restart.sh


COPY flag.txt /flag.txt
RUN chown root:root /flag.txt
RUN chmod 700 /flag.txt

RUN cp /flag.txt /beluga-is-here-with-the-flag.txt

# Expose the port and start the app
EXPOSE 3000
# CMD [ "node", "./app.js" ]
CMD ["/bin/bash", "-c", "/restart.sh & /usr/bin/supervisord"]
