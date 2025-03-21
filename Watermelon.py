def can_divide_watermelon(w):
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"


w = int(input())
print(can_divide_watermelon(w))