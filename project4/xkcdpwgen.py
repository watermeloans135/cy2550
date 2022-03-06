import random
import argparse

parser = argparse.ArgumentParser(description= 'generate passwords via XKCD method')
group = parser.add_argument_group()
group.add_argument('-w', '--words', type = int, metavar = '', required = False, help = ' include WORDS words in the password (default=4)')
group.add_argument('-c', '--caps', type = int, metavar = '', required = False, help = 'capitalize the first letter of CAPS random words (default=0)')
group.add_argument('-n', '--numbers', type = int, metavar = '', required = False, help = 'insert NUMBERS random numbers in the password (default=0)')
group.add_argument('-s', '--symbols', type = int, metavar = '', required = False, help = 'insert SYMBOLS random symbols in the password (default=0)')

args = parser.parse_args()


f = open("words.txt", "r")
words = f.readlines()

symbols = "!@#$%^&*()"
numbers = "1234567890"
symbolsList = list(symbols)
numbersList = list(numbers)

default_words = 4

def gen_xkcd_default():
    result = []
    for i in range(default_words):
        result.append(words[random.randint(0, len(words))][:-1])
    return result


def gen_xkcd(num_words):
    result = []
    for i in range(num_words):
        result.append(words[random.randint(0, len(words))][:-1])
    return result


def gen_xkcd_capitalize(start_list, num_capitalized):
    result = []
    to_be_capitalized = random.sample(range(0, len(start_list)), num_capitalized)
    for i in range(len(start_list)):
        if i in to_be_capitalized:
            result.append(start_list[i].capitalize())
        else:
            result.append(start_list[i])
    return result

def gen_xkcd_insert_symbols(start_list, num_inserted):
    to_be_inserted = []

    for i in range(num_inserted):
        to_be_inserted.append(random.randint(0, len(start_list)))
    to_be_inserted.sort()
    for i in range(len(to_be_inserted) -1, 0, -1):
        start_list.insert(to_be_inserted[i], random.choice(symbolsList))
    return start_list

def gen_xkcd_insert_numbers(start_list, num_inserted):
    to_be_inserted = []

    for i in range(num_inserted):
        to_be_inserted.append(random.randint(0, len(start_list)))
    to_be_inserted.sort()
    for i in range(len(to_be_inserted) - 1, 0, -1):
        start_list.insert(to_be_inserted[i], random.choice(numbersList))
    return start_list

def combine(list):
    result = ""
    for i in range(len(list)):
        result += list[i]
    return result

if __name__ == '__main__':
    result = []
    if args.words:
        result = gen_xkcd(args.words)
    else:
        result = gen_xkcd_default()
    if args.caps:
        result = gen_xkcd_capitalize(result, args.caps)
    if args.numbers:
        result = gen_xkcd_insert_numbers(result, args.numbers)
    if args.symbols:
        result = gen_xkcd_insert_symbols(result, args.symbols)

    print(combine(result))




