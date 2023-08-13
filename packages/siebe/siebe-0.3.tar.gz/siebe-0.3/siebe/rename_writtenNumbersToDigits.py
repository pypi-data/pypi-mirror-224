def text2int(textnum, numwords={}):
    import re
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    textnum = re.sub(r'([^\s\w]|_)+', '', textnum)     # remove adjacent characters
    words = textnum.split()
    converted_words = []
    for word in words:
        if word.lower() in numwords:
            scale, increment = numwords[word.lower()]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            converted_words.append(str(current))
            current = 0  # Reset current after conversion
        else:
            converted_words.append(word)

    return ' '.join(converted_words)

print (text2int("this Fourteen is a test") )