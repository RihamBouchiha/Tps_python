def position_element(tuple, ele):
    try:
        return tuple.index(ele)
    except ValueError:
        return -1

tuple_example = (1, 2, 3, 4, 5)
print(position_element(tuple_example, 3))  
