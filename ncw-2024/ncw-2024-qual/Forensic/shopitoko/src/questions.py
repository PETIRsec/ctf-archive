import signal
import threading
import time

correct_answers = {
    "Q1": "3",
    "Q2": "190.253.15.120",
    "Q3": "bargaintime.jsp",
    "Q4": "ClassLoader",
    "Q5": "discount_master",
    "Q6": "15/06/2024:02:24:45",
    "Q7": "CVE-2022-22965",
}


user_answers = {
    "Q1": "",
    "Q2": "",
    "Q3": "",
    "Q4": "",
    "Q5": "",
    "Q6": "",
    "Q7": ""
}



class TimeoutException(Exception):
    pass

def input_with_timeout(prompt, timeout=45):
    def input_thread(prompt, result):
        result.append(input(prompt).strip())

    result = []
    thread = threading.Thread(target=input_thread, args=(prompt, result))
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if not result:
        print("\nTime's up!")
        exit()
    return result[0]




def check_all_correct():

    return all(user_answers.values())  

while not check_all_correct():
    
    if user_answers["Q1"] == "":
        q1_answer = input_with_timeout("1. How many different HTTP status codes appear in the log? (answer format: 0): ").strip()
        if q1_answer.lower() == correct_answers["Q1"].lower():
            print("Correct!")
            user_answers["Q1"] = q1_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q2"] == "":
        q2_answer = input_with_timeout("2. What is the attacker's IP address? (answer format: 000.000.000.000): ").strip()
        if q2_answer.lower() == correct_answers["Q2"].lower():
            print("Correct!")
            user_answers["Q2"] = q2_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q3"] == "":
        q3_answer = input_with_timeout("3. what is the name of the file created by the attacker's exploit attempt? (answer format: filename.ext): ").strip()
        if q3_answer.lower() == correct_answers["Q3"].lower():
            print("Correct!")
            user_answers["Q3"] = q3_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q4"] == "":
        q4_answer = input_with_timeout("4. What is the name of the Java class used in the exploit attempt? (answer format: ClassName): ").strip()
        if q4_answer.lower() == correct_answers["Q4"].lower():
            print("Correct!")
            user_answers["Q4"] = q4_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q5"] == "":
        q5_answer = input_with_timeout("5. What is the name of the user account that the attacker attempted to create? (answer format: username): ").strip()
        if q5_answer.lower() == correct_answers["Q5"].lower():
            print("Correct!")
            user_answers["Q5"] = q5_answer
        else:
            print("Incorrect. Try again.")
            exit()
    
    if user_answers["Q6"] == "":
        q6_answer = input_with_timeout("6. What is the exact timestamp (in UTC) of the first successful command execution by the attacker after gaining access through the vulnerability? (answer format: DD/MM/YYYY:HH:MM:SS): ").strip()
        if q6_answer.lower() == correct_answers["Q6"].lower():
            print("Correct!")
            user_answers["Q6"] = q6_answer
        else:
            print("Incorrect. Try again.")
            exit()

    if user_answers["Q7"] == "":
        q7_answer = input_with_timeout("7. What is the CVE number for the vulnerability exploited in this attack? (answer format: CVE-YYYY-NNNNN): ").strip()
        if q7_answer.lower() == correct_answers["Q7"].lower():
            print("Correct!")
            user_answers["Q7"] = q7_answer
        else:
            print("Incorrect. Try again.")
            exit()

print("bravo heres the flag, Enjoy!!!!!!!!:: NCW{n1ce_3yes_y0u_got_th3re_d1d_the_chall_made_your_eyes_spring}")
