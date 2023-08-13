import re

GENERAL_NUMBERS = {
    '0': 'ნული',
    '1': 'ერთი',
    '2': 'ორი',
    '3': 'სამი',
    '4': 'ოთხი',
    '5': 'ხუთი',
    '6': 'ექვსი',
    '7': 'შვიდი',
    '8': 'რვა',
    '9': 'ცხრა'
}

SIMPLE_TENS = {
    '1': 'ათი',
    '2': 'ოცი',
    '4': 'ორმოცი',
    '6': 'სამოცი',
    '8': 'ოთხმოცი',
    '10': 'ასი'
}

DOZEN_STARTERS = {
    '1': '',
    '2': 'ოცდა',
    '3': 'ოცდა',
    '4': 'ორმოცდა',
    '5': 'ორმოცდა',
    '6': 'სამოცდა',
    '7': 'სამოცდა',
    '8': 'ოთხმოცდა',
    '9': 'ოთხმოცდა'
}

TENS_NUMBERS = {
    '0': 'ათი',
    '1': 'თერთმეტი',
    '2': 'თორმეტი',
    '3': 'ცამეტი',
    '4': 'თოთხმეტი',
    '5': 'თხუთმეტი',
    '6': 'თექვსმეტი',
    '7': 'ჩვიდმეტი',
    '8': 'თვრამეტი',
    '9': 'ცხრამეტი'
}

TENS = [
    '1', '3', '5', '7', '9'
]

HUNDREDS = {
    '1': 'ას',
    '2': 'ორას',
    '3': 'სამას',
    '4': 'ოთხას',
    '5': 'ხუთას',
    '6': 'ექვსას',
    '7': 'შვიდას',
    '8': 'რვაას',
    '9': 'ცხრაას'
}

def numbers_converter(number):
    # Converts numbers to Georgian language up to 4 digits

    digits = [str(digit) for digit in str(number)]
    
    first = ''
    second = ''
    result = ''
    if len(digits) == 4:
        if digits[0] != '0':
            if digits[1] == '0':
                if digits[2] != '0' :
                    if digits[3] != '0':
                        if digits[0] == '1':
                            if digits[2] in TENS:
                                result = 'ათას' + ' ' + DOZEN_STARTERS[digits[2]] + TENS_NUMBERS[digits[3]]
                            else:
                                result = 'ათას' + ' ' + DOZEN_STARTERS[digits[2]] + GENERAL_NUMBERS[digits[3]]
                        else:   
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + DOZEN_STARTERS[digits[2]] + TENS_NUMBERS[digits[3]]
                    else:
                        if digits[2] in TENS:
                            if digits[0] == '1':
                                result = 'ათას' + ' ' + DOZEN_STARTERS[digits[2]] + 'ათი'
                            else:
                                result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + DOZEN_STARTERS[digits[2]] + 'ათი'
                        else:
                            if digits[0] == '1':
                                result = 'ათას' + ' ' + SIMPLE_TENS[digits[2]]
                            else:
                                result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + SIMPLE_TENS[digits[2]]
                else:
                    if digits[3] != '0':
                        if digits[0] == '1':
                            result = 'ათას' + ' ' +  GENERAL_NUMBERS[digits[3]]
                        else:
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + GENERAL_NUMBERS[digits[3]]
            else:
                if digits[2] != '0':
                    if digits[3] != '0':
                        if digits[0] == '1':
                            result = 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + DOZEN_STARTERS[digits[2]] + GENERAL_NUMBERS[digits[3]]
                        elif digits[2] in TENS:
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + DOZEN_STARTERS[digits[2]] + TENS_NUMBERS[digits[3]]
                        else:
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + DOZEN_STARTERS[digits[2]] + GENERAL_NUMBERS[digits[3]]
                    else:
                        if digits[0] == '1':
                            result = 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + DOZEN_STARTERS[digits[2]] + 'ათი'
                        else:
                            if digits[2] in TENS:
                                result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + DOZEN_STARTERS[digits[2]] + 'ათი'
                            else:
                                result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + SIMPLE_TENS[digits[2]]
                else:
                    if digits[3] != '0':
                        if digits[0] == '1':
                            result = 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + GENERAL_NUMBERS[digits[3]]
                        else:
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + ' ' + GENERAL_NUMBERS[digits[3]]
                    else:
                        if digits[0] == '1':
                            result = 'ათას' + ' ' + HUNDREDS[digits[1]] + 'ი'
                        else:
                            result = GENERAL_NUMBERS[digits[0]] + ' ' + 'ათას' + ' ' + HUNDREDS[digits[1]] + 'ი'
    elif len(digits) == 3:
        if digits[0] != 0:
            if digits[0] == '1':
                if digits[1] == '0':
                    if digits[2] == '0':
                        result = 'ასი'
                    else:
                        result = 'ას' + ' ' + GENERAL_NUMBERS[digits[2]]
                else:
                    if digits[2] != '0':
                        if digits[1] in TENS:
                            result = 'ას' + ' ' + DOZEN_STARTERS[digits[1]] + TENS_NUMBERS[digits[2]]
                        else:
                            result = 'ას' + ' ' + DOZEN_STARTERS[digits[1]] + GENERAL_NUMBERS[digits[2]]
                    else:
                        if digits[1] in TENS:
                            result = 'ას' + ' ' + DOZEN_STARTERS[digits[1]] + 'ათი'
                        else:
                            result = 'ას' + ' ' + SIMPLE_TENS[digits[1]]
            else:
                if digits[1] == '0':
                    if digits[2] == '0':
                        result = HUNDREDS[digits[0]] + 'ი'
                    else:
                        result = HUNDREDS[digits[0]] + ' ' + GENERAL_NUMBERS[digits[2]]
                else:
                    if digits[2] != '0':
                        if digits[1] in TENS:
                            result = HUNDREDS[digits[0]] + ' ' + DOZEN_STARTERS[digits[1]] + TENS_NUMBERS[digits[2]]
                        else:
                            result = HUNDREDS[digits[0]] + ' ' + DOZEN_STARTERS[digits[1]] + GENERAL_NUMBERS[digits[2]]
                    else:
                        if digits[1] in TENS:
                            result = HUNDREDS[digits[0]] + ' ' + DOZEN_STARTERS[digits[1]] + 'ათი'
                        else:
                            result = HUNDREDS[digits[0]] + ' ' + SIMPLE_TENS[digits[1]]
    elif len(digits) == 1:
        result = GENERAL_NUMBERS[digits[0]]
    elif len(digits) == 2:
        if digits[0] in TENS:
            if digits[1] == '0':
                result = DOZEN_STARTERS[digits[0]] + 'ათი'
            else:
                first = DOZEN_STARTERS[digits[0]]
                second = TENS_NUMBERS[digits[1]]

                result = first + second
        elif digits[0] not in TENS:
            if digits[1] == '0':
                result = SIMPLE_TENS[digits[0]]
            else:
                first = DOZEN_STARTERS[digits[0]]
                second = GENERAL_NUMBERS[digits[1]]

                result = first + second
    elif len(digits) > 4: 
        return
    
    return result


def numbers_converter_in_text(text):
    # Finds numbers in text and converts them

    pattern = r'\b\d{1,4}\b'
    years = re.findall(pattern, text)

    for year in years:
        text_year = numbers_converter(int(year))
        text = text.replace(year, text_year)

    return text