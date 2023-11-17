
def are_consecutive(numbers):
    sorted_numbers = sorted(set(numbers))  # Remove duplicates and sort

    # adding Ace as a 1 as well.
    if 14 in sorted_numbers:
        sorted_numbers = sorted(sorted_numbers + [1])

    consecutive_list = []
    current_consecutive = [sorted_numbers[0]]

    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] == sorted_numbers[i - 1] + 1:
            current_consecutive.append(sorted_numbers[i])
        else:
            current_consecutive = [sorted_numbers[i]]

        if len(current_consecutive) >= 5:
            consecutive_list = current_consecutive

    return consecutive_list


def count_dupes(some_list: list, occurences: int):
    """
    returns a list of cards that appear in the list passed the specificed amount of occurences.
    """
    
    unique = set(some_list)
    dupe_count = {u:some_list.count(u) for u in unique}
    duplicate_cards = [k for k in dupe_count.keys() if dupe_count[k] >= occurences]


    return duplicate_cards

