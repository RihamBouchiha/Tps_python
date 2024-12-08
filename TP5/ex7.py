def min_max(data):
    if data:
        return (min(data), max(data))
    return None

tuple = (1, 2, 3, 4, 5)
print(min_max(tuple))  
