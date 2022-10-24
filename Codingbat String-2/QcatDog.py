def catDog(a):
    count_dog = 0
    count_cat = 0
    control = False
    for x in range(len(a)-2):
        if a[x:x+3] == "dog":
            count_dog += 1
        if a[x:x+3] == "cat":
            count_cat += 1
    if count_cat == count_dog:
        control = True
    return control
test_inputs = ["catdog","catcat","1cat1cadodog","catxxdogxxxdog","catxdogxdogxcat","catxdogxdogxca","dogdogcat","dogogcat","dog","cat","ca","c",""]
expected = [True,False,True,False,True,False,False,True,False,False,True,True,True]
all_correct = True
for i in range(len(expected)):
    if catDog(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)