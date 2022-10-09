from mcstatus import JavaServer
import colorama
from random import shuffle
import sys
import signal

def log(phrase, online):
    path = "offline.txt"
    if online:
        path = "online.txt"
    with open(path, 'a') as fp:
        fp.write(phrase + '\n')

prepare = True
shuffle_it = True
if "--no-prepare" in sys.argv:
    prepare = False
if "--no-shuffle" in sys.argv:
    shuffle_it = False

def read_wordlist():
    with open("wordlist.txt") as fp:
        wordlist = fp.read().split('\n')
        return wordlist


words = read_wordlist()

if prepare:
    print(colorama.Fore.CYAN)
    print("Preparing...")
    i = 0
    while i < len(words):
        if "'" in words[i] or \
            '&' in words[i] or \
            '!' in words[i] or \
            '@' in words[i] or \
            '#' in words[i] or \
            '$' in words[i] or \
            '%' in words[i] or \
            '^' in words[i] or \
            '*' in words[i] or \
            '(' in words[i] or \
            ')' in words[i]:
            del words[i]
            i -= 1
        i += 1
    print("Prepared.")
    print("Wordlist length:", len(words))
    print()
    print(colorama.Fore.WHITE)

if shuffle_it:
    shuffle(words)

successful = 0
offline = 0
can_run = True
def sigint_handler(*args):
    global can_run
    can_run = False
signal.signal(signal.SIGINT, sigint_handler)

for q in words:
    if not can_run:
        print(colorama.Fore.CYAN, end='')
        print("Exiting...")
        break
    try:
        server = JavaServer.lookup(f"{ q }.aternos.me")
        status = server.status()
        if "This server is offline." not in status.description and "not found" not in status.description:
            log(f"{ q }.aternos.me", True)
            print(colorama.Fore.LIGHTGREEN_EX)
            print(f"#{ q } !FOUND! { status.description }")
            successful += 1
            print(colorama.Fore.WHITE)
        elif "offline" in status.description:
            log(f"{q}.aternos.me", False)
            print(f"#{q}. offline.")
            offline += 1
        else:
            print(f"#{q}. not found.")
    except:
        print(f"#{q}. error")

print(colorama.Fore.CYAN, end='')
print(f"Launched servers found: {successful}. Offline servers found: {offline}.")
print(colorama.Fore.WHITE)
