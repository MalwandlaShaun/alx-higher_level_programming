def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0

    for letter in roman_string[::-1]:
        curr = roman_dict[letter]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr

    return result
