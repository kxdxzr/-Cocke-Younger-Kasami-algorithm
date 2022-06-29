def check_not_exists(array,exam_string):
    for cur in array:
        if cur == exam_string:
            return False
    return True
