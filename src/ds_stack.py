from ds_linked_list import LinkedList


class Stack(object):
    def __init__(self, item=None):
        self.linked_list = LinkedList(item)

    def push(self, item):
        self.linked_list.append(item)

    def peek(self):
        return self.linked_list.tail.item

    def pop(self):
        return self.linked_list.pop()

    def length(self):
        return self.linked_list.length()

    def is_empty(self):
        return self.linked_list.is_empty()

    def to_list(self):
        return self.linked_list.to_list()


if __name__ == "__main__":
    st = Stack()
    st.push(3)
    st.push(32)
    st.push(24)
    st.push(42)
    print(st.length(), st.to_list(), st.is_empty())
    while True:
        a = st.pop()
        print(st.length(), st.to_list(), a, st.is_empty())
        if a is None:
            break
