# Implement an Array data structure as a simplified type of list.


class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds, and
            return self.__a[n]  # only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds, and
            self.__a[n] = value  # only set item if in bounds

    def insert(self, item):  # Insert item at end
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k + 1]  # right over 1
                return True  # Return success flag

        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__a[j])


if __name__ == "__main__":
    maxSize = 10  # Max size of the array
    arr = Array(maxSize)  # Create an array object

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

    print("Array containing", len(arr), "items")
    arr.traverse()

    print("Search for 12 returns", arr.search(12))

    print("Search for 12.34 returns", arr.search(12.34))

    print("Deleting 0 returns", arr.delete(0))
    print("Deleting 17 returns", arr.delete(17))

    print("Setting item at index 3 to 33")
    arr.set(3, 33)

    print("Array after deletions has", len(arr), "items")
    arr.traverse()
