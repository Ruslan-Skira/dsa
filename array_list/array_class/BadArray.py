# Implement an Array Data structure as asimplified type of list.


class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.nItems = 0  # No items in array initially

    def insert(self, item):  # Insert item at end
        self.__a[self.nItems] = item  # Item goes at current end
        self.nItems += 1  # Increment number of items

    def search(self, item):
        for j in range(self.nItems):  # Search among current
            if self.__a[j] == item:  # If found,
                return self.__a[j]  # then return item

        return None  # Not found -> None

    def delete(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                for k in range(j, self.nItems):
                    self.__a[k] = self.__a[k + 1] # TODO: need to fix
                self.nItems -= 1
                return True

        return False

    def traverse(self, function=print):
        for j in range(self.nItems):
            function(self.__a[j])


if __name__ == "__main__":
    maxSize = 10  # Max size of the Array
    arr = Array(maxSize)  # Create an Array object

    arr.insert(77)  # Insert 10 items
    arr.insert(99)
    arr.insert("foo")
    arr.insert("bar")
    arr.insert(44)
    arr.insert(55)
    arr.insert(12.34)
    arr.insert(0)
    arr.insert("baz")
    arr.insert(-17)

    print("Array containing", arr.nItems, "items")
    arr.traverse()

    print("Search for 12 returns", arr.search(12))

    print("Search for 12.34 returns", arr.search(12.34))

    print("Deleting 0 returns", arr.delete(0))
    print("Deleting 17 returns", arr.delete(17))

    print("Array after deletions has", arr.nItems, "items")
    arr.traverse()
