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

def getVersions(versionsFile):
    return [version.strip() for version in open(versionsFile)]

def init(softwareName):
    '''init needed data,output command list'''
    dictForCommand ={'chrome':'wget -P chrome https://chromium.googlesource.com/chromium/src.git/+archive/%s.tar.gz',
                'linux_kernel':'wget -P linux_kernel https://www.kernel.org/pub/linux/kernel/v%s/linux-%s.tar.xz',
                'firefox':'wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/%s/source/firefox-%s.source.tar.bz2'}
    
    versionsFile = softwareName + "1.txt"
    baseCommand = dictForCommand[softwareName]
    commands = []
    
    if softwareName == "chrome":
        for version in open(versionsFile):
            version = version.strip()
            command = baseCommand % version
            commands.append(command)
    elif softwareName == "linux_kernel":
        for version in open(versionsFile):
            version = version.strip()
            if version[0] == "4":
                command = baseCommand % ("4.x",version)
            else:
                command = baseCommand % (version[:3],version)
            commands.append(command)
    elif softwareName == "firefox":
        for version in open(versionsFile):
            version = version.strip()
            baseCommand = dictForCommand[softwareName]
            if version.split(".")[0] >= "1":
                if version[:3] == "1.0" or version[:3] == "2.0" or version[:3] == "3.0":
                    baseCommand = "wget -P firefox http://ftp.mozilla.org/pub/firefox/releases/%s/source/firefox-%s-source.tar.bz2"
                if version[-4:] == "real":
                    command = baseCommand % (version,version.split("-")[0])
                else:
                    command = baseCommand % (version,version) 
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
    else:
        print "Software Name Wrong!"
        return
    return commands
        
 

def main():
    
    if len(sys.argv) !=2:
        print '''Usage: python download.py <softwareName>
        Tips:Please confirm your software versions file name must be same to the software name
        Example: chrome.txt mozilla.txt...'''
        return
    commands = init(sys.argv[1])
    
    pool = ThreadPool(64)
    pool.map(download,commands)
    pool.close()
    pool.join()
    

if __name__ == '__main__':
    main()
