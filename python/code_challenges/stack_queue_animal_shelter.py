from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("Animal not accepted")

    def dequeue(self, pref=None):
        if pref == "dog":
            return self.dog_queue.dequeue()
        elif pref == "cat":
            return self.cat_queue.dequeue()
        elif pref is None:
            raise InvalidOperationError("No animals in the shelter")


class Dog:
    pass


class Cat:
    pass
