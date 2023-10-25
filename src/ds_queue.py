from ds_linked_list import LinkedList


class Queue(object):
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, item):
        self.linked_list.append_left(item)

    def dequeue(self):
        return self.linked_list.pop()

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
    q = Queue()
    print(q.is_empty())
    q.enqueue(8.4)
    q.enqueue(42)
    q.enqueue(True)
    q.enqueue(None)
    print(q.to_list())
    q.rotate_right()
    print(q.to_list())
    q.rotate_right()
    print(q.to_list())
    q.rotate_right()
    print(q.to_list())
    q.rotate_right()
    print(q.to_list())
