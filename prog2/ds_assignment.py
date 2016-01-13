class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):
    """
    >>> test = SinglyLinkedList()
    >>> print test.prepend(6)
    Insertion 6 Successful
    >>> print test.prepend(9)
    Insertion 9 Successful
    >>> print test.prepend(10)
    Insertion 10 Successful
    >>> print test
    List:10->9->6
    >>> print test.__len__
    3
    >>> print test.__contains__(6)
    True
    >>> print test.remove(11)
    Element 11 not in the list
    >>> print test.remove(9)
    Element 9 removed successfully
    >>> print test
    List:10->6
    """
    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        # TODO
        self._head = None

    @property
    def __len__(self):
        # TODO
        len = 0
        temp = self._head
        while temp:
            len += 1
            temp = temp.next
        return len

    def __iter__(self):
        # TODO
        temp = self._head
        while temp:
            yield str(temp.item)
            temp = temp.next

    def __contains__(self, item):
        # TODO
        temp = self._head
        while temp:
            if temp.item == item:
                return True
            temp = temp.next
        return False

    def remove(self, item):
        # TODO: find item and remove it.
        temp = self._head
        prev = None
        if temp.item == item:
            self._head = temp.next
        while temp:
            if temp.item == item:
                if prev is None:
                    self._head = temp.next
                else:
                    prev._next = temp.next
                return "Element " + str(item) + " removed successfully"
            elif temp:
                prev = temp
                temp = temp.next
        return "Element " + str(item) + " not in the list"

    def prepend(self, item):
        # TODO ad item to the front of the list
        new = SinglyLinkedNode(item)
        if self._head is None:
            self._head = new
        else:
            temp = self._head
            self._head = new
            new._next = temp
        return "Insertion " + str(item) + " Successful"

    def __repr__(self):
        s = "List:" + "->".join([item for item in self])
        return s


