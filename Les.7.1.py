def count_words(function):
    func = function()
    print(func.split())
    return func

@count_words
def entered_string():
    return input('Enter string:')