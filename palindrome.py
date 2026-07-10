list = [1,2,3,2,1]
cpy = list.copy()
list.reverse()
if(list == cpy):
    print("The list is a palindrome")   
else:
    print("The list is not a palindrome")