import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

@pytest.fixture
def hashtable():
    return Hashtable()


def test_set_and_get(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")

    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"


def test_get_nonexistent_key(hashtable):
    assert hashtable.get("nonexistent_key") is None


def test_keys(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    hashtable.set("key3", "value3")

    keys = hashtable.keys()
    assert len(keys) == 3
    assert "key1" in keys
    assert "key2" in keys
    assert "key3" in keys


def test_collision(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")

    # Trigger a collision by setting a key that hashes to the same index
    hashtable.set("k1", "value3")

    # Test retrieval of values after collision
    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"
    assert hashtable.get("k1") == "value3"


def test_hash_range(hashtable):
    key = "test_key"
    index = hashtable.hash(key)
    size = hashtable.size

    assert index >= 0
    assert index < size

