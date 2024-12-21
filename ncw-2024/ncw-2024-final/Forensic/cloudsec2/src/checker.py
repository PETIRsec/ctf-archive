import os

FLAG = os.getenv("FLAG", "flag{this_is_a_fake_flag}")

q1 = False
q2 = False
q3 = False
q4 = False
q5 = False
q6 = False
q7 = False
q8 = False
q9 = False
q10 = False

print("What is the Access Key ID of the leaked AWS credentials?")
print("Example input: AKIA1234567890AOKWKO")
if input("Your answer: ").strip() != "AKIA453N4QOMCFGUPBPV":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q1 = True

print("What is the invoke URL of the other API Gateway that exists?")
print("Example input: https://www.example.com")
if input("Your answer: ").strip() != "https://bp61amux7k.execute-api.ap-northeast-1.amazonaws.com/list":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q2 = True

print("How many Lambda functions were deployed in the AWS account?")
print("Example input: 100")
if int(input("Your answer: ")) != 4:
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q3 = True

print("What is the full URL of the compromised S3 bucket?")
print("Example input: https://www.example.com")
if input("Your answer: ").strip() not in ["https://wijenbank-tokyo.s3.ap-northeast-1.amazonaws.com/", "https://wijenbank-tokyo.s3.ap-northeast-1.amazonaws.com"]:
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q4 = True

print("What is the valid AWS Access Key ID that was exposed in the S3 bucket?")
print("Example input: AKIA1234567890AOKWKO")
if input("Your answer: ").strip() != "AKIA453N4QOMEIL32YW4":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q5 = True

print("What is the statement ID that allowed public access to the directory with the valid AWS Access Key ID?")
print("Example input: statementID")
if input("Your answer: ").strip() != "PublicReadGetObject":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q6 = True

print("What is the IP address of the DigitalOcean production server?")
print("Example input: 123.123.123.123")
if input("Your answer: ").strip() != "165.22.109.13":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q7 = True

print("What is the password of the account \"deploy\"?")
print("Example input: password123")
if input("Your answer: ").strip() != "deploy":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q8 = True

print("What is the MD5 hash of the file left by the attacker inside the app deployment directory on the DigitalOcean production server?")
print("Example input: q1w2e3r4t5y6q1w2e3r4t5y6q1w2e3r4")
if input("Your answer: ").strip() != "c8c7209c7a87f99a1d11a53854808f1f":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q9 = True

print("How many non-default environment keys were set on the DigitalOcean production server?")
print("Example input: 10")
if input("Your answer: ").strip() != "2":
    print("Incorrect")
    exit()
else:
    print("Correct\n")
    q10 = True

if q1 and q2 and q3 and q4 and q5 and q6 and q7 and q8 and q9 and q10:
    print("Congratulations! You have successfully completed the challenge.")
    print(FLAG)
    exit()
else:
    print("This is a rare error... Please contact the challenge author.")