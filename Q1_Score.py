student1 = input("請輸入第一位學生成績")
student2 = input("請輸入第二位學生成績")
student3 = input("請輸入第三位學生成績")
student4 = input("請輸入第四位學生成績")
student5 = input("請輸入第五位學生成績")

score_list = [int(student1), int(student2), int(student3), int(student4), int(student5)]
score_list_correct = []
for i in score_list:
#  如果一位數或三位數分數 老師不會看錯 老師只會看錯二位數的分數
 if i//10 != 1:
  score_list_correct.append(i)
 elif i//10 == 1:
  score_list_correct.append(i//10 + (i%10)*10)

print(score_list_correct)

