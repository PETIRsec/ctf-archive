from timedinput import timedinput

print("I was doing my work paper but then I got blue screen! How is it possible? I was just doing my work paper! I need to find out what happened.\n", flush=True)

def wrong(ans):
    if ans == "Tch":
        print("\nStill thinking, eh? Come back later ^^", flush=True)
    else:
        print("\nWrong answer! Come back once you get it right !!", flush=True)
    exit(1)

print("When was the dump captured? [mm/dd/yyyy]", flush=True)
ans = timedinput("> ", timeout=60, default="Tch")
if ans != "10/18/2009":
    wrong(ans)

print("\nWhat is the bug check code and its name? [0xcode:name]", flush=True)
ans = timedinput("> ", timeout=60, default="Tch")
if ans != "0xF4:CRITICAL_OBJECT_TERMINATION" and ans != "0xf4:CRITICAL_OBJECT_TERMINATION":
    wrong(ans)

print("\nWhat is the name of the terminated process?", flush=True)
ans = timedinput("> ", timeout=60, default="Tch")
if ans != "csrss.exe":
    wrong(ans)

print("\nWhat is the kernel version?", flush=True)
ans = timedinput("> ", timeout=60, default="Tch")
if ans != "6.0.6002.18005":
    wrong(ans)

print("\nWhat is the address of the exceptions handler function? [0xaddress]", flush=True)
ans = timedinput("> ", timeout=60, default="Tch")
if ans != "0xfffff80001e71ffc":
    wrong(ans)

flag = open("flag.txt", "r").read()
print("\nThanks, now I will report it to my IT support! Here is your flag:", flag, flush=True)
exit(0)
