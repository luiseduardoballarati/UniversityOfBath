"""
Implement an algorithm in Java which given a String as input, redacts all words from a given set of
“redactable” words (an array of Strings), and returns the result as a String. For example, given the String:

    The quick brown fox jumps over the lazy dog!

and the redactable set of words:

    Fox, jumps, dog

the output String should be:

    The quick brown *** ***** over the lazy ***!

Rules:

Your implementation must use the public static String redact(...) method signature
You are not allowed to import any libraries or fully-qualified names of additional classes for this question
The number of stars in the redacted text is the same as the number of letters in the word that has been redacted
Capitalization of redacted words is ignored (i.e., "the" in the redacted words list would redact "The", "THE" etc.)
Only whole words that match one of the redacted words should be redacted, e.g., given the redacted word "pass",
the word "password" would not be redacted.
Hyphenated words and words with apostrophes (e.g. Chris' or Chris's) will not be tested.
Capitalization of unredacted words in the input text should be maintained in the output text.

"""

string = "The quick brown fox jumps over the lazy dog!"

redact_list = ["Fox", "jumps", "dog"]

def redact(string, redact_list):

    new_list = []
    new_redact_list = []
    rmv = []

    for index, letter in enumerate(string):
        if letter.isalpha() or letter == " ":
            pass
        else:
            string = string.replace(letter, "")
            rmv.append([index, letter])

    for re in redact_list:
        new_redact_list.append(re.capitalize())

    string_splitted = string.split(" ")
    for st in string_splitted:
        if st in redact_list or st in new_redact_list:
            new_list.append("*"*len(st))
        else:
            new_list.append(st)

    res = ' '.join(new_list)

    for r in rmv:
        res = res[:r[0]] + r[1] + res[r[0]:]

    return res

print(redact(string, redact_list))

