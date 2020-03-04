# This number was calcualted by adding all of the 1, 2, 3, and 4 digit primes together to get there total length
# Then the number of 5 digit primes was calculated to give a digit length of 10,005 which is required for the question
# The number of primes needed to get the requiered length was 2287
# 20231 is the 2287th prime
num_for_prime_digit_list = 20231
id_length = 5


def solution(i):
    minion_id = get_minion_id(i)
    return minion_id


def get_minion_id(hat_number):
    prime_list = get_prime_list_in_range(num_for_prime_digit_list)
    digit_list = convert_list_of_primes_to_digit_list(prime_list)
    minion_id = get_minion_id_from_digit_list(digit_list, hat_number)
    return minion_id


def get_minion_id_from_digit_list(digit_list, i):
    minion_id_slice = digit_list[i:i+id_length]
    minion_id = ''.join(minion_id_slice)
    return minion_id


def get_prime_list_in_range(num_to):
    """
    Invented by the Greek mathematician Eratosthenes over two thousand years ago, is to sieve by repeatedly casting out multiples of primes.
    Begin by making a list of all numbers from 2 to the maximum desired prime n.
    Then repeatedly take the smallest uncrossed number and cross out all of its multiples;
    the numbers that remain uncrossed are prime.

    Optimisations have been made:
        The sieve automatically filters out all multiples of 2 apart from 2 itself as there are no even primes apart from 2
        The inner loop which sieves out non primes starts at the square of the current prime as all primes since all smaller primes have been caught in previous sift loops
        Cant get to work # The outer loop stops at the sqrt of the muber to find primes up to as all non primes will have been sieved out on previous loops
    Arguments:
        num_to {int} -- [number of primes up to]
    Returns:
        [list] -- [list of all primes]
    """
    prime_list = list()
    sieve = _create_optimised_sieve(num_to)

    for outer_index in xrange(2, (num_to)+1):

        if (sieve[outer_index]):
            prime_list.append(outer_index)

            for inner_index in xrange(int(outer_index**2), num_to+1, outer_index):
                sieve[inner_index] = False

    return prime_list


def _create_optimised_sieve(num_to):
    sieve = [False
             if (index) % 2 == 0 and (index != 2)
             else True
             for index in xrange(num_to + 1)]
    return sieve


def convert_list_of_primes_to_digit_list(primes):
    strings = _convert_int_list_to_string_list(primes)
    prime_string = ''.join(strings)
    int_list = _convert_int_string_to_digit_list(prime_string)
    return int_list


def _convert_int_list_to_string_list(int_list):
    return [str(integer) for integer in int_list]


def _convert_int_string_to_digit_list(string):
    return [digit for digit in string]


if __name__ == '__main__':
    solution(3)
