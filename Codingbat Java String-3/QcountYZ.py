def countYZ(a):
    count_YZ = 0
    i = 0
    a = a.lower()   # büyük küçük harf fark etmiyor ondan kontrol edebilmek için hepsini küçük harf olarak kontrol ediyoruz.
    while i < len(a):
        if len(a) > 0 and a[i].isalpha() == False and (a[i-1] == "y" or a[i-1] == "z"):     #.isalpha() eğer karakter harfse True çıkar değilse False.
            count_YZ += 1
            i += 1
        else:
            i += 1
    if a[len(a)-1] == "y" or a[len(a)-1] == "z":
        count_YZ += 1
    return count_YZ
test_inputs = ["fez day","day fez","day fyyyz","day yak","day:yak","!!day--yaz!!","yak zak","DAY abc XYZ","aaz yyz my","y2bz","zxyx"]
expected = [2,2,2,1,1,2,0,2,3,2,0]
all_correct = True
for i in range(len(expected)):
    if countYZ(test_inputs[i]) != expected[i]:
        print(test_inputs[i],countYZ(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)