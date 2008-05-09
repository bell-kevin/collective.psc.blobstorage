from os.path import isfile
from shutil import copyfileobj
from os import name as os_name
from StringIO import StringIO

from zope.interface import implements
from zope.component import adapts

from Products.CMFDefault.interfaces import IFile

from plone.app.blob.interfaces import IBlobbable

class BlobbableFile(object):
    """ adapter for FileUpload objects to work with blobs """
    implements(IBlobbable)
    adapts(IFile)

    def __init__(self, context):
        self.context = context
        self._name = context.filename

    def mimetype(self):
        return self.context.content_type

    def filename(self):
        return self._name

    def feed(self, blob):
        """ see interface ... """
        file_ = StringIO(self.context.data)
        blob.open('w').write(file_.read())

