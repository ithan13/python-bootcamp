tracker = {
    "Sabrina" : 7400,
    "Rumi" : 7200,
}

for _ in range(3):
    runner_name = input("Enter Name: ")
    runner_time = int(input("Enter Time: "))
    if runner_name not in tracker:
        tracker[runner_name] = runner_time
    elif runner_time < tracker[runner_name]:
        tracker[runner_name] = runner_time

print(tracker)


