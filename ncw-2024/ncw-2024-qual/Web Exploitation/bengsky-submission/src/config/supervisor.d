[supervisord]
nodaemon=true

[program:myapp]
command=node /app/app.js
autostart=true
autorestart=true
stdout_logfile=/dev/stdout
stderr_logfile=/dev/stderr
startretries=5
startsecs=5
