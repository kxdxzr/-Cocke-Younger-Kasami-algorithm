def make_list(test_strings):
    counter = 0
    while counter < len(test_strings):
        buf_list = list(test_strings[counter])
        test_strings[counter] = buf_list
        counter += 1
    return test_strings
