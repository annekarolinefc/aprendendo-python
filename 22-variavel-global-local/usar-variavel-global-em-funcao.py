x = 10
print(x) #10

def global_sum(y):
    global x 
    x = 15
    return x + y

print(x) #10
print(global_sum(20)) #35
print(x) #15