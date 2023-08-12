import os


def my_sum(number1, number2):
    return number1 + number2


def my_random(number):
    return '%d%s' % (number, os.urandom(number))
