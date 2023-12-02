def merge_sort(string):
    if len(string) <= 1:
        return string

    # Dividir a string ao meio
    middle = len(string) // 2
    left_half = string[:middle]
    right_half = string[middle:]

    # Chamada recursiva para ordenar as metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinação das metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Comparação e mesclagem das metades
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes, se houver
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return ''.join(result)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    ordered_first_string = merge_sort(first_string)
    ordered_second_string = merge_sort(second_string)
    compare = ordered_first_string == ordered_second_string

    if not first_string or not second_string:
        return ordered_first_string, ordered_second_string, False

    return ordered_first_string, ordered_second_string, compare


print(is_anagram('amor', 'roma'))
