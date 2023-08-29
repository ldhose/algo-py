
def assert_binary_search():
    print(binary_search([1,5],2))
    assert binary_search([1],2) == "Element not found"
    assert binary_search([1],1) == "Element found"


def binary_search_book(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

def binary_search(sorted_array, elem):
    start = 0
    end = int(len(sorted_array))-1
    mid = int(end/2)
    while(end >= start):
        if elem == sorted_array[mid]:
            return "Element found"
        elif elem > sorted_array[mid]:
            start = mid+1
            mid = int((start + end)/2)
        else:
            end = mid-1
            mid = int((end + start) /2 )    

    return "Element not found"