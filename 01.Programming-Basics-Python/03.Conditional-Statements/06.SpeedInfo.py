num = float(input())

if num <= 10:
    print("slow")
elif num <= 50:
    print("average")
elif num <= 150:
    print("fast")
elif num <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
