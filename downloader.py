#!/usr/bin/python
'''
DownLoad source code
'''
import sys
from subprocess import Popen,PIPE
from multiprocessing.dummy import Pool as ThreadPool


def communicate(commandLine):
    #print('Executing command:%s...' % commandLine)
    process = Popen(commandLine, stdout=PIPE, stderr=PIPE, shell=True)
    return process.communicate()

def download(command):
    communicate(command)
    print "Done ",command.split('/')[-1]

def init_chrome():
    baseCommand = 'wget -P chrome https://chromium.googlesource.com/chromium/src.git/+archive/%s.tar.gz'
    versionsFile = "./versions/chrome.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % version
        commands.append(command)
    return commands

def init_linux_kernel():
    baseCommand = 'wget -P linux_kernel https://www.kernel.org/pub/linux/kernel/v%s/linux-%s.tar.xz'
    versionsFile = "./versions/linux_kernel.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        if version[0] == "4":
            command = baseCommand % ("4.x",version)
        else:
            command = baseCommand % (version[:3],version)
        commands.append(command)
    return commands 

def init_firefox():
    baseCommand = 'wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/%s/source/firefox-%s.source.tar.bz2'
    versionsFile = "./versions/firefox.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        if version.split(".")[0] >= "1":
            if version[:3] == "1.0" or version[:3] == "2.0" or version[:3] == "3.0":
                baseCommand1 = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/%s/source/firefox-%s-source.tar.bz2"
            if version[-4:] == "real":
                command = baseCommand1 % (version,version.split("-")[0])
            else:
                command = baseCommand1 % (version,version) 
        elif version[:3] == "0.9":
            command = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/%s/firefox-%s-source.tar.bz2" % (version,version)
        elif version == "0.10" or version == "0.10.1":
            command = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/0.10/firefox-1.0PR-source.tar.bz2"
        elif version == "0.10rc":
            command = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/0.10rc/firefox-1.0PRrc-i686-linux-gtk2%2Bxft.tar.gz"
        elif version == "0.8":
            command = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/0.8/firefox-source-0.8.tar.bz2"
        else:
            break;
        commands.append(command)
    return commands

def init_seamonkey():
    baseCommand = 'wget -P seamonkey http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%s/source/seamonkey-%s.source.tar.bz2'
    versionsFile = "./versions/seamonkey.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        if version.split(".")[0] == "1":
            command = "wget -P seamonkey http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%s/seamonkey-%s.source.tar.bz2" % (version,version)
        elif version.split(".")[1][:2] == "38" or version.split(".")[1][:2] == "39":
            command = "wget -P seamonkey http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%s/source/seamonkey-%s.source.tar.xz" % (version,version)
        else:
            command = "wget -P seamonkey http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%s/source/seamonkey-%s.source.tar.bz2" % (version,version)
        commands.append(command)
    return commands      

def init_thunderbird():
    versionsFile = "./versions/thunderbird.txt"
    commands = []
    for version in open(versionsFile):
        version = version.strip()
        if version.split(".")[0] == "0":
            if version == "0.1":
                command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/0.1/thunderbird-0.1-i686-pc-linux-gtk2-gnu.tar.bz2"
            elif version == "0.2" or version == "0.3" or version == "0.4":
                command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/%s/thunderbird-source-%s.tar.bz2" % (version,version)
            elif version == "0.5":
                command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/0.5/thunderbird-0.5-i686-pc-linux-gtk2-gnu.tar.bz2"
            elif version == "0.7rc":
                command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/0.7rc/thunderbird-0.7rc-i686-linux-gtk2%2Bxft.tar.gz"
            else:
                command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/%s/thunderbird-%s-source.tar.bz2" % (version,version)
        elif version[:2] == "1." or version[:3] == "2.0":
            command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/%s/source/thunderbird-%s-source.tar.bz2" % (version,version)
        elif version[-4:] == "real":
            command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/%s/source/thunderbird-%s.source.tar.bz2" % (version,version.split("-")[0])
        else:
            command = "wget -P thunderbird http://ftp.mozilla.org/pub/thunderbird/releases/%s/source/thunderbird-%s.source.tar.bz2" % (version,version)
        commands.append(command)
    return commands

def init_wireshark():
    baseCommand = 'wget -P wireshark https://www.wireshark.org/download/src/all-versions/wireshark-%s.tar.bz2'
    versionsFile = "./versions/wireshark.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % version
        commands.append(command)
    return commands

def init_webkit():
    baseCommand = "svn checkout https://svn.webkit.org/repository/webkit/releases/WebKitGTK/webkit-%s/ ./webkit/webkit-%s/"
    versionsFile = "./versions/webkit.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % (version,version)
        commands.append(command)
    return commands
    
