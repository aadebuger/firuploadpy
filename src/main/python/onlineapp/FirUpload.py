'''
Created on 2014 1108

@author: aadebuger
'''
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from glob import glob
import sys
import os
import AndroidManifestInfo
infourl = 'http://fir.im/api/v2/app/info/%s?token=%s&type=%s'
uploadurl = 'http://up.qiniu.com/'
updateinfourl = 'http://fir.im/api/v2/app/%s?token=%s'

def getToken():
    return os.environ.get('FIR_TOKEN',"7e697da0663511e4b3e635cd05465ca74c55a20f")
def getJobname():
    return os.environ.get('JOB_NAME',"MyApp")


def getBundle(package):
        token = getToken()
        url = "http://fir.im/api/v2/app/info/%s?token=%s&type=android"%(package,token)
        res = requests.get(url)
        print res.json()
        print res.json()['bundle']['pkg']['token']
        return res.json()
def upload(pkgkey,pkgtoken,icon,pkg,filename):
    e = MultipartEncoder(
    fields={'key': pkgkey, 'token': pkgtoken,
            'file': ('filename', open(filename), 'text/plain')}
    )
 

    uploadresponse = requests.post(uploadurl, data=e, headers={'Content-Type': e.content_type})
    print uploadresponse.json()
    return  uploadresponse.json()
    
def update(appid,token):
    updateinfourl1 = updateinfourl % (appid, token)
    dict =""" {"version":"1.0"}"""
    updateinforesponse = requests.put(updateinfourl1, dict)
#    print updateinforesponse.text
def update1(versionOid,version,name):
    updateinfourl1 = "http://fir.im/api/v2/appVersion/%s/complete" % (versionOid)
#    dict ={"version":"%s","name":"%s"}"""%(version,name)
    dict = {"version":version,"name":name,"desc":"hello"};
    print 'dict=',dict   
    updateinforesponse = requests.put(updateinfourl1, data=dict)
#    print updateinforesponse.text
def update2(token,appid,version,name):
    updateinfourl1 = "http://fir.im/api/v2/app/%s?token=%s" % (appid,token)
    print 'updateinfourl1',updateinfourl1
#    dict ={"version":"%s","name":"%s"}"""%(version,name)
    dict = {"version":version,"name":name,"desc":"hello"};
    print 'dict=',dict   
    updateinforesponse = requests.put(updateinfourl1, data=dict)
#    print updateinforesponse.text

def isValidapk(filename):
      print 'filename',filename
      if not filename.endswith(".apk"):
            return False;
      if filename.endswith("unaligned.apk"):
            return False;   
      return True;
def getApk(dir):
        files = os.listdir(dir)
        validapks = filter(isValidapk,files)
        print 'apks=',validapks
        return validapks
if __name__ == '__main__':
        if len(sys.argv)<3:
                        print 'python firuploadpy apk AndroidManifest.xml'
                        exit(0)
        if  os.path.isdir( sys.argv[2]):
                androidmainfestfile=  sys.argv[2]+"/"+ "AndroidManifest.xml"
        else:
                androidmainfestfile= sys.argv[2]
        
        if not os.path.exists(androidmainfestfile):
             print  androidmainfestfile+" no exists"
             exit(-1)
        apkfile = sys.argv[1]
        if  os.path.isdir( sys.argv[1]):
                apks =  getApk(sys.argv[1])            
                if len(apks)>=1:
                    apkfile = sys.argv[1]+"/"+ apks[0]
                    
        (package,versionname)= AndroidManifestInfo.androidmainfestinfo(androidmainfestfile)
        print 'package=',package
        print 'versionname=',versionname
        bundle = getBundle(package)
        token = bundle['bundle']['pkg']['token']
        key = bundle['bundle']['pkg']['key']
        res1 = upload(key,token,"","",apkfile)
#        print res1['message']
        print bundle['id']
        print 'bundle short=',bundle['short']
        
#        onlineapp.FirUpload.update (res.json()['id'],token)
        name=getJobname()
        if len(sys.argv)>3:
                name=sys.argv[3]
        update1(res1['versionOid'],versionname,name)
        update2(getToken(),bundle['id'],versionname,name)
        print 'url=',"http://fir.im/%s"%bundle['short']
        print 'qucode=',"""<span><img src="http://qr.liantu.com/api.php?text=aa" alt="qrcode"/></span>"""
        
