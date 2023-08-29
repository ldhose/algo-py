def test_selection_sort():
    elements = [3,3,2, 5,1,7,9, 8]
    print(selection_sort(elements))
    print(selection_sort_book(elements))

def selection_sort(elements):
    smallest = elements[0]
    for i in range(0, len(elements)):
        for j in range(i, len(elements)):
            if(elements[i] > elements[j]):
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    return elements

def selection_sort_book(elems):
    new_arr = []
    for i in range(len(elems)):
        smallest = smallest_elem_index(elems);
        new_arr.append(elems.pop(smallest))
    return new_arr    

def smallest_elem_index(elements):
    smallest = elements[0]
    smallest_index = 0
    for i in range(1, len(elements)):
        if(elements[i]< smallest):
            smallest = elements[i]
            smallest_index = i
    return smallest_index                    