def init_ffmpeg():
    baseCommand = "wget -P ffmpeg http://ffmpeg.org/releases/ffmpeg-%s.tar.bz2"
    versionsFile = "./versions/ffmpeg.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % version
        commands.append(command)
    return commands

def init_httpd():
    baseCommand = "wget -P  httpd http://archive.apache.org/dist/httpd/apache_%s.tar.gz"
    baseCommand1 = "wget -P  httpd http://archive.apache.org/dist/httpd/httpd-%s.tar.gz"
    versionsFile = "./versions/httpd.txt"
    commands = [] 
    for version in open(versionsFile):
        version = version.strip()
	if version.split(".")[0] == "1":
            command = baseCommand % version
        else:
            command = baseCommand1 % version
        commands.append(command)
    return commands
def init_xen():
    baseCommand = 'wget -P xen http://bits.xensource.com/oss-xen/release/%s/xen-%s.tar.gz'
    versionsFile = './versions/xen.txt'
    commands = []
    for version in open(versionsFile):
        version = version.strip()
        if version == "3.0.4" :
            command = 'wget -P xen http://bits.xensource.com/oss-xen/release/3.0.4-1/src.tgz/xen-3.0.4_1-src.tgz'
        elif version == "3.0.3" :
            command = 'wget -P xen http://bits.xensource.com/oss-xen/release/3.0.3-0/src.tgz/xen-3.0.3_0-src.tgz'
        elif version == '3.0.2':
            command = 'wget -P xen http://bits.xensource.com/Xen/latest/xen-3.0.2-src.tgz'
        else:
            command = baseCommand % (version,version)
        commands.append(command)
    return commands
def init_openssl():
    baseCommand0 = 'wget -P openssl ftp://ftp.openssl.org/source/openssl-%s.tar.gz'
    baseCommand1 = 'wget -P openssl ftp://ftp.openssl.org/source/old/0.9.x/openssl-%s.tar.gz'
    baseCommand2 = 'wget -P openssl ftp://ftp.openssl.org/source/old/1.0.0/openssl-%s.tar.gz'
    baseCommand3 = 'wget -P openssl ftp://ftp.openssl.org/source/old/1.0.1/openssl-%s.tar.gz'
    baseCommand4 = 'wget -P openssl ftp://ftp.openssl.org/source/old/1.0.2/openssl-%s.tar.gz'
    baseCommand5 = 'wget -P openssl ftp://ftp.openssl.org/source/old/fips/openssl-%s.tar.gz'
    versionsFile = './versions/openssl.txt'
    commands = []
    baseCommand = baseCommand1
    for version in open(versionsFile):
        version = version.strip()
        if version[:3] == 'KEY':
            baseCommand = eval('baseCommand' + version.split(".")[-1])
            continue
        commands.append(baseCommand % version)
    return commands
def init_mozilla():
    commands = []
    versionsFile = './versions/mozilla.txt'
    list0 = ['m10','m11','m12','m13','m15','m16','m17','m18']
    list1 = ['m4','m5','m6']
    list2 = ['m7','m8','m9']
    list3 = ['1.8a5','1.8a6','1.8b1']
    list4 = ['1.0.1rc2','1.0.1rc1','1.4rc1','1.4rc2','1.4rc3','1.5rc1','1.5rc2','1.7rc1','1.7rc3']

    for version in open(versionsFile):
        version = version.strip()
        if version in list0:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/%s/src/mozilla-source-%s.tar.gz' % (version,'M'+version[1:])
        elif version in list1:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/%s/TGZ/mozilla-5.0-%s.tar.gz' % (version,'M'+version[1:])
        elif version in list2:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/%s/TGZ/mozilla-source-%s.tar.gz' % (version,'M'+version[1:])
        elif version in list3:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/mozilla%s/source/mozilla-source-%s.tar.gz' % (version,version)
        elif version in list4:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/mozilla%s/mozilla-i686-pc-linux-gnu-%s.tar.gz' % (version,version)
        elif version == 'm14':
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/m14/src/mozilla-source-M14-no-crypto.tar.gz'
        elif version == 'm3':
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/m3/TGZ/mozilla-5.0-SeaMonkey_M3_BRANCH_19990323.tar.gz'
        else:
            command = 'wget -P mozilla http://ftp.mozilla.org/pub/mozilla/releases/mozilla%s/src/mozilla-source-%s.tar.gz' % (version,version)
        commands.append(command)
    return commands

