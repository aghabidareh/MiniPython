def minimum_steps_to_friend(step):
    full_steps = step // 5
    remainder = step % 5
    if remainder > 0:
        return full_steps + 1
    return full_steps

step = int(input().strip())
print(minimum_steps_to_friend(step))