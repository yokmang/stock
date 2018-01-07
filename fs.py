#!/usr/local/bin/python3
from fs_naver import *
from fs_sejong import *
import matplotlib.pyplot as plt

#print("기업명 기업코드 현재가 발행주식수 당좌비율(%)")
#print(get_profile_naver("002460"))

#print(get_fin_table_sejong_data("002460","a"))
#print(get_fin_table_sejong_data("002460", "a"))
#DataFrame 접근방법...
#바꿔보자

table = get_fin_table_sejong_data("002460","a")


#print (table.index)
#print (table.columns)

#print(type(table.index))
#print(table.index[1:])
table[0][0] = "date"
for i in table.index[1:]:
    table[0][i] = table[0][i].split(" ")[0]
    #print(table[0][i])

#print (table)


#print(table.ix[0])

#print(table.info())
plt.plot(table[0][1:],table[1][1:])
plt.show()


#print (table[0]) #연도
#print (table[1])  #매출액
#print (table[2])  #영업이익
#print (table[3])  #순이익
#print (table[4])  #연결순이익
#print (table[5])  #자산총계
#print (table[6])  #부채총계
#print (table[7])  #자본총계
