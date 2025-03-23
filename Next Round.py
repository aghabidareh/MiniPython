n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k - 1]
advancing = sum(1 for score in scores if score >= threshold and score > 0)
print(advancing)
