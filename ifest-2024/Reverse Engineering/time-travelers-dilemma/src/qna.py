def generator():
    questions = [
        f"1. What is the value of the variable 'rand' when 'i = 3'?",
        f"2. What is the value of the variable 'rand' when 'i = 2'?",
        f"3. What is the value of the variable 'rand' when 'i = 1'?",
    ]

    answers = [
        "524177213401",
        "972919039644",
        "809327279315"
    ]
    return questions, answers

def ask_questions(questions, answers):
    print('''
  ____ ____ ____            _                   _    ____                                         _      __        __    _       _     
 / ___/ ___/ __■■          | |    _____   _____| |  |  _ \ ___  __ _ _ __ ___  _■■■■■■■■■__  _ __( )___  \ \      / /_ _| |_ ___| |__  
 \__■■■___ \___ \   _____  | |   / _ \■■■/ / _ \ |  | |_) / ■■■/ _` | '__/ _ \/ __/ __|/ _ \| '__|// __|  \ \ /\ /■■■■■ | __/ __| '_ \ 
  ___) |__) |__) | |_■■__| | |__|  __/\ V /  __■■■  |  _ <  __/ (_| | | |  __/\__ \__ \ (_■■■■■    \__ \   \ V  V / (_| | || (__| | | |
 |____/___■■■■__/          |___■■■___| \_/ \___|_|  |_| \_\___|\__, |_|  ■■■■||___/___/\___/|_|    |___/    ■■/\_/ \__,_|\__\_■■■■■■|_|
                                                               |___/                                                                             
    ''')
    print("Welco■■ to the SSS-Le■■l Reg■■■sor's Wa■■■ interface.")
    print("We ■■■■ your help to fix ■■■ coordi■■tes of t■■ time travel so that ■■ can ret■rn safely")
    for i in range(len(questions)):
        print(questions[i])
        user_input = str(input("Your answer : ").strip())
        
        if user_input != answers[i]:
            print("Incorrect!")
            exit(0)
        else:
            if i == 0:
                print("That is c■■rect! X co■■dinates ■re set!")
            if i == 1:
                print("Th■t i■ correct! Y coord■nates are set!")
            if i == 2:
                print("Tha■ is co■rect! Z coo■■■nates a■■ s■t!")
    print("Congratulations! You've helped the Time Traveler go back to his own timeline safely.")
    print("Here's your reward : IFEST{wh04_h0w_d1d_y0u_b3c0m3_4_r3gr3ss0r}")
    exit(0)

if __name__ == "__main__":
    questions, answers = generator()
    ask_questions(questions, answers)