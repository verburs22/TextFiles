#sarah verburg 06-03

# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#
# jabber.close()

# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
#
# for line in reversed(lines):
#     print(line, end='')

# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()

# for ch in reversed(text):
#     print(ch, end='')

# with open('Jabberwocky.txt') as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
# print("-"*40)

with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for i in jabber:
        print(i.rstrip())
