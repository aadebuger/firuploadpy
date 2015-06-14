'''
Created on 20141109

@author: aadebuger
'''
import unittest

import xmltodict
class Test(unittest.TestCase):


    def testName(self):
        ret = xmltodict.parse(open("AndroidManifest.xml"))
        print 'ret=',ret
        print 'manifest',ret['manifest']
        print 'manifest @package',ret['manifest']['@package']
        print 'manifest @android:versionName',ret['manifest']['@android:versionName']        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()