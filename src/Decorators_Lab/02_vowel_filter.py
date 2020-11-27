vowels = {'a', 'e', 'o', 'u', 'i', 'y'}


def vowel_filter(function):

    def wrapper(*args):
        result = function(*args)
        filtered_list = [x for x in result if x.lower() in vowels]
        return filtered_list

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
