def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero = one = 0
    prev = None
    for ch in string:
        if ch != prev:
            if ch == "0":
                zero += 1
            else:
                one += 1
            prev = ch
    return min(zero, one)


string = input()
result = find_count_to_turn_out_to_all_zero_or_all_one(string)
print(result)