class ChainedHashDict(object):
    """
    >>> chained=ChainedHashDict(hashfunc=terrible_hash(10))
    >>> print chained.__setitem__(2,20)
    Inserted Successfully
    >>> print chained.__setitem__(4,40)
    Inserted Successfully
    >>> print chained.__setitem__(6,60)
    Inserted Successfully
    >>> print chained.__getitem__(4)
    40
    >>> print chained.__delitem__(4)
    Element (4, 40) removed successfully
    >>> print chained.__contains__(6)
    True
    >>> print chained.__setitem__(8,80)
    Inserted Successfully
    >>> print chained.__len__()
    3
    >>> chained.display()
    ---Chained Hash Dictionary---
    Bin0 List:(8, 80)->(6, 60)->(2, 20)
    Bin1 List:
    Bin2 List:
    Bin3 List:
    Bin4 List:
    Bin5 List:
    Bin6 List:
    Bin7 List:
    Bin8 List:
    Bin9 List:
    ---end---
    >>> print chained.__setitem__(9,90)
    Inserted Successfully
    >>> print chained.__setitem__(0,0)
    Inserted Successfully
    >>> print chained.__getitem__(9)
    90
    >>> print chained.__setitem__(1,10)
    Inserted Successfully
    >>> print chained.__setitem__(7,99)
    Inserted Successfully
    >>> print chained.__setitem__(5,55)
    Inserted Successfully
    >>> print chained.__len__()
    8
    >>> chained.display()
    ---Chained Hash Dictionary---
    Bin0 List:
    Bin1 List:
    Bin2 List:
    Bin3 List:
    Bin4 List:
    Bin5 List:
    Bin6 List:
    Bin7 List:
    Bin8 List:
    Bin9 List:
    Bin10 List:(5, 55)->(2, 20)->(6, 60)->(8, 80)->(9, 90)->(0, 0)->(1, 10)->(7, 99)
    Bin11 List:
    Bin12 List:
    Bin13 List:
    Bin14 List:
    Bin15 List:
    Bin16 List:
    Bin17 List:
    Bin18 List:
    Bin19 List:
    ---end---
    """

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()

        # TODO: Construct a new table
        pass

        self.table = {}
        self.item_count = 0
        self._bin_count = bin_count
        self._max_load = max_load
        self.hashfunc = hashfunc
        for bin in range(self._bin_count):
            self.table[bin] = SinglyLinkedList()

    @property
    def load_factor(self):
        # TODO
        pass
        load = float(self.__len__()) / self._bin_count
        return load

    @property
    def bin_count(self):
        # TODO
        pass
        return self._bin_count

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        pass
        new = ChainedHashDict(bincount, hashfunc=self.hashfunc)
        self._bin_count = bincount

        key_list = self.getkey(self.table)
        value_list = self.getvalue(self.table)
        l = len(key_list)
        for i in range(l):
            bin = self.hashfunc(key_list[i]) % bincount
            new.table[bin].prepend(item=(key_list[i], value_list[i]))

        self.table = new.table

    def gettuple(self, inp, key):
        temp = inp._head
        while temp:
            if temp._item[0] == key:
                return temp._item[1]
            temp = temp.next
        return False

    def getkey(self, table):
        self._table = table
        keys = []
        for bin in self._table:
            temp = self._table[bin]._head

            while temp:
                keys.append(temp._item[0])
                temp = temp.next
        return keys

    def getvalue(self, table):
        self._table = table
        values = []
        for bin in self._table:
            temp = self._table[bin]._head

            while temp:
                values.append(temp._item[1])
                temp = temp.next
        return values

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        pass
        bin = self.hashfunc(key) % self._bin_count
        temp = self.gettuple(self.table[bin], key)
        return temp

    def __setitem__(self, key, value):
        # TODO:
        pass

        bin = self.hashfunc(key) % self._bin_count

        self.table[bin].prepend(item=(key, value))
        self.item_count += 1
        if self.load_factor >= self._max_load:
            self.rebuild(self.bin_count * 2)
        return "Inserted Successfully"

    def __delitem__(self, key):
        # TODO
        pass
        bin = self.hashfunc(key) % self._bin_count
        temp = self.table[bin].remove((key, self.__getitem__(key)))
        self.item_count -= 1
        return temp

    def __contains__(self, key):
        # TODO
        pass
        bin = self.hashfunc(key) % self._bin_count
        if self.gettuple(self.table[bin], key):
            return True
        return False

    def __len__(self):
        # TODO
        pass
        return self.item_count

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        pass
        print "---Chained Hash Dictionary---"
        for each in self.table:
            print "Bin" + str(each), self.table[each]
        print "---end---"


