# my_dict1 = {}
# my_dict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# my_key = sorted(my_dict, key=my_dict.get, reverse=True) [:3]
# my_velu = sorted(my_dict.values(), reverse=True)[:3]
# for i,x in zip(my_key,my_velu):
#     my_dict1.setdefault(i,x)
# print(my_dict1)    


# s = 'a,2,b,5,c,8,a,4,e,11'
# s1 = s.split(',')
# tarer = []
# tver = []
# res = {}

# for i in s1:
#     if i.isdigit:
#         tver.append(int(i))
#     else:
#         tarer.append(i)
# print(tarer,tver)         
# a = 'a, 2, b, 5, c, 8, a, 4, e, 11'
# a = a.split(', ')
# mydict = {}
# char_list = []
# num_list = []
# new_num_list = []
# new_char_list = []
# for i in a:
#       if i.isdigit():
#             num_list.append(int(i))
#       else:
#             char_list.append(i)
# for i in char_list:
#       if i not in new_char_list:
#             new_char_list.append(i)
# for i in range(0, len(new_char_list)):
#       Sum = 0
#       indexs = []       
#       for u in range(0, len(char_list)):
#             if new_char_list[i] == char_list[u]:
#                   indexs.append(u)
#       for number in indexs:
#             Sum += num_list[number]
#       new_num_list.append(Sum)
# for x, y in zip(new_char_list, new_num_list):
#       mydict.setdefault(x,y)
# print(mydict)   


# def my_fuc(x):
#     if x == 1:
#         return 1    
#     else:
#         return x * my_fuc(x-1) 
# print(my_fuc(6)) 




# def my_func(x):
#     if x in (1,2):
#         return 1
#     return my_func(x-1) + my_func(x -2)    
# print(my_func(40))

# def kalkulator(a,b,gort):
#     if gort == '*':
#         return a*b
#     elif gort == '-':
#         return a-b
#     elif gort == '+':
#         return a + b
#     elif gort == '/':
#         return a / b 
# a = int(input('number1--'))
# gort = input('mutqagreq gortoxutyun') 
# b = int(input('number2---'))
# print(kalkulator(a,b,gort))



# def fib(x):
#     if x == 1:
#         return 0
#     elif x in (1,2):
#         return 1      
#     else:
#         return fib(x-1) + fib(x-2)
# x = int(input('mutqagreq tiv---'))            
# print(fib(x)) 



