def evenSubarray(numbers, k):
    n = len(numbers)
    count = 0
    prefix = [0] * (n + 1)
    odd = 0

    # traverse in the array
    for i in range(n):
        prefix[odd] += 1

        # if array element is odd
        if (numbers[i] & 1):
            odd += 1

        for t in range(k+1):
            # when number of odd elements>=t
            if (odd >= t):
                count += prefix[odd - t]

    return count


def test_even():
    error_counter = 0
    input_output_pairs = [(([1, 3, 7, 8, 10, 13], 0), 3),
                          (([1, 3, 7, 8, 10, 13], 1), 11),
                          (([1, 3, 7, 8, 10, 13], 2), 16),
                          (([6, 3, 5, 8], 1), 6),]
    for inp, out in input_output_pairs:
        curr_out = evenSubarray(*inp)
        if curr_out != out:
            error_counter += 1
            print(f'Input: {inp}    Output: {out}    Current: {curr_out}')

    print(f'errors {error_counter}/{len(input_output_pairs)}')


test_even()
