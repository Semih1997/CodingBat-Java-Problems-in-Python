def hasOne(a):
    # // 10 son rakamdan kurtulur
    # % yi de kalanı almak için for içinde ikisini birlikte kullancaz
    has_one = False
    while a > 0:
        control = 0
        control = a % 10
        if control == 1:
            has_one = True
        a = a // 10
    return has_one
test_inputs = [10,220,22,212,1,9,211112,121121,222222,56156,56856]
expected = [True,False,False,True,True,False,True,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if hasOne(test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)