class OpenAddressHashDict(object):
    """
    >>> chained1 = OpenAddressHashDict()
    >>> chained1.__setitem__(1,10)
    Insertion Successful
    >>> chained1.__setitem__(2,20)
    Insertion Successful
    >>> chained1.display()
    ---Open address Hash Dictionary---
    Bin0 None
    Bin1 (1, 10)
    Bin2 (2, 20)
    Bin3 None
    Bin4 None
    Bin5 None
    Bin6 None
    Bin7 None
    Bin8 None
    Bin9 None
    ---end---
    >>> print chained1.__getitem__(2)
    20
    >>> print chained1.__len__()
    2
    >>> print chained1.__contains__(1)
    True
    >>> print chained1.__contains__(3)
    False
    >>> print chained1.__delitem__(2)
    Deletion Successful
    >>> print chained1.__len__()
    1
    >>> chained1.__setitem__(7,21)
    Insertion Successful
    >>> chained1.__setitem__(3,267)
    Insertion Successful
    >>> chained1.__setitem__(4,24)
    Insertion Successful
    >>> chained1.__setitem__(5,23)
    Insertion Successful
    >>> chained1.__setitem__(20,20)
    Insertion Successful
    >>> chained1.__setitem__(14,78)
    Insertion Successful
    >>> chained1.__setitem__(15,98)
    Insertion Successful
    >>> print chained1.__len__()
    8
    >>> chained1.display()
    ---Open address Hash Dictionary---
    Bin0 (20, 20)
    Bin1 (1, 10)
    Bin2 None
    Bin3 (3, 267)
    Bin4 (4, 24)
    Bin5 (5, 23)
    Bin6 None
    Bin7 (7, 21)
    Bin8 None
    Bin9 None
    Bin10 None
    Bin11 None
    Bin12 None
    Bin13 None
    Bin14 (14, 78)
    Bin15 (15, 98)
    Bin16 None
    Bin17 None
    Bin18 None
    Bin19 None
    ---end---
    """

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()

        # TODO initialize
        pass
        self.table = {}
        self.item_count = 0
        self._bin_count = bin_count
        self.hashfunc = hashfunc
        for bin in range(self._bin_count):
            self.table[bin] = None

    @property
    def load_factor(self):
        # TODO
        pass
        load = float(self.__len__()) / self._bin_count
        return load

    @property
    def bin_count(self):
        # TODO
        pass
        return self._bin_count

    def keyitem(self, table):
        keyitem = []
        for val in table.values():
            if val:
                keyitem.append(val[0])
        return keyitem

    def valueitem(self, table):
        valueitem = []
        for val in table.values():
            if val:
                valueitem.append(val[1])
        return valueitem

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        pass
        new = OpenAddressHashDict(bin_count=bincount)
        keyitem = self.keyitem(self.table)
        valueitem = self.valueitem(self.table)
        self._bin_count = bincount
        for i in range(len(keyitem)):
            bin = self.hashfunc(keyitem[i]) % self._bin_count
            if new.table[bin] is None:
                new.table[bin] = (keyitem[i], valueitem[i])
            else:
                for bin in range(bin + 1, len(new.table)) + range(0, bin):
                    if new.table[bin] is None:
                        new.table[bin] = (keyitem[i], valueitem[i])
                        break
        self.table = new.table

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        pass
        keyitem = self.keyitem(self.table)
        valitem = self.valueitem(self.table)
        for i in range(len(keyitem)):
            if key == keyitem[i]:
                return valitem[i]
        return "No element"

    def __setitem__(self, key, value):
        # TODO:
        pass
        bin = self.hashfunc(key) % self._bin_count
        if self.table[bin] is None:
            self.table[bin] = (key, value)
            self.item_count += 1
        else:
            for bin in range(bin + 1, len(self.table)) + range(0, bin):
                if self.table[bin] is None:
                    self.table[bin] = (key, value)
                    self.item_count += 1
                    break
        if self.load_factor >= 0.7:
            self.rebuild(self._bin_count * 2)
        print "Insertion Successful"

    def __delitem__(self, key):
        # TODO
        pass
        bin = self.hashfunc(key) % self._bin_count
        if self.table[bin][0] is key:
            self.table[bin] = None
            self.item_count -= 1
            return "Deletion Successful"
        else:
            for bin in range(bin + 1, len(self.table)) + range(0, bin):
                if self.table[bin][0] is key:
                    self.table[bin] = None
                    self.item_count -= 1
                    return "Deletion Successful"

    def __contains__(self, key):
        # TODO
        pass
        if self.__getitem__(key) == "No element":
            return False
        return True

    def __len__(self):
        # TODO
        pass
        return self.item_count

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        pass
        print "---Open address Hash Dictionary---"
        for each in self.table:
            print "Bin" + str(each), self.table[each]
        print "---end---"


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTreeDict(object):
    """
    >>> bst = BinarySearchTreeDict()
    >>> print bst.__setitem__(10, 10)
    Insertion Successful
    >>> print bst.__setitem__(12, 12)
    Insertion Successful
    >>> print bst.__setitem__(14, 14)
    Insertion Successful
    >>> print bst.__contains__(14)
    True
    >>> print bst.__contains__(15)
    False
    >>> print bst.__getitem__(12)
    12
    >>> print bst.__getitem__(15)
    False
    >>> print bst.height
    3
    >>> bst.__delitem__(12)
    >>> print bst.items()
    (10, 10)->(14, 14)
    >>> print bst.height
    2
    >>> print bst.__setitem__(4, 4)
    Insertion Successful
    >>> print bst.__setitem__(7, 7)
    Insertion Successful
    >>> print bst.__setitem__(18, 18)
    Insertion Successful
    >>> print bst.__setitem__(13, 13)
    Insertion Successful
    >>> print bst.inorder_keys()
    4->7->10->13->14->18
    >>> print bst.preorder_keys()
    10->4->7->14->13->18
    >>> print bst.postorder_keys()
    7->4->13->18->14->10
    >>> print bst.__len__()
    6
    >>> bst.display()
    Inorder: 4->7->10->13->14->18
    Preorder: 10->4->7->14->13->18
    Postorder: 7->4->13->18->14->10
    """

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()

        # TODO initialize
        self.root = None

    @property
    def height(self):
        # TODO
        return self.ht(self.root)

    def ht(self, tree):
        temp = tree
        if temp is None:
            return 0
        else:
            return 1 + max(self.ht(temp.left), self.ht(temp.right))

    def inorder_keys(self):
        # TODO:Use the 'yield'  keyword and StopIteration exception
        # to return the keys, using an INORDER traversal
        pass
        return "->".join(str(data[0]) for data in self.inorder_keys_fetch(self.root))

    def inorder_keys_fetch(self, tree):
            temp = tree
            if temp:
                for data in self.inorder_keys_fetch(temp.left):
                    yield data
                yield tree.data
                for data in self.inorder_keys_fetch(temp.right):
                    yield data
            else:
                StopIteration

    def postorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in POSTORDER
        pass
        return "->".join(str(data[0]) for data in self.postorder_keys_fetch(self.root))

    def postorder_keys_fetch(self, tree):
            temp = tree
            if temp:
                for data in self.postorder_keys_fetch(temp.left):
                    yield data

                for data in self.postorder_keys_fetch(temp.right):
                    yield data
                yield tree.data
            else:
                StopIteration

    def preorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in PREORDER
        pass
        return "->".join(str(data[0]) for data in self.preorder_keys_fetch(self.root))

    def preorder_keys_fetch(self, tree):
            temp = tree
            if temp:
                yield tree.data
                for data in self.preorder_keys_fetch(temp.left):
                    yield data

                for data in self.preorder_keys_fetch(temp.right):
                    yield data
            else:
                StopIteration

    def items(self):
        # TODO: Use 'yield' to return the items (key and value) using
        # an INORDER traversal.
        pass
        return "->".join(str(data) for data in self.inorder_keys_fetch(self.root))

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        pass
        temp = self.root
        while temp is not None:
            if temp.data[0] == key:
                return temp.data[1]
            if temp.data[0] < key:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def __setitem__(self, key, value):
        # TODO:
        pass
        if self.root is None:
            self.root = BinaryTreeNode(data=(key, value))
            return "Insertion Successful"
        current_node = self.root
        while current_node is not None:
            if key > current_node.data[0]:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BinaryTreeNode(data=(key, value), parent=current_node)
                    return "Insertion Successful"
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BinaryTreeNode(data=(key, value), parent=current_node)
                    return "Insertion Successful"

    def tree_min(self, key):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp

    def attach(self, x, y):
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y is not None:
            y.parent = x.parent

    def __delitem__(self, key):
        # TODO
        pass
        temp = self.root
        while temp:
            if temp.data[0] == key:
                break
            elif key < temp.data[0]:
                temp = temp.left
            elif key > temp.data[0]:
                temp = temp.right

        if temp is not None:
            if temp.left is None:
                self.attach(temp, temp.right)
            elif temp.right is None:
                self.attach(temp, temp.left)
            else:
                a = self.tree_min(temp.right)
                if a.parent != temp:
                    self.attach(a, a.right)
                    a.right = temp.right
                    a.right.parent = temp
                self.attach(a, temp)
                a.left = temp.left
                a.left.parent = a

    def __contains__(self, key):
        # TODO
        pass
        temp = self.root
        while temp is not None:
            if temp.data[0] == key:
                return True
            if temp.data[0] < key:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def __len__(self):
        # TODO
        pass
        i = 0
        for data in self.inorder_keys_fetch(self.root):
                i += 1
        return i

    def display(self):
        # TODO: Print the keys using INORDER on one
        #      line and PREORDER on the next
        pass
        print "Inorder: " + self.inorder_keys()
        print "Preorder: " + self.preorder_keys()
        print "Postorder: " + self.postorder_keys()


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :rtype : int
    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passes into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item):
        return bin
    return hashfunc


