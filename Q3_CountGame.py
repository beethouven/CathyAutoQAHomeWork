def generate_list(number):
 number_list = []
 for i in range(number):
  number_list.append(i+1)
 return number_list

def count_left_number(number_list,divide):
 remove_number = len(number_list)//divide
 left_number = len(number_list)%divide
 delete_list = []
 for i in range(remove_number):
  delete_list.append((i+1)*divide-1)
 for i in reversed(delete_list):
  number_list.pop(i)
 while number_list[0]=='a':
  number_list.remove('a')
 if len(number_list)==1:
  return number_list
 elif len(number_list)>1:
  for i in range(left_number):
   number_list.insert(0,'a')
  return number_list

def answar(number_list,divide):
 while len(number_list)>1:
  number_list = count_left_number(number_list,divide)
 return str(number_list[0])


input_number = input('請輸入n值(0-100)')

if(int(input_number)==0):
 print('無人參加')
elif(int(input_number)):
 print('總人數為'+input_number+'人' ) 
 print('第'+answar(generate_list(int(input_number)),3)+'順位')