f = open("test.txt")
content = f.read()

elf_cals = content.split('\n\n')
# print(elf_cals)

max_cals = 0
top_three = [0] * 3

for i in elf_cals:
    lines=i.split('\n')
    total_cals = 0
    for j in lines:
        if (j) != '':
            total_cals += int(j)
    max_cals = max(max_cals,total_cals)
    if max_cals > max(top_three):
        min_index = top_three.index(min(top_three))
        top_three.pop(min_index)
        top_three.insert(1,max_cals)

total_three = sum(top_three)

print("max calories of one: ",max_cals)
print("total of top three: ",total_three)
