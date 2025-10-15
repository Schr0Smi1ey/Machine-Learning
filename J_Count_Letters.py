s = input()
dict = {}
for char in s:
    if char not in dict:
        dict[char] = 0
    dict[char] += 1
for k,v in sorted(dict.items()):
    print(f"{k} : {v}")
