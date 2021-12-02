def advent_of_code_1(input):
    answer = 0
    input = input.split()
    for counter, i in enumerate(input[4:], start=1):
        if int(i) > int(input[counter]):
            answer += 1
    print(answer)

def advent_of_code_day_2(input):
    test_list = input.split("\n")
    forward, aim, depth = 0,0,0
    for i in test_list:
        direction, value = i.split()
        match direction:
            case "forward":
                forward += int(value)
                depth += aim*int(value)
            case "up":
                aim -= int(value)
            case "down":
                aim += int(value)
    print(forward,aim,depth, forward*depth)
