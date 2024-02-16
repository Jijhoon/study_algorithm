import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def get_user_details():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    return name, email


def create_linked_list():
    name, email = get_user_details()
    head = Node(name)
    head.next = Node(email)
    return head

linked_list = create_linked_list()

##------------------------------------------------------------##

rotto = [random.randint(1, 45) for _ in range(6)]
for i in range(6):
    print(f"{rotto[i]}", end = ' ')