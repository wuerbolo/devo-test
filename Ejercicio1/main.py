from argparse import ArgumentParser
import math
import logging


def init_args():

    parser = ArgumentParser(
        description='Number classifier')
    parser.add_argument('n', type=int, help='upper limit to search upto')
    args = parser.parse_args()
    return args

def get_logger(level=logging.INFO):
    logger = logging.getLogger('perfect_numbers')
    fh = logging.FileHandler('./classify_numbers.log', mode='w')
    logger.addHandler(fh)
    logger.setLevel(level)
    return logger

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
        if primes.get(str(x)):
            continue
        if (n % x == 0): # divisor
            yield x
            if x != n//x:
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
        num_divisors = 0
        # import pdb; pdb.set_trace()
        if primes.get(str(num)):
            logger.info('****** %s ******' % num)
            logger.info('%s is a prime number' % num)
            continue

        max_divisors = 2 * math.isqrt(num)
        logger.info('****** %s ******' % num)
        logger.debug('Max divisors for {} are {}'.format(num, max_divisors))
        for i, divisor in enumerate(get_divisor(num), start=1):
            divisor_sum += divisor
            str_divisors += ' + {}'.format(str(divisor))
            num_divisors += 1
            if i == max_divisors:
                logger.debug('Early exit for number %s' % num)
                break
            else:
                logger.debug('No exit found for number {0} at iterator {1} where 2*sqrt of {0} is {2}'.format(num, i, max_divisors))

        if num_divisors == 1:
            logger.debug('Only 1 divisor found, adding to primes list %s' % num)
            primes[str(num)] = True

        logger.info('Divisors: {}'.format(str_divisors))
        if divisor_sum == num:
            logger.info('%s is a perfect number' % num)
        elif divisor_sum > num:
            logger.info('%s is an abundant number' % num)
        elif divisor_sum < num:
            logger.info('%s is deficient number' % num)


def import_primes(filename):
    primes = {}
    with open(filename, 'r') as f:
        contents = f.read()
        for prime in contents.split('-'):
            primes[prime] = True
    return primes


if __name__ == "__main__":
    args = init_args()
    global primes
    primes = import_primes('./primes.txt')
    global n
    n = args.n

    global logger
    logger = get_logger(logging.INFO)
    import timeit
    exec_time = timeit.timeit(classify, number=1, globals=globals())
    print(exec_time)
