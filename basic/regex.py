import re


def find_all_integers(string):
    return list(map(int, re.findall(r'[0-9\-]+', string)))


def find_all_positive_integers(string):
    return list(map(int, re.findall(r'\d+', string)))


def find_all_letters(string):
    return re.findall(r'[A-Za-z]+', string)


def find_all_uppercase(string):
    return re.findall(r'[A-Z]+', string)


def find_all_lowercase(string):
    return re.findall(r'[a-z]+', string)
