def transform_to_array_s1(string):
    array = []
    for s in string:
        array.append(s)
    return array


def transform_to_array_s2(string):
    array = []
    for s in string:
        array.append([s, 1])
    return array


def two_arrays(str1, str2):
    for i in range(len(str1)):
        flag = 0
        for j in range(len(str2)):
            if ord(str1[i]) == ord(str2[j][0]) and str2[j][1] == 1:
                str2[j][1] = 0
                flag = 1
                break
        if flag == 0:
            return False
    return True


def test_1():
    s1_example_1 = transform_to_array_s1("hi,man")
    s2_example_1 = transform_to_array_s2("man,hi")
    if two_arrays(s1_example_1, s2_example_1) is True:
        return "Correct"
    else:
        return "Incorrect"


def test_2():
    s1_example_1 = transform_to_array_s1("aa")
    s2_example_1 = transform_to_array_s2("aab")
    if two_arrays(s1_example_1, s2_example_1) is True:
        return "Correct"
    else:
        return "Incorrect"


def test_3():
    s1_example_1 = transform_to_array_s1("aA")
    s2_example_1 = transform_to_array_s2("bB")
    if two_arrays(s1_example_1, s2_example_1) is False:
        return "Correct"
    else:
        return "Incorrect"


s1 = transform_to_array_s1(input("s1: "))
s2 = transform_to_array_s2(input("s2: "))

print(two_arrays(s1, s2))

# print("==========\nTest 1: ", test_1())
# print("==========\nTest 2: ", test_2())
# print("==========\nTest 3: ", test_3())
