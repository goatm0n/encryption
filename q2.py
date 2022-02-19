import encryption as enc

def main():
    """
    We need to decrypt an integer list of RSA encrypted numbers 
    given public key (e=307, N=165073).
    
    """
    # path to rsa file
    path = "RSA-encrypted-3.txt"
    #public key [e=307, N=165073]
    publicKey = [307, 165073]
    decryptedString = enc.decryptFileGivenPublicKey(path, publicKey)
    print(decryptedString)

    

if __name__ == "__main__":
    main()