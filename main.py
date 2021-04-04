import re
opened_file = open('regex_sum_1186280.txt')
read_file = opened_file.read()

numbers = re.findall('[0-9]+',read_file)

num_list = list()

for number in numbers:
    number = int(number)
    num_list.append(number)

print(sum(num_list))