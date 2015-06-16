'''
Created on 201411108

@author: aadebuger
'''
import unittest
import requests
import onlineapp.FirUpload
#7e697da0663511e4b3e635cd05465ca74c55a20f
class Test(unittest.TestCase):


    def testName(self):
        token = "7e697da0663511e4b3e635cd05465ca74c55a20f"
        url = "http://fir.im/api/v2/app/info/com.example.zhy_slidingmenu?token=%s&type=android"%(token)
        res = requests.get(url)
        print res.json()
        print res.json()['bundle']['pkg']['token']
    def testUpload(self):
        token = "7e697da0663511e4b3e635cd05465ca74c55a20f"
        url = "http://fir.im/api/v2/app/info/com.example.zhy_slidingmenu?token=%s&type=android"%(token)
        res = requests.get(url)
        print res.json()
        print res.json()['bundle']['pkg']['token']
        token = res.json()['bundle']['pkg']['token']
        key = res.json()['bundle']['pkg']['key']
        res1 = onlineapp.FirUpload.upload(key,token,"","","MainActivity-debug.apk")
        print res.json()['id']
#        onlineapp.FirUpload.update (res.json()['id'],token)
        onlineapp.FirUpload.update1(res1['versionOid'],"1.0","myunittest")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
