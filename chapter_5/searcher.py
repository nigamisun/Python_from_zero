class Sort_Search: 
    def __init__(self, data):
        self.data = sorted(list(data))

    def binary_search(self, target):
        low = 0
        high = len(self.data) - 1 
        while low <= high:
            mid = (low + high) // 2 
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