def main():
    # Thoroughly test your program and produce useful out.
    #
    # Do at least these kinds of tests:
    #  (1)  Check the boundary conditions (empty containers,
    #       full containers, etc)
    #  (2)  Test your hash tables for terrible hash functions
    #       that map to keys in the middle or ends of your
    #       table
    #  (3)  Check your table on 100s or randomly generated
    #       sets of keys to make sure they function
    #
    #  (4)  Make sure that no keys / items are lost, especially
    #       as a result of deleting another key
    pass

    
    print "------Linked List------"
    test = SinglyLinkedList()
    print test.prepend(6)
    print test.prepend(9)
    print test.prepend(10)
    print test
    print "Length = ", test.__len__
    print "Contains 6: ", test.__contains__(6)
    print test.remove(11)
    print test.remove(9)
    print test


    print "------Chained Hash Dictionary------"
    chained=ChainedHashDict(hashfunc=terrible_hash(10))
    print "(2, 20)", chained.__setitem__(2, 20)
    print "(4, 40)", chained.__setitem__(4, 40)
    print "(6, 60)", chained.__setitem__(6, 60)
    print "Get Item of 4: ", chained.__getitem__(4)
    print chained.__delitem__(4)
    print "Contains 6: ", chained.__contains__(6)
    print "(8, 80)", chained.__setitem__(8,80)
    print "Length= ", chained.__len__()
    chained.display()
    print "(9, 90)", chained.__setitem__(9,90)
    print "(0, 0)", chained.__setitem__(0,0)
    print "Get Item of 9: ", chained.__getitem__(9)
    print "(1, 10)", chained.__setitem__(1,10)
    print "(7, 99)", chained.__setitem__(7,99)
    print "(5, 55)", chained.__setitem__(5,55)
    print "Length= ", chained.__len__()
    chained.display()


    print "------Open Address Hash Dictionary------"
    chained1 = OpenAddressHashDict()
    print "(1, 10)",
    chained1.__setitem__(1,10)
    print "(2, 20)",
    chained1.__setitem__(2,20)
    chained1.display()
    print "Get Item of 2: ", chained1.__getitem__(2)
    print "Length: ", chained1.__len__()
    print "Contains 1:",chained1.__contains__(1)
    print "Contains 3:", chained1.__contains__(3)
    print "Item 2 ", chained1.__delitem__(2)
    print "Length: ", chained1.__len__()
    print "(7, 21)",
    chained1.__setitem__(7,21)
    print "(3, 267)",
    chained1.__setitem__(3,267)
    print "(4, 24)",
    chained1.__setitem__(4,24)
    print "(5, 23)",
    chained1.__setitem__(5,23)
    print "(2, 20)",
    chained1.__setitem__(20,20)
    print "(14, 78)",
    chained1.__setitem__(14,78)
    print "(15, 98)",
    chained1.__setitem__(15,98)
    print "Length: ", chained1.__len__()
    chained1.display()


    print "------Binary Search Tree------"
    bst = BinarySearchTreeDict()
    print "(10, 10)", bst.__setitem__(10, 10)
    print "(12, 12)", bst.__setitem__(12, 12)
    print "(14, 14)", bst.__setitem__(14, 14)
    print "Contains 14: ", bst.__contains__(14)
    print "Contains 15: ", bst.__contains__(15)
    print "Get Item of 12: ", bst.__getitem__(12)
    print "Height= ", bst.height
    print "Deleted 12"
    bst.__delitem__(12)
    print "Items: ", bst.items()
    print "Height= ", bst.height
    print "(4, 4)", bst.__setitem__(4, 4)
    print "(7, 7)", bst.__setitem__(7, 7)
    print "(18, 18)", bst.__setitem__(18, 18)
    print "(13, 13)", bst.__setitem__(13, 13)
    print "Inorder= ", bst.inorder_keys()
    print "Preorder= ", bst.preorder_keys()
    print "Postorder= ", bst.postorder_keys()
    print "Length= ", bst.__len__()
    bst.display()


if __name__ == '__main__':

    main()
    #import doctest
    #doctest.testmod()
