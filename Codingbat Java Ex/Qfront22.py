def front22(a):
    if len(a) >= 3:
        a = str(a)
        a = a[:2] + a + a[:2]
    elif len(a) < 3:
        a = str(a)
        a = a[:len(a)] + a + a[:len(a)]
    elif len(a) == 0:
        a = str(a)
    return a
test_inputs = ["kitten","Ha","abc","ab","a","","Logic"]
expected = ["kikittenki","HaHaHa","ababcab","ababab","aaa","","LoLogicLo"]
all_correct = True
for i in range(len(expected)):
    if front22(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)