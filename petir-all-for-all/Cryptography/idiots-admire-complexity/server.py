# CREDIT https://github.com/kamsec/SIDH/tree/main
# i dont want to spoil it but the title is very relevant to the challenge so please give this challenge a try
import os
import random
from hashlib import sha256
from json import loads, dumps
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

try:
    import cypari
    pari = cypari.pari
except ModuleNotFoundError:
    import cypari2
    pari = cypari2.Pari()

class Params:
    def __init__(self, l_A, e_A, l_B, e_B, f, p, Fp2_gen, EC, P_A, Q_A, P_B, Q_B):
        self.l_A, self.e_A = l_A, e_A
        self.l_B, self.e_B = l_B, e_B
        self.f = f
        self.p = p  # self.l_A ** self.e_A * self.l_B ** self.e_B * self.f - 1
        self.Fp2_gen = Fp2_gen
        self.EC = EC
        # Points P_A and Q_A which generate E[l_A ^ e_A]
        self.P_A = P_A
        self.Q_A = Q_A
        # Points P_B and Q_B which generate E[l_B ^ e_B]
        self.P_B = P_B
        self.Q_B = Q_B

    def print_params(self):
        print("-------------------------------------------------------------------")
        print("--------------------- PUBLIC PARAMETERS SETUP ---------------------")
        print(f'l_A = {self.l_A}, e_A = {self.e_A}')
        print(f'l_B = {self.l_B}, e_B = {self.e_B}')
        print(f'p = {self.p}')
        print(f'EC: y^2 = x^3 + {str(self.EC[3])} * x + {str(self.EC[4])}')  # [3] and [4] are short Weierstrass a and b
        print('Public EC j-invariant:', self.EC.j())
        print(f'P_A: {self.P_A}')
        print(f'Q_A: {self.Q_A}')
        print(f'P_B: {self.P_B}')
        print(f'Q_B: {self.Q_B}')

def choose_params(name):
    if name == "small":
        l_A, e_A = 2, 4  # 2 ^ 4 = 16
        l_B, e_B = 3, 3  # 3 ^ 3 = 27
        f = 1
        p = 431  # l_A ** e_A * l_B ** e_B * f - 1
        irr_poly = pari(f"Mod(1, {p})*x^2 + Mod(1, {p})")  # instead of ffinit()
        Fp2_gen = pari(f"ffgen({irr_poly}, 'i)")  # instead of Fp2 we use generator of Fp2
        x = Fp2_gen  # x is generator of Fp2
        EC = pari.ellinit([1, 0], x)
        P_A = [111 + 311 * x, 247 + 162 * x]  # points are initialized with x as i (so here [111 + 311*i, 247 + 162*i])
        Q_A = [290 + 176 * x, 29 + 421 * x]
        P_B = [360 + 112 * x, 287 + 146 * x]
        Q_B = [347 + 404 * x, 68 + 176 * x]
    elif name == "medium":
        l_A, e_A = 2, 18  # 2 ^ 18 = 262144
        l_B, e_B = 3, 13  # 3 ^ 13 = 1594323
        f = 1
        p = 417942208511  # l_A ** e_A * l_B ** e_B * f - 1
        irr_poly = pari(f"Mod(1, {p})*x^2 + Mod(1, {p})")  # instead of ffinit()
        Fp2_gen = pari(f"ffgen({irr_poly}, 'i)")  # instead of Fp2 we use generator of Fp2
        x = Fp2_gen
        EC = pari.ellinit([1, 0], x)
        P_A = [87274892954 + 7030669172 * x, 336685454335 + 270079778903 * x]
        Q_A = [171667875835 + 147460659556 * x, 324400676567 + 66966031470 * x]
        P_B = [415490311461 + 256577897080 * x, 29207284535 + 2477354271 * x]
        Q_B = [38161532236 + 43503164885 * x, 375022212868 + 317098013729 * x]
    elif name == "SIKEp434":
        l_A, e_A = 2, 216  # 2 ^ 216 = 105312291668557186697918027683670432318895095400549111254310977536
        l_B, e_B = 3, 137  # 3 ^ 137 = 232066203043628532565045340531182604896544238770765380550355483363
        f = 1
        p = 24439423661345221551909145011457493619085780243761596511325807336205221239331976725970216671828618445898719026692884939342314733567
        irr_poly = pari(f"Mod(1, {p})*x^2 + Mod(1, {p})")  # instead of ffinit()
        Fp2_gen = pari(f"ffgen({irr_poly}, 'i)")  # instead of Fp2 we use generator of Fp2
        x = Fp2_gen
        EC = pari.ellinit([1, 0], x)
        P_A = [
            15937686683633039019196728742331738441209610167832388917703407269928835422226362845467776102646239486823941673658245515771001898283 +
            2003351496878340769927496857888485805825600511617562327658105361759369326590776207465430298367135830995863247764468049749472449827 * x,
            17108323619081055472406376613720773413736121124406182472541249873821398922393300545360934897611851130699945176056842470104358654884 +
            8337004641788845819131721857290673922295053839933467431582336072726065745705096801632409264717689480409378684646781531582640287399 * x]
        Q_A = [
            15088817061064820268855215031798808081934414602474420517091065419503164076185078899700761543847379884983212295919804932006246031947 +
            7804220673805821185818875507282627517813183801913071739476129171353898518782055651068417838573748671068461643818212154265625205666 * x,
            3248126327355632307449398910863440627630497001071650448251192432379165836841686224302872841534443206199579057873167957417639551029 +
            19507679526450799728438014183641858310821309240412911974764102921372927929916615211429302545241275283904311830918752312996285161807 * x]
        P_B = [
            556274038285849315241897557477215211505102505036877971385691866860361859320408873381354575789101651011570316507766991773952557997 +
            16306656024954733221075162754955969260730457357369697629788710022165816786748701612472655217816963254297818152946097129242450733644 * x,
            14837889202738555922760869822639160650458519841159771977016139817337716263517812064882918694469258377690642456437323127075249813131 +
            3614789590927682028814871604873208458500877330458658745597461397001311907390924812620749562716470922547140320752451448882603082824 * x]
        Q_B = [
            3847144497801108225028716818622358634049600547745572272841246235914612333824083439220341539519730256837264684681979401578390546981 +
            8224904841129032115973432646497290185163264395865958574314664346285559445962868006749870180240521074454182724558887407546736075058 * x,
            5070201965208378562575304366332945278081481321657317607555997081531054662815938554843891620583341723452310835208486872845165579560 +
            5917717394456628336842002186881500641795694051979049336189885252227184440851721545191446902294118704165036223586306979148424339996 * x]
    return Params(l_A, e_A, l_B, e_B, f, p, Fp2_gen, EC, P_A, Q_A, P_B, Q_B)


