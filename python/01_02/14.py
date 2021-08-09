num_list = []
for i in range(3):
    num_list.append(int(input()))
    
num_list[0]*num_list[1]*num_list[2]
print(num_list.index(max(num_list))+1)