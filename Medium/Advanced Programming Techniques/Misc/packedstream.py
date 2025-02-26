def omg_packed(original_string):
    packedstring = ""
    letter_counter = {}
    for i in original_string:
        if not i in letter_counter.keys():
            letter_counter[i] = 1
        else:
            letter_counter[i] += 1

    for i, k in letter_counter.items():
        packedstring += (str(i) + str(k))

    print(f'{"Not pack required, here´s the word it self: " + original_string if len(packedstring) >= len(original_string) else "Packed string: " + packedstring}')

omg_packed("whhhhaaaatttttt") 