score = [3,54,6,23,4,65]
s = [score[i] for i in range(len(score))]
s.sort(reverse=True)
dict1 = {}
for i in range(len(s)):
    dict1[s[i]] = i+1
for i in range(len(score)):
    if dict1[score[i]] == 1:
        score[i] = "Gold Medal"
    elif dict1[score[i]] == 2:
        score[i] = "Silver Medal"
    elif dict1[score[i]] == 3:
        score[i] = "Bronze Medal"
    else:
        score[i] = str(dict1[score[i]])

print(score)

