# input char; return ascii value

def convertCharToASCII(character):
    ASCII = ord(character)
    return ASCII


#define function to convert string to list of ASCII numbers
def convertStringToASCIIList(string):
    ASCIIlist = [] #builds empty list 
    for char in string: #runs through every character in input string
        ASCII = convertCharToASCII(char) 
        ASCIIlist.append(ASCII) #adds to list encoded letter of string input
    return ASCIIlist #returns list of ASCII numbers

# input ascii list; return encrypted ascii list, public exponent, modulus
def encryptASCIIList(asciiList, publicKey):
    e = publicKey[0]
    n = publicKey[1]
    print(e,n)
    encryptedList = [] 
    for num in asciiList:
        encryptedNum = (num**e) % n
        encryptedList.append(encryptedNum)
    return encryptedList

# input string; return encrypted integer list
# public key is integer
def encryptStringToIntegerList(string, publicKey):
    asciiList = convertStringToASCIIList(string)
    encryptedIntegerList = encryptASCIIList(asciiList, publicKey[0], publicKey[1])
    return encryptedIntegerList

def decryptIntegerListToASCIIList(integerList, privateKey, n):
    asciiList = []
    for num in integerList:
        decryptedNum = (num**privateKey) % n
        asciiList.append(decryptedNum)
    return asciiList

def convertASCIIListToString(asciiList):
    myString = ""
    for num in asciiList:
        myString += chr(int(num)) # converts floating point number from list to integer then to character then adds to string
    return myString        
    
# input encrpyted integer list; return decrypted string
def decryptIntegerListToString(integerList, privateKey, n):
    asciiList = decryptIntegerListToASCIIList(integerList, privateKey, n)
    decryptedString = convertASCIIListToString(asciiList)
    return decryptedString
    
# read integer values from text file with new line to seperate values
def readTextFile(path):
    numList = []
    file = open(path, "r")
    for line in file:
        cleanLine = line.rstrip() # removes newline character
        num = int(cleanLine) # casts to integer type
        numList.append(num) # adds to list
    file.close()
    return numList

def writeIntegerListToTextFile(intList, path):
    outFile = open(path, "w")
    for item in intList:
        outFile.write(str(item) + "\n")
    outFile.close()

def extendedEuclidian(a, b):
    # return g, x, y such that a*x + b*y = g = gcd(a, b) = 1
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extendedEuclidian(b % a, a)
        return g, y - (b // a) * x, x

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p



def isCoprime(p, q):
    # return true if coprime, false otherwise
    return gcd(p, q) == 1

def returnLargestMagnitude(a, b):
    if abs(a) > abs(b):
        return a
    else:
        return b

def isPrime(num):
    #primes are greather than 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                continue
        return True
    else:
        return False

def generateEdList(p, q):
    ## choose e * d mod phi = 1
    N = p * q
    # euler totient
    phi = (p-1) * (q-1)

    #e = 2
    eList = [x for x in range(phi)]
    #generate list of e's that are coPrime with phi and N
    
    
    ## not sure about this but think its ok; potentially unintended side effects in what values are being selected
    for e in eList:
        if not(isCoprime(e, N) and isCoprime(e, phi)):
            eList.remove(e)

    e_dPairList = []
   
    for e in eList:
        g, k, d = extendedEuclidian(phi, e)
        d = returnLargestMagnitude(k, d)
        if d < 0:
            d += phi
        e_dPair = [e, d]
        e_dPairList.append(e_dPair)

    cleanedEdList = []

    for pair in e_dPairList:
        if isPrime(pair[0]):
            cleanedEdList.append(pair)
        
    return cleanedEdList

def generateKeyPair(e, d, N):
    publicKey = [e, N]
    privateKey = [d, N]
    return publicKey, privateKey




