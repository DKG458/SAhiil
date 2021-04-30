#!/usr/bin/python

# coding=utf-8

# Originally Written By:Muhammad Hamza

# Source : Python2"

# Donot Recode It. 

#Import module

try:

    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests

    from multiprocessing.pool import ThreadPool

    from requests.exceptions import ConnectionError

    from mechanize import Browser

except ImportError:

    os.system('pip2 install requests')

    os.system('pip2 install mechanize')

    os.system('python2 jam.py')

#Browser Setting

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

	 def exit():

	print "[!] Exit"

	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def hamza(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.03)
