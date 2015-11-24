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
