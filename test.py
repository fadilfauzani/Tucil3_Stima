# listpenelurusan =[]
# inp = [1,2,3,4,5]
# listpenelurusan.append(inp)
# inp = [2,3,4,5,1]
# print(listpenelurusan)
# listpenelurusan.append(inp)
# print(listpenelurusan)
customers = []
customers.append((2, "Harry")) #no sort needed here because 1 item. 
customers.append((3, "Charles"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((1, "Riya"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((4, "Stacy"))
customers.sort(reverse=True)
while customers:
     print(customers.pop(0)[1])
print(set([1,1]))