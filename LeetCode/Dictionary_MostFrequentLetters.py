# Most frequent letters
# dict, lambda, sort
sentence = "this is a common interview question"
dic = {}
for i in range(len(sentence)):
    # if sentence[i] == " ":
    #     continue
    if sentence[i] in dic:
        dic[sentence[i]] += 1
    else:
        dic[sentence[i]] = 1

char_frequency_sorted = sorted(
    dic.items(),
    key=lambda x: x[1],
    reverse=True)
print(char_frequency_sorted[0])
