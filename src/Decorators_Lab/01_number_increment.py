def number_increment(numbers):

    def increase():
        result_list = [x+1 for x in numbers]
        return result_list

    return increase()


print(number_increment([1, 2, 3]))