# This is Cursor Era No VSCode

## Description

I'm new to web development, but I managed to build this revolutionary AI chatbot using Cursor IDE!
I think it's already super secure, Right?

## Solve

1. Exploit logic error untuk menjadi admin

    - GET `/api/auth/register?username=admin%0a&password=bebas` ambil `sessionKey` dari response
    - GET `/api/auth/login?username=admin&sessionKey=<sessionKey>`

2. Race Condition di `/api/add-balance` untuk menghilangkan `is_trust_issue` di `/api/remove-trust-issue`

3. Soceng dikit buat dapetin flag di `/api/chat`