# algorithm from https://crypto.stackexchange.com/questions/58375/how-to-get-an-optimal-strategy-in-computing-isogenies-for-sidh-sike # noqa
# n is amount of steps (exponent e_A or e_B), p is the cost of multiplication, q is the cost of isogeny
def generate_strategy(n, p, q):
    S = {1: []}
    C = {1: 0}
    for i in range(2, n+2):
        b, cost = min(((b, C[i-b] + C[b] + b*p + (i-b)*q) for b in range(1, i)), key=lambda t: t[1])
        S[i] = [b] + S[i-b] + S[b]
        C[i] = cost
    return S[n+1]

def validate_strategy(strat):  # it will raise exception if strategy is invalid, will return None if is valid
    t = len(strat) + 1
    if t == 1:
        return
    n = strat[0]
    if (n < 1) or (n >= t):
        raise Exception("Invalid strategy")
    L = strat[1:t-n]
    R = strat[t-n:]
    validate_strategy(L)
    validate_strategy(R)

# algorithm from SIDH specification https://sike.org/files/SIDH-spec.pdf p.14
def exec_strategy(EC, base_l, S, points, strat, stage, x):
    t = len(strat) + 1
    if t == 1:
        [F, f] = pari.ellisogeny(EC, S)
        EC = pari.ellinit(F, x)
        return EC, [pari.ellisogenyapply(f, point) for point in points]
    n = strat[0]
    L = strat[1:t-n]
    R = strat[t-n:]

    scalar = pow(base_l, n)  # instead of params.l_A ** n
    T = pari.ellmul(EC, S, scalar)
    EC, points = exec_strategy(EC, base_l, T, [S, *points], L, stage, x)
    EC, points = exec_strategy(EC, base_l, points[0], points[1:], R, stage, x)
    return EC, points

