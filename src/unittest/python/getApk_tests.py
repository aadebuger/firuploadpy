'''
Created on 20141114

@author: aadebuger
'''
import unittest
import onlineapp.FirUpload

class Test(unittest.TestCase):


    def testName(self):
           onlineapp.FirUpload.getApk(".");


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()