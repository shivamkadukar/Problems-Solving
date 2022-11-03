def sort_list_of_dictionary(input_list, key):
    for i in range(len(input_list)):
        for j in range(len(input_list)-i-1):
            if input_list[j][key] > input_list[j+1][key]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j] 

    return input_list