def render_pixel(cycle, register):
    sprite = [register - 1, register, register + 1]
    if((cycle - 1) % 40 in sprite):
        print("#", end="")
    else:
        print(".", end="")
    if(cycle in [40,80,120,160,200,240]):
        print()


if __name__ == "__main__":
    f = open("input.txt", "r")

    cycle = 1
    register = 1
    for line in f:
        command = line.replace("\n", "").split(" ")
        if command[0] == "noop":
            render_pixel(cycle, register)
            cycle += 1
        else: # addx n
            for i in range(2):
                render_pixel(cycle, register)
                cycle += 1
                if i == 1:
                    register += int(command[1])
