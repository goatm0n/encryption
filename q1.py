import encryption as enc
"""
I have created the tools for RSA encryption in the module encryption.py
The code does not neccessarilly have to run this way.
This script is to walk the user through the encryption process while demonstrating its capabilities.
"""

def main():
    ## PART 2 OF Q1
    print("--------PART 2 OF Q1---------")
    print("Enter a string for encrpytion: ")
    myString = input()
    asciiList = enc.convertStringToASCIIList(myString)
    print("Your string in ASCII decimal code: ")
    print(asciiList)
    print("---------END PART 2 OF Q1---------")
    ## END PART 2 OF Q1
    print("Enter 2 primes for public-private key generation: ")
    PRIME1 = int(input())
    PRIME2 = int(input())
    N = PRIME1 * PRIME2
    print("p = " + str(PRIME1) + "; q = " + str(PRIME2) + "; N = " + str(N) + ";")
    print("-------- List of e d pairs ----------")
    edPairList = enc.generateEdList(PRIME1, PRIME2)
    print(edPairList)
    print("Enter a pair of numbers from the list to generate your public and private key")
    e = int(input())
    d = int(input())
    publicKey, privateKey = enc.generateKeyPair(e, d, N)
    print("PublicKey: " + str(publicKey) + " PrivateKey: " + str(privateKey))
    print("Your string encrypted into an integer list corrresponding to ASCII its decimal code")
    intList = enc.encryptASCIIList(asciiList, publicKey)
    print(intList)    
    encryptedString = enc.convertASCIIListToString(intList)
    print("Your encrypted integer list converted back into a string by ascii decimal code")
    print(encryptedString)
    print("Writing encrypted integer list to file \"out.txt\"...")
    enc.writeIntegerListToTextFile(intList, "out.txt")
    print("Complete")
    print("Reading integer list from file \"out.txt\"...")
    encryptedIntList = enc.readTextFile("out.txt")
    print("Complete")
    print("Decrypting integer list to string...")
    decryptedString = enc.decryptIntegerListToString(encryptedIntList, privateKey)
    print("Complete")
    print("------Decrypted String-------")
    print(decryptedString)

    

if __name__ == "__main__":
    main()