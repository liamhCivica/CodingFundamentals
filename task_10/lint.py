'''count function '''
def count(sequence, item):
    '''function to get number of items in array'''
    number = 0
    for index in sequence:
        if index == item:
            number += 1
    return number
