import hamming_dist as hamming
import indel_dist as indel
import levenshtein_dist as leven


def main():
    common_mistakes = {"o": "p",
                       "n": "m",
                       "d": "f",
                       "r": "t",
                       "z": "x"}

    choice = '0'
    print("Which operation?")
    print("1. Input from keyboard")
    print("2. Input from file")

    while choice == '0':
        choice = input("Your choice: ")

        if choice == '1':
            word_input(common_mistakes)
        elif choice == '2':
            file_input(common_mistakes)
        else:
            print("Wrong choice!")
            choice = '0'


def word_input(common_mistakes):
    given_string = input("Insert word: ")
    print("Searching for correct word...")
    correct_string = find_correct_string(given_string, common_mistakes)

    print("Did you mean " + correct_string + "?")


def file_input(common_mistakes):
    words_input = open("words_input.txt", "r")
    words_input_read = words_input.read()
    words_correct = open("words_input_corrected.txt", "w")

    print("Checking the file...")

    for given_string in words_input_read.split():
        correct_string = find_correct_string(given_string, common_mistakes)
        words_correct.write(correct_string + " ")

    words_input.close()
    words_correct.close()
    print("Corrected file has been created")


def find_correct_string(given_string, common_mistakes):
    correct_word = ""
    min_hamming = 1000
    min_indel = 1000
    min_leven = 1000

    words_bank = open("words_alpha.txt", "r")

    for line in words_bank:
        line = line.rstrip('\n')

        hamming_dist = hamming.calculate_hamming_distance(given_string, line,
                                                          common_mistakes)
        indel_dist = indel.calculate_indel_distance(given_string, line,
                                                    common_mistakes)
        leven_dist = leven.calculate_leven_distance(given_string, line,
                                                    common_mistakes)

        if hamming_dist >= 0:
            if (hamming_dist < min_hamming) and (leven_dist <= min_leven) and \
               (indel_dist <= min_indel):
                min_hamming = hamming_dist
                min_indel = indel_dist
                min_leven = leven_dist
                correct_word = line

    words_bank.close()
    return correct_word


if __name__ == "__main__":
    main()