def init_samba():
    baseCommand = 'wget -P samba https://download.samba.org/pub/samba/'
    commands = []
    versionsFile = './versions/samba.txt'
    url0 = 'old-versions/nbserver-%s.tar.Z'
    url1 = 'old-versions/nbserver-%s.tar.gz'
    url2 = 'old-versions/samba-%s.tar.bz2'
    url3 = 'old-versions/samba-%s.tar.gz'
    url4 = 'old-versions/server-%s.tar.gz'
    url5 = 'old-versions/server-%s.tar.Z'
    url6 = 'old-versions/smbserver-%s.tar.gz'
    url7 = 'samba-%s.tar.gz'
    for version in open(versionsFile):
        version = version.strip()
        if version[:3] == "KEY":
            baseCommand1 = baseCommand + eval('url'+version[-1])
            continue
        else:
            command = baseCommand1 % version
        print command
        commands.append(command)
    return commands
            
def init_bind():
    baseCommand = 'wget -P bind -A .tar.gz -r -nd ftp://ftp.isc.org/isc/'
    commands = []
    versionsFile = './versions/bind.txt'
    url0 = 'bind4/src/%s/*'
    url1 = 'bind8/src/%s/*'
    url2 = 'bind9/%s/*'
    url3 = 'bind10/%s/*'
    for version in open(versionsFile):
        version = version.strip()
        if version[:3] == "KEY":
            baseCommand1 = baseCommand + eval('url'+version[-1])
            continue
        else:
            if version[:3] == '4.8':
                command = baseCommand1 % version[:3]
            else:
                command = baseCommand1 % version
        commands.append(command)
    for command in commands:
        download(command)
    commands = ['Hi,honey~',] 
    return commands

def init_postgresql():
    baseCommand = 'wget -P postgresql https://ftp.postgresql.org/pub/source/v%s/'
    commands = []
    versionsFile = './versions/postgresql.txt'
    url0 = 'postgresql-%s.tar.gz'
    url1 = 'postgresql-v%s.tar.gz'
    url2 = 'postgres95-%s.tar.gz'
    for version in open(versionsFile):
        version = version.strip()
        if version[0] > '6':
            command = (baseCommand + url0) % (version,version)
        elif version[:3] == '6.0':
            command = (baseCommand + url1) % (version,version)
        elif version[:2] == '6.':
            command = (baseCommand + url0) % (version[:3],version)
        elif version == '1.08' or version == '1.09':
            command = (baseCommand + url2) % (version,version)
        print command
        commands.append(command)
    return commands

def init_freetype():
    baseCommand = 'wget -P freetype http://freetype.sourcearchive.com/downloads/%s/freetype_%s.orig.tar.gz'
    commands = []
    versionsFile = './versions/freetype.txt'
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % (version,version)
        commands.append(command)
    return commands

def init_openssh():
    baseCommand = 'wget -P openssh http://ftp.jaist.ac.jp/pub/OpenBSD/OpenSSH/openssh-%s'
    commands = []
    versionsFile = './versions/openssh.txt'
    for version in open(versionsFile):
        version = version.strip()
        if version == 'KEY0':
            command1 = baseCommand + '.tgz'
            continue
        elif version == 'KEY1':
            command1 = baseCommand + '.tar.gz'
            continue
        command = command1 % version
        commands.append(command)
    return commands
    
def init_asterisk():
    baseCommand = 'wget -P asterisk http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%s.tar.gz'
    commands = []
    versionsFile = './versions/asterisk.txt'
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % version
        commands.append(command)
    return commands

def init_proftpd():
    baseCommand='wget -P proftpd ftp://ftp.proftpd.org/historic/source/proftpd-%s.tar.gz'
    commands=[]
    versionsFile='./versions/proftpd.txt'
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % version
        commands.append(command)
    return commands
   
def init_libpng():
    baseCommand = 'wget -P libpng http://lil.fr.packages.macports.org/libpng/libpng-%s'
    commands = []
    versionsFile = './versions/libpng.txt'
    for version in open(versionsFile):
        version = version.strip()
        if version == 'key0':
            command1 = baseCommand + '.i386-x86_64.tbz2'
            continue
        elif version == 'key1':
            command1 = baseCommand + '.x86_64.tbz2'
            continue
        command = command1 % version
        commands.append(command)
    return commands    

def init_clamav():
    baseCommand='wget -P clamav http://sourceforge.net/projects/clamav/files/clamav/%s/clamav-%s.tar.gz'
    commands=[]
    versionsFile='./versions/clamav.txt'
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % (version,version)
        commands.append(command)
    return commands

def init_pidgin():
    baseCommand='wget -P pidgin http://pidgin.sourcearchive.com/downloads/%s/pidgin_%s.orig.tar.bz2'
    commands=[]
    versionsFile='./versions/pidgin.txt.tmp'
    for version in open(versionsFile):
        version = version.strip()
        name = version
        if name[:2] == "1:":
            name = name[2:]
        index = name.find("-")
        if index != -1:
            name = name[:index]
        command = baseCommand % (version,name)
        commands.append(command)
    return commands


