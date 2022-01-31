#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

print(r"""\
        ╓░▒▒╦╗
        jÜ¢¢╩╩▒_               r▒▒Ü¢¢Ä¢ÄÄÄ▒╗╓r                     ╓░░▒▒Ä▒⌐
       j¢╩¢▒R╚ºªÜ▒mr╖╓╓.    ºΓ          º╚¢╩¢¢▒╗▒▒╓        ╓    ╖▒▒╝¢¢¢¢¢╩¢¢▒
      ºº╚ªº        j╚╩¢¢Ä=       ╖r▒▒▒▒▒▒m╓º¢╩¢╩¢¢¢¢¢¢▒▒▒Ü¢╩¢¢¢¢¢¢¢╝╩╩¢╩¢╩¢╩░
      ┌¢▒▒Ü░r▒▒▒»╓▒╝¢╩¢ª      ╓▒Ü╩¢¢¢╩¢¢¢¢¢¢▒╝¢╩¢╩¢╩¢╩¢¢¢╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢░r░═
      ¢╩¢¢╩¢¢¢¢¢¢¢¢╩╩╩▒      ▒Ü¢╩╩¢╩╩╩╩╩¢╩¢╩¢╝¢╩¢░º╝¢╩╩╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩╩╩¢╩¢╩╩¢¢▒R
        «╩¢╩¢╩¢╩╩╩¢╩¢▒      ▒Ö╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩╩Γ  ªºº ¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩¢╩╩╩¢╩¢▒
        º▒╝╩¢╩¢╩¢╩╩╩¢▒     ▐Ü╝¢╝¢╩╩╩¢╩¢╩¢╩╩╩¢ª╙º      ╔▒╝╩╩╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩¢╩¢¢▒
      º¬²ê╩╩¢╩¢╩¢╩¢╩¢░      ¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢¢▒▒▒¬     ²╩╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢░
        ª╝¢╩¢╩¢╩¢╩¢╩╩¢      j╝¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢¢¢Γ «Ä▒▒▒╝╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╝¢╓_
         «¢╩¢╩¢╩¢╩¢╩¢╩▒      º╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢░▒Ö¢¢¢¢¢╩╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩╩╩¢╩¢╩▒╝▒.
          j╝╩╩¢╩¢╩¢╩╩╩¢▒╖      º¢╩╩╩¢╩¢╩¢╩╩╚j▒╝╩¢Ä¢╝¢╝¢╩¢╩¢╩╩╩¢╩¢╩╩¢¢╩▒╚╙ºΓ
            │¢╚╝╩╩¢╩¢╩¢▒╝▒╗         ºººº  ╓▒╝¢╩╩╩╩¢╩¢╩¢▒╚▒╝╩╩╩╩=º
                 ╩¢╩╩╩¢¬    º!r╗╓   ╓╖r   ╙==  j╩  ╙º
                  ╙ºº └       └¢¢¢▒Ä=º        ¢╩ª
""")


def get_proxy(url):
    try:
        r = requests.get(url, timeout=30)  # seconds
        return r.content
    except:
        return None


def download_proxies(socks_type, out_file):
    try:
        with open(out_file, 'wb') as f:
            f.truncate()

            if socks_type == 'SOCKS4':
                try:
                    data = get_proxy('https://www.proxy-list.download/api/v1/get?type=socks4')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://www.proxyscan.io/download?type=socks4')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('http://pubproxy.com/api/proxy?limit=2&format=txt&http=true&type=socks4')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt')
                    if data:
                        f.write(data)
                except:
                    pass

            if socks_type == 'SOCKS5':
                try:
                    data = get_proxy('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://www.proxy-list.download/api/v1/get?type=socks5')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://www.proxyscan.io/download?type=socks5')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('http://pubproxy.com/api/proxy?limit=2&format=txt&http=true&type=socks5')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt')
                    if data:
                        f.write(data)
                except:
                    pass

            if socks_type == 'HTTP':
                try:
                    data = get_proxy('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://www.proxy-list.download/api/v1/get?type=http')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('http://pubproxy.com/api/proxy?limit=2&format=txt&http=true&type=http')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://www.proxyscan.io/download?type=http')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt')
                    if data:
                        f.write(data)
                except:
                    pass

            if socks_type == 'HTTPS':
                try:
                    data = get_proxy('https://www.proxyscan.io/download?type=https')
                    if data:
                        f.write(data)
                except:
                    pass
                try:
                    data = get_proxy('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt')
                    if data:
                        f.write(data)
                except:
                    pass

            f.close()
    except IOError:
        print('Failure')


def check_proxy(proxy, socks_type):
    proxy_split = proxy.strip().split(":")

    if len(proxy_split) != 2:
        proxy = proxy + ':8080'

    protocol = str(socks_type).lower()

    proxies = {
        'https': protocol + "://" + proxy,
        'http': protocol + "://" + proxy,
    }

    try:
        r = requests.get('https://www.wikipedia.org', proxies=proxies, timeout=5)
        if proxy_split[0] == r.headers['X-Client-IP']:
            return True
        return False
    except:
        return False


def check_list(socks_type, out_file):
    temp_list = []
    try:
        with open(out_file, 'r+') as rfile:
            temp = rfile.readlines()
            for i in temp:
                if i not in temp_list:  # check duplicate
                    if ':' in i:
                        proxy_split = i.strip().split(":")
                        if len(proxy_split) != 2:
                            continue
                        temp_list.append(i)
            rfile.truncate()
            rfile.close()

        with open(out_file, 'wb') as wfile:
            for proxy in list(temp_list):
                wfile.write(bytes(proxy, encoding='utf-8'))
            wfile.close()
    except IOError:
        print('Failure')

    return temp_list


def download(socks_type):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    files = base_dir + '/files'

    if not os.path.isdir(files):
        os.mkdir(files)
        os.chmod(files, 0o7777)

    out_file = files + '/' + str(socks_type).lower() + '.txt'

    download_proxies(socks_type, out_file)
    check_list(socks_type, out_file)


if __name__ == "__main__":
    download('HTTP')
    download('HTTPS')
    download('SOCKS4')
    download('SOCKS5')
