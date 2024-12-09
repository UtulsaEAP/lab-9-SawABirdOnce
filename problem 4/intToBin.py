def int_to_reverse_binary(integer_value):
    binary_val = ''
    while integer_value > 0:
        binary_val += str(integer_value % 2) 
        integer_value = integer_value // 2   
    return binary_val

def string_reverse(input_string): 
    reverse_input = ''
    for char in input_string:
        reverse_input = char + reverse_input 
    return reverse_input

if __name__ == '__main__':
    user_input = int(input()) 
    binary_string = int_to_reverse_binary(user_input)
    binary_string = string_reverse(binary_string)
    print(binary_string)