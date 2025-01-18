T = int(input())

for _ in range(T):
    floor = int(input())
    ho = int(input())
    people = [x for x in range(1,ho+1)]
    for _ in range(floor):
        for i in range(1, ho):
            people[i] += people[i-1]
    print(people[ho-1])