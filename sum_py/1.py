# Напишите программу для сокращения текстов по крайней мере наполовину.
#
# В файле fiction.txt записаны строки слов через пробел.
# В каждой строке нужно оставить первую половину слов
# (если их нечётное количество, то меньшую часть) и записать их в файл reduction.txt,
# предварительно расположив в алфавитном порядке. Слова в строках разделены пробелами.

with open('fiction.txt', 'r') as file:
    f = file.readlines()
wf = open('reduction.txt', 'w')

l = []
for st in f:
    s = st.split()
    n = 0
    for _ in s:
        n += 1

    if n % 2 == 0:
        b = n // 2
        rs = sorted(s[:b])
        rs = ' '.join(rs)
        rs += '\n'
        wf.write(rs)
    else:
        b = n // 2
        rs = sorted(s[:b])
        rs = ' '.join(rs)
        rs += '\n'
        wf.write(rs)
wf.close()
