import random

def NotPrime(r):
    for x in range(2, r):
        if (r % x == 0):
            return True
    return False

def GenP(p):

    while (NotPrime(p)):
        p = random.randrange(1, 65536)
    return p

def GenQ(q,p):

    while(NotPrime(q) or q == p):
        q=random.randrange(1, 65536)
    return q

def GenE(e,phi):

    while (e>phi or phi%e!=1 or NotPrime(e)):
        e = random.randrange(1, 99999)
    return e


def GenD(e,phi):
    a = []
    p = phi
    while e != 1:
        a.append(p//e)
        tmp = p
        p=e
        e=tmp%e

    x = 0
    y = 1
    for t in a:
        d= x-t*y
        x=y
        y= d

    if d < 0:
        return d+phi
    else:
        return d

def calbin(n):
    c = 0
    while (n > 0):
        c = c + 1
        n = n // 10
    return c

def EncDec(m, e, N):
    if(type(m) == str):     # Encryption
        spl = []
        cipher= []
        n = 3
        for x in range(0, len(m), n):        # Divide message into chunks
            spl.append(m[x: x + n])
        print("Message chunks", spl)
        hexo = []
        encode = []

        for txt in spl:
            s = txt.encode("utf-8").hex()  # string to hexadecimal
            hexo.append(s)
            an = int(s, 16)  # hexadeicmal to integer
            encode.append(an)



        for x1 in encode:
            bn = int("{0:b}".format(e)) # Encryption process
            digits = calbin(bn)
            tmp = bn
            sol = []
            s = 1
            i = 0
            ans = 1

            for x2 in range(digits):        # Square & Multiply
                sol.append(pow(x1, s, N))
                s = s * 2

            for x3 in range(digits):        # Square & Multiply
                dig = tmp % 10
                tmp = tmp // 10
                if (dig == 1):
                    c = sol[i]
                    ans = ans * c
                i = i + 1
            cipher.append(ans%N)
        return cipher

    else:
        decode = []         #Decryption
        for x1 in m:
            bn = int("{0:b}".format(e))  # Decryption
            digits = calbin(bn)
            tmp = bn
            sol = []
            s = 1
            i = 0
            ans = 1

            for x2 in range(digits):        # Square & Multiply
                sol.append(pow(x1, s, N))
                s = s * 2

            for x3 in range(digits):        # Square & Multiply
                dig = tmp % 10
                tmp = tmp // 10
                if (dig == 1):
                    c = sol[i]
                    ans = ans * c
                i = i + 1
            decode.append(ans % N)
        print(decode)

        hexo =[]
        m = []
        for txt in decode:
            s = hex(txt)[2:]  # integer to hexadecimal
            hexo.append(s)
            an = bytearray.fromhex(s).decode()  # hexadecimal to string
            m.append(an)
        print(m)
        message = "".join(m)
        return message


def SigVer(m, d, N):
    if (type(m) == str):        #Signature process
        spl = []
        signature = []
        n = 3
        for x in range(0, len(m), n):
            spl.append(m[x: x + n])
        print("Message to be signed chunks", spl)
        hexo = []
        encode = []

        for txt in spl:
            s = txt.encode("utf-8").hex()  # string to hexadecimal
            hexo.append(s)
            an = int(s, 16)  # hexadeicmal to integer
            encode.append(an)
        """print(integ)"""

        for x1 in encode:
            bn = int("{0:b}".format(d))  # Encryption process
            digits = calbin(bn)
            tmp = bn
            sol = []
            s = 1
            i = 0
            ans = 1

            for x2 in range(digits):  # Square & Multiply
                sol.append(pow(x1, s, N))
                s = s * 2

            for x3 in range(digits):  # Square & Multiply
                dig = tmp % 10
                tmp = tmp // 10
                if (dig == 1):
                    c = sol[i]
                    ans = ans * c
                i = i + 1
            signature.append(ans % N)
        return signature

    else:
        decode = []         #Verification process
        for x1 in m:
            bn = int("{0:b}".format(d))  # Decryption process
            digits = calbin(bn)
            tmp = bn
            sol = []
            s = 1
            i = 0
            ans = 1

            for x2 in range(digits):  # Square & Multiply
                sol.append(pow(x1, s, N))
                s = s * 2

            for x3 in range(digits):  # Square & Multiply
                dig = tmp % 10
                tmp = tmp // 10
                if (dig == 1):
                    c = sol[i]
                    ans = ans * c
                i = i + 1
            decode.append(ans % N)
        print(decode)

        hexo = []
        verify = []
        for txt in decode:
            s = hex(txt)[2:]  # integer to hexadecimal
            hexo.append(s)
            an = bytearray.fromhex(s).decode()  # hexadecimal to string
            verify.append(an)
        print(verify)
        message = "".join(verify)     # join message chucks into one message
        return message

def main():
    """
    p = GenP(random.randrange(1, 65536))
    q = GenQ(random.randrange(1, 65536),p)
    N = p*q
    phi = (p-1) * (q-1)
    e = GenE(random.randrange(1, 99999),phi)
    d = GenD(e,phi)
    print("p =",p," q =",q," N =",N," phi =",phi," e =",e," d =",d)

    """
    Message = 'What is your ID number?'
    print("Message = ",Message)
    Encryption = EncDec(Message, 62951, 1986745939)
    print("Ciphertext = ",Encryption)


    cipher = [357285600, 234235566, 338207882, 188315998, 277099956]
    print("Ciphertext = ",cipher)
    print("Message = ", EncDec(cipher, 397884067, 398056559))




    Text = "Youssef Masmoudi"
    print("Original = ", Text)
    Signature = SigVer(Text, 397884067, 398056559)
    print("Signature = ",Signature)


    Sign = [1031391050, 1414708550, 1320417579]
    print("Signed message = ", Sign)
    Signature = SigVer(Sign, 62951, 1986745939)
    print("Verify Signature = ", Signature)



if __name__ == "__main__":
    main()








