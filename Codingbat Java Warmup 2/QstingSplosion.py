def stringSplosion(a):
    if len(a) <= 1:
        return a
    elif len(a) > 1 :
        last = ""
        for x in range(len(a) + 1):#        a = a[:1] + a[:2] + a[:3] + a
            last = last + a[:x]
        return last
test_inputs = ["Code","abc","ab","x","fade","There","Kitten","Bye","Good","Bad"]
expected = ["CCoCodCode","aababc","aab","x","ffafadfade","TThTheTherThere","KKiKitKittKitteKitten","BByBye","GGoGooGood","BBaBad"]
all_correct = True
for i in range(len(expected)):
    if stringSplosion(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(stringSplosion(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)