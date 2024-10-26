def flatten(array):
    arr = []
    for item in array:
        if type(item) is list:
            arr.extend(flatten(item))
        else:
            arr.append(item)
    return arr


arr = ['list', ['list inside list'], ['another list', 'other list']]
print(flatten(arr)) #['list', 'list inside list', 'another list', 'other list']
