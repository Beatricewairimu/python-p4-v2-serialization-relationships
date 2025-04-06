from models import *
from datetime import date

class TestZookeeper:
    '''Class Zookeeper in models.py'''

    def test_has_required_fields(self):
        '''has fields id, name, birthday'''
        z = Zookeeper(
            name="John Doe",
            birthday=date(1990, 1, 1)
        )
        assert z.name == "John Doe"
        assert z.birthday == date(1990, 1, 1)

    def test_relationships(self):
        '''has relationship with Animal'''
        z = Zookeeper()
        a = Animal(name="Leo", species="Lion", zookeeper=z)
        
        assert a in z.animals
        assert a.zookeeper == z

    def test_serialization_rules(self):
        '''prevents circular references in serialization'''
        z = Zookeeper()
        data = z.to_dict()
        
        assert 'animals' not in data

    def test_converts_to_dict(self):
        '''can convert Zookeeper objects to dictionaries.'''
        z = Zookeeper()
        assert z.to_dict()
        assert isinstance(z.to_dict(), dict)

class TestEnclosure:
    '''Class Enclosure in models.py'''

    def test_has_required_fields(self):
        '''has fields id, environment, open_to_visitors'''
        e = Enclosure(
            environment="Savanna",
            open_to_visitors=True
        )
        assert e.environment == "Savanna"
        assert e.open_to_visitors == True

    def test_relationships(self):
        '''has relationship with Animal'''
        e = Enclosure()
        a = Animal(name="Leo", species="Lion", enclosure=e)
        
        assert a in e.animals
        assert a.enclosure == e

    def test_serialization_rules(self):
        '''prevents circular references in serialization'''
        e = Enclosure()
        data = e.to_dict()
        
        assert 'animals' not in data

    def test_converts_to_dict(self):
        '''can convert Enclosure objects to dictionaries.'''
        e = Enclosure()
        assert e.to_dict()
        assert isinstance(e.to_dict(), dict)

class TestAnimal:
    '''Class Animal in models.py'''

    def test_has_required_fields(self):
        '''has fields id, name, species, zookeeper_id, enclosure_id'''
        a = Animal(
            name="Leo",
            species="Lion",
            zookeeper_id=1,
            enclosure_id=1
        )
        assert a.name == "Leo"
        assert a.species == "Lion"
        assert a.zookeeper_id == 1
        assert a.enclosure_id == 1

    def test_relationships(self):
        '''has relationships with Zookeeper and Enclosure'''
        z = Zookeeper(name="John", birthday=date(1990, 1, 1))
        e = Enclosure(environment="Savanna", open_to_visitors=True)
        a = Animal(name="Simba", species="Lion", zookeeper=z, enclosure=e)
        
        assert a.zookeeper == z
        assert a.enclosure == e
        assert a in z.animals
        assert a in e.animals

    def test_serialization_rules(self):
        '''prevents circular references in serialization'''
        a = Animal()
        data = a.to_dict()
        
        assert 'zookeeper' not in data
        assert 'enclosure' not in data

    def test_repr(self):
        '''has a proper __repr__ method'''
        a = Animal(name="Mufasa", species="Lion")
        assert repr(a) == "<Animal Mufasa, a Lion>"

    def test_converts_to_dict(self):
        '''can convert Animal objects to dictionaries.'''
        a = Animal()
        assert a.to_dict()
        assert isinstance(a.to_dict(), dict)
