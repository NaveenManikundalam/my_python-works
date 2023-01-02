my_dic = {}
len_my_dic = int(input("Enter the length of the dictionary = "))

for i in range(len_my_dic):
    key = input(f"Enter the no.{i+1} key of the dictionary = ")
    val = input(f"Enter the no.{i+1} value of the dictionary = ")
    my_dic[key] = val

print(my_dic)

ele = input("Enter the key for which the value need to be searched = ")
print("Value for the entered key is ",my_dic[ele])





