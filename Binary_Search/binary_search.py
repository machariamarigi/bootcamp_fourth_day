class BinarySearch(list):
    """
        This class inherits from the list class.
        The __init__() takes two integers as parameters
        The first is is the length of the list.
        The second is the difference between the consecutive values.
        It initializes an instance variable 'length'
        It has a method called search that takes one argument that is the value to be found
        The search method returns a dictionary object that contains count, index.
        The search method implements the binary search algorithm
    """


# Creating a List
    def __init__(self, a, b):
        # refer to list Class
        super(BinarySearch, self).__init__()
        # holds the length of a list
        self.length = a
        # holds difference between values in a list
        self.b = b
        # Append values
        for item in range(self.b, (self.b*self.length) + 1, self.b):
            self.append(item)

    # method implementing Binary Search for a value
    def search(self, value):
        first = 0
        last = self.length - 1
        count = 0
        # True if the value is found in the list
        value_found = False
        # True if Value actually exists in the list
        value_is_in_list = False

        # index position of the the value in the list
        # if value is found on the list  set index
        try:
            index = self.index(value)
            value_is_in_list = True
        except ValueError:
            index = -1
            value_is_in_list = False

        # set mid_point and compare  with target value
        while first <= last and not value_found and value_is_in_list and value != self[last]:
            mid_point = (first + last) // 2
            mid_value = self[mid_point]
            if mid_value == value:
                value_found = True
                count += 1
                index = mid_point
            else:
                # Traverse down the list
                if value < mid_value:
                    last = mid_point - 1
                    count += 1
                # Traverse Up the list
                else:
                    first = mid_point + 1
                    count += 1

        return {"count": count, "index": index}
