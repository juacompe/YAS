from unittest2 import TestCase
from yas.stub import Stub

class TestStub(TestCase):
    def test_stub_with_properties(self):
        jack = Stub(name = 'Jack', age = 20)
        self.assertEqual('Jack', jack.name) 
        self.assertEqual(20, jack.age) 

    def test_stub_nested_properties(self):
        jack = Stub()
        jack.make_chain().car.engine.horse_power = 500
        self.assertEqual(500, jack.car.engine.horse_power)


