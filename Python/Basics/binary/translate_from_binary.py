"""
Converts binary string to text.
"""
def translate(input):
    binary_string = input.replace(" ", "").replace("\n", "")
    if binary_string_valid(binary_string):
        binary_string_list = split_binary_to_list(binary_string)
        print(binary_string_list)
        return get_text_from_binary(binary_string_list)
    else:
        return "Invalid Binary String"

def binary_string_valid(binary_string):
    for char in binary_string:
        if char != '0' and char != '1':
            return False

    # Append missing zeros at the begining of a string.
    missing_zeros = 8 - len(binary_string) % 8
    binary_string = '0'*missing_zeros + binary_string
    return True


def split_binary_to_list(binary_strings):
    n = 8
    binary_strings = [binary_strings[i:i+n]
                      for i in range(0, len(binary_strings), n)]
    return binary_strings


def get_text_from_binary(binary_strings):
    # 01000001 -> 65 -> 'A'
    text = ""
    for b_str in binary_strings:
        text += binary_to_str(b_str)
    return text


def binary_to_str(b_str):
    power = 7
    base = 2
    dec = 0
    
    for i in range(0, len(b_str)):
        # print("================")
        bit = int(b_str[i])
        dec += base**power*bit
        # print(base**power*bit)
        power -= 1
    print(f"Binary:{b_str} = [{dec}] = [{chr(dec)}]")
    return chr(dec)



