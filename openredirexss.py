import requests
import argparse
from colorama import Fore
from pyfiglet import Figlet
import time
 
print(Fore.RED+(""))
f = Figlet(font='slant')
print(f.renderText('OpenRedireXSS'))
print("                                                      By INNOCENTx0")

parser = argparse.ArgumentParser(
                    prog='OpenRedireXSS.py',
                    description='Example: python openredirecxss.py -u http://example.com/HERE/signin --openredirect yes -w wordlist',
                    epilog='Read the README.md for other info')
                    

#Set mode for openredirect
parser.add_argument('-or','--openredirect')
parser.add_argument('-u', '--url')
parser.add_argument('-w','--wordlist')
args = parser.parse_args()

# Function to fuzz the endpoint

if args.openredirect == "no":
    print(Fore.YELLOW + "[!] Open redirect mode: NO")
if args.openredirect == "yes":
    print(Fore.YELLOW + "[!] Open redirect mode: YES")
time.sleep(1)



def openr_fuzzer():
    print(Fore.GREEN + "[!] Starting..")
    time.sleep(0.5)
    with open(args.wordlist) as wordlist:
        for line in wordlist:
            stripped = line.strip()
            #print (stripped) #for debug
            point = args.url.replace("HERE",stripped)
            generate_wordlist = (point)
            print(generate_wordlist)

def param_fuzz():
    print(Fore.GREEN + "[!] Starting..")
    time.sleep(0.5)
    with open(args.wordlist) as wordlist:
     for line in wordlist:
            stripped = line.strip()
            #print (stripped) #for debug
            generate_wordlist = (args.url + stripped)
            print(generate_wordlist)

if args.openredirect == "no":
    openr_fuzzer()
if args.openredirect == "yes":
    param_fuzz()

