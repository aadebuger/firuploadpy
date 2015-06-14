'''
Created on 20141110

@author: aadebuger
'''
import unittest
import onlineapp.AndroidManifestInfo

class Test(unittest.TestCase):


    def testName(self):
        (package,versionname)= onlineapp.AndroidManifestInfo.androidmainfestinfo('AndroidManifest1.xml')
        print 'package=',package
        print 'versionname=',versionname
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()