def listToString(s):
    str1 = " "
    return str1.join(s)


with open("/PycharmProjects/#100daysofcode/24(Mail_Merge)/Input/Names/invited_names.txt", "r") as names:
    for i1 in names:
        i2 = i1.rstrip("\n")
        with open("/PycharmProjects/#100daysofcode/24(Mail_Merge)/Input/Letters/starting_letter.txt", "r") as letter:
            letters = letter.readlines()
            new_name = letters[0].replace("[name]", i2)
            letters[0] = new_name
            letter_to_send = listToString(letters)
            with open(f"/PycharmProjects/#100daysofcode/24(Mail_Merge)/Output/ReadyToSend/letter_to_{i2}", "w") as send_letter:
                send_letter.write(letter_to_send)
