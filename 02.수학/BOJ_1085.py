# BOJ 1085 직사각형에서 탈출

# 한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 x, y, w, h가 주어진다.
# 첫째 줄에 문제의 정답을 출력한다.

import sys

x,y,w,h = map(int, sys.stdin.readline().split())

w_min = min(x, w-x)
h_min = min(y, h-y)

result = min(w_min, h_min)
print(result)