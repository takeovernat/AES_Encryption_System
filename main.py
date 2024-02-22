
import sys
import numpy as np

def main():
    #inputfile = raw_input("Enter the name of the plaintext input file: ")
    #keyfile = raw_input("Enter the name of the input key file")
    #outputfile = raw_input("Enter the name of the output cyphertext file")
    
    try:
        f = open("input.txt", 'r')
        k = open("key.txt", 'r')
        o = open('output.txt', 'w')
    except:
        print("unable to open file, please try again")
        exit()
    
    contents = f.read()
    key = k.read()
    cContent = cleanupspaces(contents)
    clean = cleanuppunctuation(cContent)
    write("Preprocessing...", o, clean)
    fitKey = lengthKey(clean, key)
    Vig = VigSub(clean, fitKey)
    write("subtitution...", o , Vig)
    Pad(Vig)
    #PaddedString = Pad(Vig)
    #write("Padding...", o , PaddedString)


def cleanupspaces(contents):
    cont = contents.replace(" ", "")
    return cont
def cleanuppunctuation(contents):
    cleanContent = "".join(u for u in contents if u not in ("?", ".", ";", ":", "!"))
    return cleanContent

def write(message, o, con):
    print(message)
    print(con)
    o.write(message)
    o.write("\n")
    o.write(con)

def lengthKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def VigSub(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def Pad(string):   
    fobyfo = []
    if(len(string) % 16 != 0):
       #print(len(string))
        while(len(string) % 16 != 0):
            string += "A"

    x = [string[i:i+1] for i in range(0, len(string))]
    print(x)
    mat = np.array(x).reshape(4, 4).T
  


        
    #print(len(string))
    







if __name__ == "__main__":
    main()   