def init_vlc_media_player():
    baseCommand = 'wget -P vlc_media_player http://download.videolan.org/pub/videolan/vlc/%s/vlc-%s.tar.'
    commands = []
    versionsFile = './versions/vlc_media_player.txt'
    for version in open(versionsFile):
        version = version.strip()
        if version == 'KEY0':
            command1 = baseCommand + 'gz'
            continue
        elif version == 'KEY1':
            command1 = baseCommand + 'bz2'
            continue
        elif version == 'KEY2':
            command1 = baseCommand + 'xz'
            continue
        command = command1 % (version,version)
        commands.append(command)
    return commands    

def init_libav():
    baseCommand = "wget -P libav https://libav.org/releases/libav-%s.tar.xz"
    baseCommand1 = "wget -P libav https://libav.org/releases/old/libav-%s.tar.xz"
    commands = []
    versionsFile = "./versions/libav.txt"
    for version in open(versionsFile):
        version = version.strip()
        if version == "KEY0":
            baseCommand0 = baseCommand1
            continue
        elif version == "KEY1":
            baseCommand0 = baseCommand
            continue
        command = baseCommand0 % version
        commands.append(command)
    return commands

def init_libtiff():
    baseCommand = "wget -P libtiff http://download.osgeo.org/libtiff/tiff-%s.tar.gz"
    baseCommand1 = "wget -P libtiff http://download.osgeo.org/libtiff/old/tiff-%s.tar.gz"
    commands = []
    versionsFile = "./versions/libtiff.txt"
    sset = (['3.8.0','3.6.1','3.7.1','3.7.2'])
    for version in open(versionsFile):
        version = version.strip()
        if version == "KEY0":
            baseCommand0 = baseCommand
            continue
        elif version == "KEY1":
            baseCommand0 = baseCommand1
            continue
        if version in sset:
            baseCommands= baseCommand0[:-14] + "pics-%s.tar.gz"
            command = baseCommands % version
        elif version == 'v3.4pics':
            command = baseCommand0[:-14] + version + ".tar.gz"
        else:
            command = baseCommand0 % version
        commands.append(command)
    return commands

def init_cups():
    baseCommand = "wget -P cups https://www.cups.org/software/%s/cups-%s-source.tar.bz2" 
    versionsFile = "./versions/cups.txt"
    commands = []
    for version in open(versionsFile):
        version = version.strip()
        command = baseCommand % (version,version)
        commands.append(command)
    return commands
def init_quagga():
    baseCommand = "wget -P quagga http://download.savannah.gnu.org/releases/quagga/" 
    versionsFile = "./versions/quagga.txt"
    commands = []
    flag=None
    for version in open(versionsFile):
        version = version.strip()
        if version=="FLAG":
            flag=1
            continue
        if flag==None:
            command = baseCommand + "attic/quagga-%s.tar.gz" % version
        else:
            command = baseCommand + "quagga-%s.tar.gz" % version
        commands.append(command)
    return commands
    
def init_libxslt():
    baseCommand = "wget -P  libxslt http://xmlsoft.org/sources/" 
    versionsFile = "./versions/libxslt.txt"
    commands = []
    flag=None
    for version in open(versionsFile):
        version = version.strip()
        if version=="FLAG":
            flag=1
            continue
        if(flag==None):
            command = baseCommand + "old/libxslt-%s.tar.gz" % version
        else:
            command = baseCommand + "libxslt-%s.tar.gz" % version
        commands.append(command)
    return commands

def init_libxml():
    baseCommand = "wget -P  libxml http://xmlsoft.org/sources/" 
    versionsFile = "./versions/libxml.txt"
    commands = []
    flag=None
    for version in open(versionsFile):
        version = version.strip()
        if version=="FLAG1":
            flag=1
            continue
        elif version == "FLAG2":
            flag=2
            continue
        if flag==None:
            command = baseCommand + "old/libxml-%s.tar.gz" % version
        elif flag==1:
            command = baseCommand + "old/libxml2-%s.tar.gz" % version
        elif flag==2:
            command = baseCommand + "libxml2-%s.tar.gz" % version
        commands.append(command)
    return commands

    
def main():
    
    if len(sys.argv) !=2:
        print '''Usage: python download.py <softwareName>
        Tips:Please confirm your software versions file name must be same to the software name
        Example: chrome.txt firefox.txt...'''
        return
    softwareName = sys.argv[1]
    func_name = "init_" + softwareName
    commands = eval(func_name)()
    
    pool = ThreadPool(64)
    pool.map(download,commands)
    pool.close()
    pool.join()
    

if __name__ == '__main__':
    main()
