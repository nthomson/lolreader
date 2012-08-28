def camalcase_to_pythonic(word):
    char_list = list(word)
    for counter, c in enumerate(char_list):
        if(c.isupper()):
            char_list.insert(counter, '_')
            if char_list[counter + 1]:
                char_list[counter + 1] = char_list[counter + 1].lower()

    return ''.join(char_list)
