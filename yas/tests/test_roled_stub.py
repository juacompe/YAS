from unittest2 import TestCase
from yas.stub import ModelStub

class TestModelStub(TestCase):
    def test_proxy_of_meta_class_is_false(self):
        """
        roles.django.ModelRoleType is setting proxy to True to allows a 
        roled model to save.
        """
        self.assertFalse(ModelStub.Meta.proxy)

