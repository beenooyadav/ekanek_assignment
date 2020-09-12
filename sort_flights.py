from operator import itemgetter

from typing import List


def print_cheapest_flights(onward_price_list: List[int], return_price_list: List[int], k: int):
    """
    prints the k cheapest combinations of onward and return flights
    :param onward_price_list: onward flights price
    :param return_price_list: return flights price
    :param k: k cheapest price
    :return: prints k cheapest combo of onward and return flights

    Time complexity:
    the sort is O(n*m log n*m) both on average and in the worst case.

    Space complexity:
    the sort is Ω(n*m) since python uses time sort which is similar to merge sort. they use auxillary list to sort.

    where n is number of onward flights
    and m is number of return flights
    """
    onward_price_list.sort()
    return_price_list.sort()

    price_list = []
    for i in onward_price_list:
        for j in return_price_list:
            price_list.append((i, j, i + j))

    price_list.sort(key=itemgetter(2))

    for trip in price_list[:k]:
        print(f'{trip[0]}, {trip[1]}')


if __name__ == '__main__':
    # for testing
    delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    k = 10
    print_cheapest_flights(onward_price_list=delhi_to_mumbai, return_price_list=mumbai_to_delhi, k=k)
