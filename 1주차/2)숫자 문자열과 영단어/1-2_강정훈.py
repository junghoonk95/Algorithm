def solution(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    letter_nums = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_dict = dict(zip(letter_nums, numbers))
    print(number_dict)
    
    result = "" 
    curr_word = ""

    for letter in s:
        if letter in numbers:
            result += letter
        else:
            curr_word += letter 
            if curr_word in letter_nums:
                result += number_dict[curr_word]
                curr_word = ""
    return int(result)
