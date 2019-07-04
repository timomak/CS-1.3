def flip_vertical_axis(matrix):
    temp = []
    for array in matrix:
        temp_array = array[::-1]
        temp.append(temp_array)
    return temp

print(flip_vertical_axis([[0,0,1], [1,2,3]]))
# test = [0,1,2,3,4]
# array = test[::-1]
# print(array)
