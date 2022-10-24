def sameEnds(a):
    i = 0
    new_a = ""
    while i < len(a)//2:
        if len(a) % 2 == 0:
            if a[len(a)//2+i:len(a)] == a[:len(a)//2-i]:
                new_a = a[:len(a)//2-i]
                break
            else:
                i += 1
        elif len(a) % 2 == 1:
            if a[len(a)//2+i+1:len(a)] == a[:len(a)//2-i]:
                new_a = a[:len(a)//2-i]
                break
            else:
                i += 1
    return new_a
test_inputs = ["abXYab","xx","xxx","xxxx","javaXYZjava","javajava","xavaXYZjava","Hello! and Hello!","x","","abcb","mymmy"]
expected = ["ab","x","x","xx","java","java","","Hello!","","","","my"]
all_correct = True
for i in range(len(expected)):
    if sameEnds(test_inputs[i]) != expected[i]:
        print(test_inputs[i],sameEnds(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)