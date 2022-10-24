def plusout1(a, b):
    new_a = ""
    i = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            new_a += b
            i += len(b)
        else:
            new_a += '+'
            i += 1
    return new_a

test_inputs = ["12xy34","12xy34","12xy34xyabcxy","abXYabcXYZ","abXYabcXYZ","abXYabcXYZ","abXYxyzXYZ"]
other_test_inputs = ["xy","1","xy","ab","abc","XY","XYZ"]
expected = ["++xy++","1+++++","++xy++xy+++xy","ab++ab++++","++++abc+++","++XY+++XY+","+++++++XYZ"]
all_correct = True
for i in range(len(expected)):
    if plusout1(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i], plusout1(test_inputs[i],other_test_inputs[i]),i)
        all_correct = False
print("All Correct: ", all_correct)