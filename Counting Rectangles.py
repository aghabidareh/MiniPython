target = 2_000_000
closest_diff = float('inf')
best_m, best_n = 0, 0

for m in range(1, 100):
    rect_m = (m * (m + 1)) // 2

    n_estimate = int(((8 * target / rect_m + 1) ** 0.5 - 1) / 2)

    for n in [n_estimate, n_estimate + 1]:
        rect_n = (n * (n + 1)) // 2
        rect_count = (rect_m * rect_n)

        diff = abs(rect_count - target)
        if diff < closest_diff:
            closest_diff = diff
            best_m, best_n = m, n

best_area = best_m * best_n
print(best_area)
