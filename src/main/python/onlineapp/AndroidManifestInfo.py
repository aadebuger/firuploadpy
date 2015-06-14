'''
Created on 20141109

@author: aadebuger
'''
import xmltodict
def  androidmainfestinfo(filename):

        ret = xmltodict.parse(open(filename))
        print 'ret=',ret
        print 'manifest',ret['manifest']
        print 'manifest @package',ret['manifest']['@package']
        
        
        print 'manifest @android:versionName',ret['manifest'].get('@android:versionName',"1.0")        
        return (ret['manifest']['@package'],ret['manifest'].get('@android:versionName',"1.0"))
if __name__ == '__main__':
    pass