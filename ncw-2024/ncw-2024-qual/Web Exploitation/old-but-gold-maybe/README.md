Simple XXE Injection but with 2 steps:
1. Need to do SSRF with XXE Injection to internal network and bypass the login by doing boolean SQL injection
2. The server will return a secret, use it to get the flag by doing another SSRF with XXE Injection