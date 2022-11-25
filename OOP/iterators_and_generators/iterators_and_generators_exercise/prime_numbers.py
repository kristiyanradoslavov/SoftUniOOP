def get_primes(nums):

    for current_num in nums:
        counter = 0

        for num in range(1, current_num + 1):
            if current_num % num == 0:
                counter += 1

        if counter <= 2 and current_num > 1:
            yield current_num


print(list(get_primes([-2, 0, 0, 1, 1, 0])))