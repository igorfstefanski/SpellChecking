def calculate_hamming_distance(first_string, second_string, common_mistakes):
    first_string_length = len(first_string)
    second_string_length = len(second_string)

    if(first_string_length != second_string_length):
        return -1

    distance = 0

    for character in range(first_string_length):
        if (first_string[character] != second_string[character]) and not (is_common_mistake(first_string[character], second_string[character], common_mistakes)):
            distance += 1

    return distance


def is_common_mistake(first_character, second_character, common_mistakes):
    if (first_character in common_mistakes) and (common_mistakes[first_character] == second_character):
        return True
    elif (second_character in common_mistakes) and (common_mistakes[second_character] == first_character):
        return True

    return False
