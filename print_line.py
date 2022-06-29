def print_oneline(array):
    length = len(array)
    counter = 0
    while counter < length-1:
        print(array[counter],end=",")
        counter += 1
    print(array[counter])

def print_lines(array):
    for cur in array:
        print(cur)

def print_noco_line(array): #no ,
    length = len(array)
    counter = 0
    while counter < length-1:
        print(array[counter],end="")
        counter += 1
    print(array[counter])
