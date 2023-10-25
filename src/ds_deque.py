from ds_linked_list import LinkedList


class Deque(object):
    def __init__(self):
        self.linked_list = LinkedList()

    def add_front(self, item):
        self.linked_list.append(item)

    def add_rear(self, item):
        self.linked_list.append_left(item)

    def pop_front(self):
        return self.linked_list.pop()

    def pop_rear(self):
        return self.linked_list.pop_left()

    def length(self):
        return self.linked_list.length()

    def is_empty(self):
        return self.linked_list.is_empty()

    def to_list(self):
        return self.linked_list.to_list()

    def rotate_right(self, n=1):
        self.linked_list.rotate_right(n)

    def rotate_left(self, n=1):
        self.linked_list.rotate_left(n)

    def peek_front(self):
        return self.linked_list.tail.item

    def peek_rear(self):
        return self.linked_list.head.item


if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())
    d.add_front(8.4)
    print(d.to_list())
    d.add_rear(42)
    print(d.to_list())
    d.add_rear(True)
    print(d.to_list())
    d.add_front(None)
    print(d.to_list())
    d.pop_rear()
    print(d.to_list())
    d.pop_front()
    print(d.to_list())
    d.pop_front()
    print(d.to_list())
