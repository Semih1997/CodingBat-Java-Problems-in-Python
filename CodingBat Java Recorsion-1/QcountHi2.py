def countHi2(a):
    if len(a) <= 1:
        return 0
    elif a[0:2] == "hi":
        return 1 + countHi2(a[1:])
    elif a[0] == "x":
        return countHi2(a[2:])
    else:
        return countHi2(a[1:])
test_inputs = ["ahixhi","ahibhi","xhixhi","hixhi","hixhhi","hihihi","hihihix","h","x",""]
expected = [1,2,0,1,2,3,3,0,0,0]
all_correct = True
for i in range(len(expected)):
    if countHi2(test_inputs[i]) != expected[i]:
        print(test_inputs[i],countHi2(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)