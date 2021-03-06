# BOJ 1181 단어정렬

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1.길이가 짧은 것부터
# 2.길이가 같으면 사전 순으로

# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 주어지는 문자열의 길이는 50을 넘지 않는다.

# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

import sys

word_list = []
for _ in range(int(input())):
    word_list.append(str(input()))

word_list = set(word_list)      #중복제거
sorted_list = []
for word in word_list:
    sorted_list.append([word, len(word)])
sorted_list.sort(key=lambda word : [word[1], word[0]])  #정렬
for word in sorted_list:
    print(word[0])

