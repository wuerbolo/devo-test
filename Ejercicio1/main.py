from argparse import ArgumentParser

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

# 12 = 1 + 2 + 3 + 4 + 6 ==> abundante
# 6 = 1 + 2 + 3 ==> perfecto
# 4 = 1 + 2 ==> defectivo
def get_number_type(n, _divisors):
    return 'number_type'

def classify(number_list):

    for num in number_list:
        divisors, divisor_sum = get_divisors(num)
        print('****** %s ******' % num)
        print('Divisors: {}'.format(' + '.join(str(x) for x in divisors)))
        if divisor_sum == num:
            print('%s is a perfect number' % num)
        elif divisor_sum > num:
            print('%s is an abundant number' % num)
        elif divisor_sum < num:
            print('%s is deficient number' % num)


if __name__ == "__main__":
    # args = init_args()

    numbers = read_numbers()
    classify(numbers)

    