def isogeny_walk(degree, S, params, stage, EC_from_PK=None, print_all=False):
    # degree 2 reserved for Alice, 3 - for Bob - used for detecttion whose is turn
    # S is a starting point of Alice or Bob. At stage 2 needs to be computed on new curve
    # stage = 1 - public key generation, stage = 2 - secret computation
    x = params.Fp2_gen

    if stage == 1:
        EC = params.EC
    elif stage == 2:
        EC = EC_from_PK
    else:
        raise Exception("Stage must be 1 or 2")

    if degree == 2:  # Alice
        e = params.e_A
        P = params.P_B
        Q = params.Q_B
    elif degree == 3:  # Bob
        e = params.e_B
        P = params.P_A
        Q = params.Q_A
    else:
        raise Exception("Degree (l_A or l_B) has to be equal 2 (Alice) or 3 (Bob)")

    strategy = [degree ** (e - i - 1) for i in range(0, e)]
    for i, scalar in enumerate(strategy):
        # e.g.
        # l_A^e_A = 2^4 order 16 -> scalar = 2 -> R order = 8 (kernel of an isogeny) -> isogeny of degree 2
        # l_B^e_B = 3^3 order 27 -> scalar = 3 -> R order = 9 (kernel of an isogeny) -> isogeny of degree 3
        if print_all is True:
            print(f"--------------------------------------------")
            print(f"------------------ step {i} ------------------")
            print("scalar:", scalar)
            print(f"S: {S}, order: {pari.ellorder(EC, S)}")
        R = pari.ellmul(EC, S, scalar)
        [F, f] = pari.ellisogeny(EC, R)
        EC = pari.ellinit(F, x)
        S = pari.ellisogenyapply(f, S)
        if stage == 1:
            P = pari.ellisogenyapply(f, P)
            Q = pari.ellisogenyapply(f, Q)

        if print_all is True:
            print(f"R: {R}, order: {pari.ellorder(EC, R)}")
            print(f'f (isogeny with R as kernel):', f)
            print(f"f(S): {S}, order: {pari.ellorder(EC, S)}")
            if stage == 1:
                print(f"f(P): {P}, order: {pari.ellorder(EC, P)}")
                print(f"f(Q): {Q}, order: {pari.ellorder(EC, Q)}")
            print("j-invariant:", EC.j())
    if stage == 1:
        PK = [EC, [P, Q]]
        return PK
    elif stage == 2:
        SK = EC
        return SK
    
def encrypt_message(message, shared_key):
    key = sha256(str(shared_key).encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), 16))
    return iv + ciphertext

def decrypt_message(ciphertext, shared_key):
    key = sha256(str(shared_key).encode()).digest()
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), 16)
    return plaintext.decode()

def encode_public_key(EC, list_of_points, params_name, side):
    EC_a = str(EC[3])  # 3rd EC coefficient in cypari is "a" coefficient of short Weierstrass
    EC_b = str(EC[4])  # 4th EC coefficient in cypari is "b" coefficient of short Weierstrass
    P_x = str(list_of_points[0][0])
    P_y = str(list_of_points[0][1])
    Q_x = str(list_of_points[1][0])
    Q_y = str(list_of_points[1][1])
    packet = {
        "protocol": {
            "name": "SIDH",
            "params": params_name,
            "side": side},
        "payload": {
            "EC_a": EC_a,
            'EC_b': EC_b,
            'P_x': P_x,
            'P_y': P_y,
            'Q_x': Q_x,
            'Q_y': Q_y},
    }
    return dumps(packet)

def decode_public_key(packet):
    data = loads(packet)
    params = choose_params(data['protocol']['params'])
    p = params.p
    irr_poly = pari(f"Mod(1, {p})*x^2 + Mod(1, {p})")  # instead of ffinit()
    Fp2_gen = pari(f"ffgen({irr_poly}, 'i)")  # instead of defining Fp2 we just use the generator of Fp2
    x = Fp2_gen

    # need to reinitialize field elements from string
    for key, value in data['payload'].items():
        if value[0] == 'i':
            if len(value) == 1:  # case1:  i
                data['payload'][key] = 1 * x
            elif len(value) > 1:  # case2: i + 12
                record = value.split(' + ')
                data['payload'][key] = 1 * x + int(record[1])
        elif value[-1] == 'i':  # case3:  3*i
            record = value.split('*')
            data['payload'][key] = int(record[0]) * x
        else:
            record = value.split('*i + ')
            if len(record) == 1:  # case4: 81
                data['payload'][key] = int(record[0])
            elif len(record) == 2:  # case5: 3*i + 15
                data['payload'][key] = int(record[0]) * x + int(record[1])

    EC = pari.ellinit([data['payload']['EC_a'], data['payload']['EC_b']], x)
    P = [data['payload']['P_x'], data['payload']['P_y']]
    Q = [data['payload']['Q_x'], data['payload']['Q_y']]
    return [EC, [P, Q]]



base_3_strat_SIDHp434 = [71, 34, 17, 8, 4, 2, 1, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 9, 4, 2, 1, 1, 2, 1, 1, 5, 2, 1, 1, 3,
                         1, 2, 1, 17, 9, 4, 2, 1, 1, 2, 1, 1, 5, 2, 1, 1, 3, 1, 2, 1, 9, 4, 2, 1, 1, 2, 1, 1, 5, 2, 1,
                         1, 3, 1, 2, 1, 38, 17, 8, 4, 2, 1, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 9, 4, 2, 1, 1, 2, 1, 1, 5,
                         2, 1, 1, 3, 1, 2, 1, 21, 9, 4, 2, 1, 1, 2, 1, 1, 5, 2, 1, 1, 3, 1, 2, 1, 12, 5, 2, 1, 1, 3, 1,
                         2, 1, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1, 1]
