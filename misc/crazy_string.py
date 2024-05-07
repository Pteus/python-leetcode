def uppercase_every_other_char(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i]
    return result


# Example usage:
input_string = "hello world"
output_string = uppercase_every_other_char(input_string)
print(output_string)
