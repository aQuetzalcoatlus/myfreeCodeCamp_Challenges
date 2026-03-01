"""Missing Socks

Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

    - Every 2 wash cycles, you lose a single sock.
    - Every 3 wash cycles, you find a single missing sock.
    - Every 5 wash cycles, a single sock is worn out and must be thrown away.
    - Every 10 wash cycles, you buy a pair of socks.
    - You can never have less than zero total socks.
    - Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
    - Return the number of complete pairs of socks.

"""


def sock_pairs(pairs: int, cycles: int) -> int:
    """Given the number of pairs of socks and number of wash cycles, return the number of complete pairs of socks after mysterious events."""

    delta: int = -(cycles // 2) + (cycles // 3) - (cycles // 5) + 2 * (cycles // 10)
    socks: int = max(0, 2 * pairs + delta)  # never below zero socks

    return socks // 2

    """ I started with the following solution, but found the above approach to be much more elegant. """
    # num_current_socks: int = pairs * 2
    # num_current_unpaired: int = 0
    # for cycle_number in range(1, cycles + 1):
    #     if cycle_number % 2 == 0:
    #         num_current_socks -= 1
    #         num_current_unpaired += num_current_socks % 2
    #     if cycle_number % 3 == 0:
    #         num_current_socks += 1
    #         num_current_unpaired += num_current_socks % 2
    #     if cycle_number % 5 == 0:
    #         num_current_socks -= 1
    #         num_current_unpaired += num_current_socks % 2
    #     if cycle_number % 10 == 0:
    #         num_current_socks += 2
    #         num_current_unpaired += num_current_socks % 2
    #     print(f"Cycle number: {cycle_number}: {num_current_socks} socks")
    # return num_current_socks // 2 if num_current_socks // 2 > 0 else 0


if __name__ == "__main__":
    # print(sock_pairs(2, 5))
    print(sock_pairs(1, 2))
