import hashlib
import os
import sys
#from past.builtins import xrange

complete_list = []

def print_help():
    print("""\n\n
    --------------------------HashKiller By Nadav Ben Tzur--------------------------
    hashKiller.py [OPTION1][OPTION][...][FILENAME]
    OPTIONS:
    --help, -h                              DISPLAY THIS HELP INFORMATION
    --encrypt, -e                           ENCRYPT GIVEN STRING OR LINES IN FILENAME
    --decrypt, -d                           DECRYPT GIVEN STRING OR LINES IN FILENAME
    --type=[HASH_TYPE], -t=[HASH_TYPE]      SPECIFY HASH TYPE
    --limit=[LIMIT], -l=[LIMIT]             MAXIMUM HASHES TO TRY OUT OF FILE
    --FILENAME=[FILE_PATH]                  PATH AND NAME OF FILE WITH STRING TO ENCRYPT OR DECRYPT
    --list=[LIST_TYPE]                      CHARSET OF ENCRYPTED STRING: a - lowercase
                                                                         A - uppercase
                                                                         d - digits
                                                                         s - special charechters{"'{}()?!@#$%^&*;:/.,[]}\n\n
    --length=[LENGTH]                       MAX LENGTH OF DECRYPTED STRING
    """)
#--string=[STRING], -s=[STRING]          STRING TO ENCRYPT OR DECRYPT

    exit(1)


"""def getargs():
    global your_list
    your_list = ""
    global hash_type
    hash_type = ""
    global encrypt
    encrypt = False
    global FILENAME
    FILENAME = ""
    global max_len
    max_len = 5
    global complete_list
    complete_list = []
    if '--help' in sys.argv or '-h' in sys.argv:
        print_help()

    for arg in sys.argv:
        if "--type=" == arg[:7]:
            hash_type = arg[7:]

    for arg in sys.argv:
        if "-t=" == arg[:3]:
            hash_type = arg[3:]

    for arg in sys.argv:
        if "--length=" == arg[:9]:
            max_len = arg[9:]


    for arg in sys.argv:
        if "--encrypt" == arg:
            encrypt = True

    for arg in sys.argv:
        if "-e" == arg:
            encrypt = True

    for arg in sys.argv:
        if "--decrypt" == arg:
            encrypt = False

    for arg in sys.argv:
        if "-d" == arg:
            encrypt = False

    for arg in sys.argv:
        if "--list=" == arg[:7]:
            if 'a' in arg[7:]:
                your_list += "abcdefghijklmnopqrstuvwxyz"
            if 'A' in arg[7:]:
                your_list += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if 'd' in arg[7:]:
                your_list += "1234567890"
            if 's' in arg[7:]:
                your_list += "'{}()?!@#$%^&*;:/.,[]"


    if "--list=" not in sys.argv:
        your_list = "abcdefghijklmnopqrstuvwxyz1234567890"

    for arg in sys.argv:
        if "--FILENAME=" == arg[:11]:
            FILENAME = arg[11:]
    with open(FILENAME) as f:
        global strings
        strings = f.readlines()

    for i in range(len(strings)-1):
        strings[i] = strings[i].strip("\n")

    for current in xrange(max_len):
        a = [i for i in your_list]
        for y in xrange(current):
            a = [x+i for i in your_list for x in a]
        complete_list = complete_list + a
"""
def md4(strings, max_len):
    global complete_list
    flag = 0
    for count in range(len(strings)):
        for i in complete_list:
            sys.stdout.write("[+]Trying: " + i +"\t")
            print(str(hashlib.new('md4', i.encode('utf-8')).hexdigest()))
            if str(hashlib.new('md4', i.encode('utf-8')).hexdigest()) == strings[count]:
                print("PASSWORD FOUND(MD4): " + i + "Number of tries: " + count)
                command = "echo FOUND--------------------------------"
                os.system("echo PASSWORD FOUND : " + i + ">> tries.txt")
                input("-------------------------------\n\n\n\n\n\n\n\n\n\n\n\n")
                flag += 1
    return flag


def md5(strings, max_len):
    global complete_list
    flag = 0
    for count in range(len(strings)):
        for i in complete_list:
            sys.stdout.write("[+]Trying: " + i +"\t")
            print(str(hashlib.new('md5', i.encode('utf-8')).hexdigest()))
            if str(hashlib.new('md5', i.encode('utf-8')).hexdigest()) == strings[count]:
                print("PASSWORD FOUND(MD5): " + i)
                command = "echo FOUND--------------------------------"
                os.system("echo PASSWORD FOUND : " + i + ">> tries.txt")
                input("-------------------------------\n\n\n\n\n\n\n\n\n\n\n\n")
                flag +=1
    return flag



def sha1(strings, max_len):
    global complete_list
    flag = 0
    for count in range(len(strings)):
        for i in complete_list:
            sys.stdout.write("[+]Trying: " + i +"\t")
            print(str(hashlib.new('sha1', i.encode('utf-8')).hexdigest()))
            if str(hashlib.new('sha1', i.encode('utf-8')).hexdigest()) == strings[count]:
                print("PASSWORD FOUND(SHA1): " + i)
                command = "echo FOUND--------------------------------"
                os.system("echo PASSWORD FOUND : " + i + ">> tries.txt")
                input("-------------------------------\n\n\n\n\n\n\n\n\n\n\n\n")
                flag +=1
    return flag


def main():
    global complete_list
#getargs()
    hash_type = "md5"
    max_len = 5
    your_list = "abcdefghijklmnopqrstuvwxyz1234567890"
    print("[-]Opening file test.txt")
    with open("test.txt", 'r') as f:
        print("[-]Generating list")
        strings = [i.replace("\n", "") for i in f.readlines()[:-1]]
        for current in range(max_len):
            a = [i for i in your_list]
            for y in range(current):
                a = [x + i for i in your_list for x in a]
                print("[-]----")
            complete_list = complete_list + a
            print(f"[-]Iteration {current}")
        print("[-]List Complete")
        print(f"[-]Decrypting {strings} with {hash_type}")
        if hash_type == "md5":
            input("press enter to continue (" + str(len(complete_list)) + " passwords to try)...")
            if not md5(strings, max_len)==len(strings):
                y = input("unspecified or abscent hash type. try all options?(y/n)")
                if (y == 'y' or y == 'Y'):
                    md4(strings, max_len)
                    sha1(strings, max_len)
        elif hash_type == "md4":
            input("press enter to continue (" + str(len(complete_list)) + " passwords to try)...")
            if not md4(strings, max_len)==len(strings):
                y = input("unspecified or abscent hash type. try all options?(y/n)")
                if (y == 'y' or y == 'Y'):
                    md5(strings, max_len)
                    sha1(strings, max_len)
        elif hash_type == "sha1":
            input("press enter to continue (" + str(len(complete_list)) + " passwords to try)...")
            if not sha1(strings, max_len)==len(strings):
                y = input("unspecified or abscent hash type. try all options?(y/n)")
                if (y == 'y' or y == 'Y'):
                    md4(strings, max_len)
                    md5(strings, max_len)




if __name__ == '__main__':
    main()
