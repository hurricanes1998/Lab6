def lab_6() -> bool:

    nomer_bileta = input("Введите номер билета: ")
    nomer_bileta_length = len(nomer_bileta)

    if nomer_bileta_length < 2 or nomer_bileta_length % 2 > 0:
        print("Количество символов в номере должно быть четным.")
        return False

    [left_numbers, right_numbers] = nomer_bileta[:: int(len(nomer_bileta) / 2)]
    left_sum = sum(int(i) for i in list(left_numbers))
    right_sum = sum(int(i) for i in list(right_numbers))

    return left_sum == right_sum

print(lab_6())