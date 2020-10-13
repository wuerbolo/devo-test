from argparse import ArgumentParser
import math

def init_args():

    parser = ArgumentParser(
        description='Number classifier')
    # parser.add_argument('input_file_path',
    #                     help='path for the input file')
    args = parser.parse_args()

    return args

def read_numbers():

    return [6, 12, 30, 2, 28, 70, 9]


def get_divisors(n):
    # TODO: should check if existing divisors have been already been calculated
    divisors = []
    divisor_sum = 0
    until = n // 2

    # import pdb; pdb.set_trace()
    for x in range(1, until + 1):
        if (n % x == 0): # divisor
            divisors.append(x)
            divisor_sum += x
    return divisors, divisor_sum

def get_divisor(n):
    yield 1
    until = math.isqrt(n) + 1 # isqrt is the floor square root
    for x in range(2, until):
        if (n % x == 0): # divisor
            yield x
            yield n//x

# 12 = 1 + 2 + 3 + 4 + 6 ==> abundante
# 6 = 1 + 2 + 3 ==> perfecto
# 4 = 1 + 2 ==> defectivo
def get_number_type(n, _divisors):
    return 'number_type'

def classify():
    number_list = range(n)
    for num in number_list:
        # divisors, divisor_sum = get_divisors(num)
        divisor_sum = 0
        str_divisors = ''
        # import pdb; pdb.set_trace()
        for divisor in get_divisor(num):
            divisor_sum += divisor
            str_divisors += ' + {}'.format(str(divisor))
        print('****** %s ******' % num)
        print('Divisors: {}'.format(str_divisors))
        if divisor_sum == num:
            print('%s is a perfect number' % num)
        elif divisor_sum > num:
            print('%s is an abundant number' % num)
        elif divisor_sum < num:
            print('%s is deficient number' % num)


if __name__ == "__main__":
    # args = init_args()
    global n
    n = 100000
    #numbers = read_numbers()
    import timeit
    # numbers = range(30)
    # classify(numbers)
    exec_time = timeit.timeit(classify, number=1, globals=globals())
    print(exec_time)
    