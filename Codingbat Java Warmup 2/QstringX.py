def stringX(a):
    if len(a) < 3:
        return a
    else:
        start_end = a[1:len(a)-1]
        final_a = a[0] + start_end.replace("x","") + a[len(a)-1]
        return final_a
test_inputs = ["xxHxix","abxxxcd","xabxxxcdx","xKittenx","Hello","xx","x",""]
expected = ["xHix","abcd","xabcdx","xKittenx","Hello","xx","x",""]
all_correct = True
for i in range(len(expected)):
    if stringX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)