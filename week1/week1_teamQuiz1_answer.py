from re import A

# Quiz 1.

num_list = [1, 5, 7, 15, 17, 22, 28, 29]

def get_odd_num(num_list):
    odd = list()
    for i in num_list:
        if i % 2 == 1:
            odd.append(i)
    return odd

print(get_odd_num(num_list))

