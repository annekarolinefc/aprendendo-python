with open('arquivo.txt') as f:
    content = f.readlines()
    print(content)

#removendo o \n
content = [x.strip('\n') for x in content]    
print(content)

# percorrendo o array
for line in content:
    print(line)