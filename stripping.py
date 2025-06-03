#sarah verburg 06-03

filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'Twas"
# apost = first.strip(chars)
# print(apost)

for ch in first:
    if ch in chars:
        print("Removing ", ch)
    else:
        break

print("-" * 40)

for ch in first[::-1]:
    if ch in chars:
        print("Removing ", ch)
    else:
      break

print("-" * 40)

twa_removed = first.removeprefix("'Twas")
print(twa_removed)
tove_removed = first.removesuffix("toves")
print(tove_removed)
