import unittest

from zope.testing import doctestunit
from zope.component import testing
from zope.component import getUtility
from Testing import ZopeTestCase as ztc
from zope.interface.verify import verifyObject

from zope.formlib import form

from Products.PloneSoftwareCenter.storage.interfaces import IPSCFileStorage
from collective.psc.blobstorage import BlobStorage

class TestCase(unittest.TestCase):            
    def test_implements_interface(self):
        class Dummy: pass
        bs = BlobStorage(Dummy())
        assert verifyObject(IPSCFileStorage, bs)
        
def test_suite():
    return unittest.TestSuite((unittest.makeSuite(TestCase),))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
