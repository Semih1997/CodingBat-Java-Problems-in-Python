def copyEvens(a,b):
    even_list = []
    i = 0
    adding_shit = 0
    while adding_shit < b:
        if a[i] % 2 == 0:
            even_list.append(a[i])
            i += 1
            adding_shit += 1
        else:
            i += 1
    return even_list
test_inputs = [[3, 2, 4, 5, 8],[3, 2, 4, 5, 8],[6, 1, 2, 4, 5, 8],[6, 1, 2, 4, 5, 8],[3, 1, 4, 1, 5],[2],[6, 2, 4, 8],[1, 8, 4],[1, 8, 4],[6, 2, 4, 8]]
other_test_inputs = [2,3,3,4,1,1,2,1,2,4]
expected = [[2, 4],[2, 4, 8],[6, 2, 4],[6, 2, 4, 8],[4],[2],[6,2],[8],[8,4],[6, 2, 4, 8]]
all_correct = True
for i in range(len(expected)):
    if copyEvens(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],copyEvens(test_inputs[i],other_test_inputs[i]),i)
        all_correct = False
print("All Correct: ", all_correct)