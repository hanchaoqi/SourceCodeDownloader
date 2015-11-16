#!/usr/bin/python
'''
DownLoad source code
'''
import sys
from subprocess import Popen,PIPE
from multiprocessing.dummy import Pool as ThreadPool


def communicate(commandLine):
    print('Executing command:%s...' % commandLine)
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
                'linux_kernel':'wget -P linux_kernel https://www.kernel.org/pub/linux/kernel/v%s/linux-%s.tar.xz'}
    
    versionsFile = softwareName + ".txt"
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
            if version[0] == "4"
                command = baseCommand % ("4.x",version)
            else:
                command = baseCommand % (version[:3],version)
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