base_2_strat_SIDHp434 = [111, 58, 27, 12, 5, 2, 1, 1, 3, 1, 2, 1, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1, 1, 15, 7, 3, 1, 2, 1, 4,
                         2, 1, 2, 1, 1, 8, 4, 2, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 31, 15, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1,
                         1, 8, 4, 2, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 16, 8, 4, 2, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 8,
                         4, 2, 1, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 58, 27, 14, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1, 1, 7, 4, 2,
                         1, 2, 1, 1, 4, 2, 1, 2, 1, 1, 15, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1, 1, 8, 4, 2, 1, 2, 1, 1, 4, 2,
                         1, 1, 2, 1, 1, 31, 15, 7, 3, 1, 2, 1, 4, 2, 1, 2, 1, 1, 8, 4, 2, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1,
                         1, 16, 8, 4, 2, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 8, 4, 2, 1, 1, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1]

params = choose_params("SIKEp434")

print("We are currently eavesdropping on the communication between Alice and Bob.")

k_A = random.randint(1, pow(2, 216))
k_AxQ_A = pari.ellmul(params.EC, params.Q_A, k_A)
S_A = pari.elladd(params.EC, params.P_A, k_AxQ_A)

strategy = base_2_strat_SIDHp434  # using precomputed strategy
PK_A = exec_strategy(params.EC, params.l_A, S_A, [params.P_B, params.Q_B], strategy, stage=1, x=params.Fp2_gen)
encoded_PK_A = encode_public_key(PK_A[0], PK_A[1], "SIKEp434", 'ALICE')
print("Alice:", encoded_PK_A)

k_B = random.randint(1, pow(3, 137))

k_BxQ_B = pari.ellmul(params.EC, params.Q_B, k_B)
S_B = pari.elladd(params.EC, params.P_B, k_BxQ_B)

strategy = base_3_strat_SIDHp434
PK_B = exec_strategy(params.EC, params.l_B, S_B, [params.P_A, params.Q_A], strategy, stage=1, x=params.Fp2_gen)
encoded_PK_B = encode_public_key(PK_B[0], PK_B[1], "SIKEp434", 'BOB')
print("Bob:",encoded_PK_B)
print()
PK_B = decode_public_key(encoded_PK_B)
EC_from_PK_B = PK_B[0]

k_AxQ_A = pari.ellmul(EC_from_PK_B, PK_B[1][1], k_A)
S_A = pari.elladd(EC_from_PK_B, PK_B[1][0], k_AxQ_A)

strategy = base_2_strat_SIDHp434
SK_A = exec_strategy(EC_from_PK_B, params.l_A, S_A, [], strategy, stage=2, x=params.Fp2_gen)[0]
SK_A = str(SK_A.j())

PK_A = decode_public_key(encoded_PK_A)
EC_from_PK_A = PK_A[0]

k_BxQ_B = pari.ellmul(EC_from_PK_A, PK_A[1][1], k_B)
S_B = pari.elladd(EC_from_PK_A, PK_A[1][0], k_BxQ_B)

strategy = base_3_strat_SIDHp434
SK_B = exec_strategy(EC_from_PK_A, params.l_B, S_B, [], strategy, stage=2, x=params.Fp2_gen)[0]
SK_B = str(SK_B.j())

print("Alice:", encrypt_message("Hello Bob, how are you?", SK_A).hex())
print("Bob:", encrypt_message("Hi Alice, I'm fine, thank you!", SK_B).hex())
print("Alice:", encrypt_message(open("flag.txt").read(), SK_A).hex())
print("Bob:", encrypt_message("Got it, thankfully we are safe and no one else can decrypt the message thanks to SIDH!", SK_B).hex())

print("Connection ended")
print()
print("Alice connected to you:", encoded_PK_A)
encoded_PK_C = input("Send her some parameters:")
PK_C = decode_public_key(encoded_PK_C)
EC_from_PK_C = PK_C[0]

kxQ = pari.ellmul(EC_from_PK_C, PK_C[1][1], k_A)
S = pari.elladd(EC_from_PK_C, PK_C[1][0], kxQ)

strategy = base_2_strat_SIDHp434
SK = exec_strategy(EC_from_PK_C, params.l_A, S, [], strategy, stage=2, x=params.Fp2_gen)[0]
SK = str(SK.j())
print("Your Shared Secret:", SK)
print("Alice:", encrypt_message("Skibidi dop dop dop yes yes", SK).hex())
enc = bytes.fromhex(input("Send her your encrypted message:"))
try:
    dec = decrypt_message(enc, SK)
    print("Alice:", encrypt_message("W rizz", SK).hex())
except:
    print("Alice:", encrypt_message("Ermm... Watta sigma", SK).hex())