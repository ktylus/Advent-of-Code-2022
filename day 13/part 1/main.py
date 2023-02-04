def check_correctness(first, second):
    if first == "[" or first == "[]":
        return True
    if second == "[" or second == "[]":
        return False

    first_char = first[1]
    second_char = second[1]
    if first_char not in ["[", "]", ","]:
        j = 2
        while first[j] not in [",", "]"]:
            first_char += first[j]
            j += 1
    if second_char not in ["[", "]", ","]:
        j = 2
        while second[j] not in [",", "]"]:
            second_char += second[j]
            j += 1

    if first_char not in ["[", "]", ","] and second_char not in ["[", "]", ","]:
        if int(first_char) < int(second_char):
            return True
        elif int(second_char) < int(first_char):
            return False
        else:
            return check_correctness("[" + first[3::], "[" + second[3::])
    elif first_char == "[" and second_char != "[":
        return check_correctness(first, "[[" + second_char + "]" + second[len(second_char) + 1::])
    elif first_char != "[" and second_char == "[":
        return check_correctness("[[" + first_char + "]" + first[len(first_char) + 1::], second)
    elif first_char == "[" and second_char == "[":
        first_list = ""
        second_list = ""
        first_par_count = 0
        second_par_count = 0
        for k in range(1, len(first) - 1):
            first_list += first[k]
            if first[k] == "[":
                first_par_count += 1
            if first[k] == "]":
                first_par_count -= 1
            if first_par_count == 0:
                break
        for k in range(1, len(second) - 1):
            second_list += second[k]
            if second[k] == "[":
                second_par_count += 1
            if second[k] == "]":
                second_par_count -= 1
            if second_par_count == 0:
                break

        if check_correctness(first_list, second_list) == check_correctness(second_list, first_list):
            return check_correctness("[" + first[len(first_list) + 2::], "[" + second[len(second_list) + 2::])
        else:
            return check_correctness(first_list, second_list)
    else:
        return False



if __name__ == "__main__":
    f = open("input.txt", "r")
    first_packet = []
    second_packet = []
    packets = []

    count = 1
    for line in f:
        line = line.replace("\n", "")
        if count == 1:
            first_packet.append(line)
            packets.append(line)
        elif count == 2:
            second_packet.append(line)
            packets.append(line)
        else:
            count = 0
        count += 1

    index_sum = 0
    for i in range(len(first_packet)):
        if check_correctness(first_packet[i], second_packet[i]):
            index_sum += 1 + i
    print(index_sum)