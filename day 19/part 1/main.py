def can_afford_ore_robot(ore):
    return ore >= ore_robot_cost[0]


def can_afford_clay_robot(ore):
    return ore >= clay_robot_cost[0]


def can_afford_obsidian_robot(ore, clay):
    return ore >= obsidian_robot_cost[0] and clay >= obsidian_robot_cost[1]


def can_afford_geode_robot(ore, obsidian):
    return ore >= geode_robot_cost[0] and obsidian >= geode_robot_cost[2]


def solution(ore, clay, obsidian, geodes, time, ore_robots, clay_robots, obsidian_robots, geode_robots):
    geode_scores = [geodes]
    if time <= 0:
        return max(geode_scores)

    new_ore = ore + ore_robots
    new_clay = clay + clay_robots
    new_obsidian = obsidian + obsidian_robots
    new_geodes = geodes + geode_robots

    if can_afford_geode_robot(ore, obsidian) and time >= 1:
        geode_scores.append(solution(new_ore - geode_robot_cost[0], new_clay, new_obsidian - geode_robot_cost[2], new_geodes, time - 1, ore_robots, clay_robots, obsidian_robots, geode_robots + 1))
    if can_afford_obsidian_robot(ore, clay) and time >= 2 and not obsidian + time * obsidian_robots >= time * geode_robot_cost[2]:
        geode_scores.append(solution(new_ore - obsidian_robot_cost[0], new_clay - obsidian_robot_cost[1], new_obsidian, new_geodes, time - 1, ore_robots, clay_robots, obsidian_robots + 1, geode_robots))
    if can_afford_clay_robot(ore) and time >= 3 and not clay + time * clay_robots >= time * obsidian_robot_cost[1] and not can_afford_geode_robot(ore, obsidian) and (obsidian_robots <= 2 or not can_afford_obsidian_robot(ore, clay)):
        geode_scores.append(solution(new_ore - clay_robot_cost[0], new_clay, new_obsidian, new_geodes, time - 1, ore_robots, clay_robots + 1, obsidian_robots, geode_robots))
    if can_afford_ore_robot(ore) and time >= 2 and not ore + time * ore_robots >= max(clay_robot_cost[0], obsidian_robot_cost[0], geode_robot_cost[0]) * time and (clay_robots <= 2 or not can_afford_clay_robot(ore)):
        geode_scores.append(solution(new_ore - ore_robot_cost[0], new_clay, new_obsidian, new_geodes, time - 1, ore_robots + 1, clay_robots, obsidian_robots, geode_robots))
    if (not can_afford_ore_robot(ore) and ore_robots < max(clay_robot_cost[0], obsidian_robot_cost[0], geode_robot_cost[0])) \
        or (not can_afford_clay_robot(ore) and ore_robots > 1)\
            or (not can_afford_obsidian_robot(ore, clay) and clay_robots >= obsidian_robot_cost[1] // 3)\
            or (not can_afford_geode_robot(ore, obsidian) and obsidian_robots >= geode_robot_cost[2] // 3):
        geode_scores.append(solution(new_ore, new_clay, new_obsidian, new_geodes, time - 1, ore_robots, clay_robots, obsidian_robots, geode_robots))
    return max(geode_scores)


if __name__ == "__main__":

    quality_levels = []
    blueprint_id = 0
    ore_robot_cost = ()
    clay_robot_cost = ()
    obsidian_robot_cost = ()
    geode_robot_cost = ()

    f = open("input2.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        blueprint_id = int(line.split(" ")[1].split(":")[0])
        ore_robot_cost = (int(line.split(" ")[6]), 0, 0)
        clay_robot_cost = (int(line.split(" ")[12]), 0, 0)
        obsidian_robot_cost = (int(line.split(" ")[18]), int(line.split(" ")[21]), 0)
        geode_robot_cost = (int(line.split(" ")[27]), 0, int(line.split(" ")[30]))
        result = solution(0, 0, 0, 0, 24, 1, 0, 0, 0)
        quality_levels.append(result * blueprint_id)

    print(sum(quality_levels))
