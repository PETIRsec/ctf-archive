# ShopiToko

Answer:

1. 3
   Description: The log file reveals 3 HTTP status codes: 200 (OK), 403 (Forbidden), 404 (Not Found).

2. 190.253.15.120
   Description: The IP address 190.253.15.120 is the attacker. This address is linked to suspicious activities including probing for vulnerabilities and attempting to exploit known security weaknesses.

3. bargaintime.jsp
   Description: The logs spotted an attempt to create a file named "bargaintime.jsp". This JavaServer Pages (JSP) file is part of the attacker's exploit strategy. JSP files can be used to execute server-side code, making this a potentially serious security threat.

4. ClassLoader
   Description: The exploit attempt targets the Java ClassLoader. The ClassLoader is a critical component of the Java Runtime Environment, and its exploitation could lead to unauthorized code execution on the server.

5. discount_master
   Description: There's evidence of an attempt to create a user account named "discount_master" in line 63

6. 15/06/2024:02:24:45
   because it represents the timestamp of the first successful command execution by the attacker after exploiting the vulnerability. The server log shows that at this exact time, the IP address 190.253.15.120 (identified as the attacker's IP) made a GET request to "/bargaintime.jsp" with parameters "pwd=j" and "cmd=whoami". This request returned a 200 status code, indicating success. The "whoami" command is typically used as an initial probe after gaining unauthorized access, making this the first evidence of successful command execution post-exploitation. Therefore, this timestamp accurately answers the question about when the attacker first successfully executed a command after gaining access.

7. CVE-2022-22965
   Description: CVE-2022-22965 also known as spring4shell is a security flaw in the Spring Framework can allow attackers to execute remote code on the target system. The specific techniques used, including ClassLoader manipulation and JSP file creation, are big trademarks of Spring4Shell exploitation.
