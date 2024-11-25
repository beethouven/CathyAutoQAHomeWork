def count_letter(word):
 word = word.upper().replace(' ','')
 word_list = list(word)
 word_list.sort()
 count_list = []
 while len(word_list)>0 :
  count_list.append([word_list[0],word_list.count(word_list[0])])
  del word_list[0:word_list.count(word_list[0])]
 return count_list

def print_result(count_list):
 for i in count_list:
  print(i[0]+' '+str(i[1]))

Cathy60th = "Hello welcome to Cathay 60th year anniversary"
print_result(count_letter(Cathy60th))

