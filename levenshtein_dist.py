def calculate_leven_distance(first_string, second_string, common_mistakes):
    no_columns = len(second_string) + 1
    no_rows = len(first_string) + 1
    leven_matrix = prepare_leven_matrix(no_columns, no_rows)

    for column in range(1, no_columns):
        for row in range(1, no_rows):
            if (first_string[row - 1] == second_string[column - 1]) or (is_common_mistake(first_string[row - 1], second_string[column - 1], common_mistakes)):
                cost = 0
            else:
                cost = 1

            leven_matrix[row][column] = min(leven_matrix[row - 1][column] + 1,
                                            leven_matrix[row][column - 1] + 1,
                                            leven_matrix[row - 1][column - 1] + cost)

    return leven_matrix[no_rows - 1][no_columns - 1]


def prepare_leven_matrix(no_columns, no_rows):
    matrix = [[0 for x in range(no_columns)] for y in range(no_rows)]

    for i in range(1, no_columns):
        matrix[0][i] = i
    for j in range(1, no_rows):
        matrix[j][0] = j

    return matrix


def is_common_mistake(first_character, second_character, common_mistakes):
    if (first_character in common_mistakes) and (common_mistakes[first_character] == second_character):
        return True
    elif (second_character in common_mistakes) and (common_mistakes[second_character] == first_character):
        return True

    return False
