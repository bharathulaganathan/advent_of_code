import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"
file_path = os.path.join(base_dir, file_name)

words =[]

with open(file_path, "r") as input:
    for row in input:
        words.append(row.strip())

nice = 0
bad_string = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]

for word in words:
    bad_present = False
    for bad in bad_string:
        if bad in word:
            bad_present = True
            break
    vowel = 0
    repeat = False
    for i in range(len(word)-1):
        if word[i] in vowels:
            vowel += 1
        if word[i] == word[i+1]:
            repeat = True
    if word[-1] in vowels:
        vowel += 1
    if not(bad_present) and repeat and vowel >= 3:
        nice += 1

print(nice)