calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    len_ = len(string)
    str1 = string.upper()
    str2 = string.lower()
    kort = (len_, str1, str2)
    count_calls()
    return kort


def is_contains(string, list_to_search):
    str_ = string.upper()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if str_ in list_to_search:
        count_calls()
        return True
    else:
        count_calls()
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
