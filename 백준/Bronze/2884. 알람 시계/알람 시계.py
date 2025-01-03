import sys
input = sys.stdin.readline
hour, minute = list(map(int, input().split()))

if minute <45:
    namuzi = 45 - minute
    minute = 60 - namuzi
    if hour == 0:
        hour = 24
    hour -= 1
    print(hour, minute)
else:
    minute -= 45
    print(hour, minute)