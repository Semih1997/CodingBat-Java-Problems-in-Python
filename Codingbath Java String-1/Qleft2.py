def left2(a):
    a = a[2:] + a[0:2]
    return a
test_inputs = ["Hello","java","Hi","code","cat","12345","Chocolate","bricks"]
expected = ["lloHe","vaja","Hi","deco","tca","34512","ocolateCh","icksbr"]
all_correct = True
for i in range(len(expected)):
    if left2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)