def longest_increasing_streak(nums: list[int]) -> dict:
    """Расчет непрерывной подпоследовательности

    Args:
        records (list[str]): Список последовательности чисел

    Returns:
        dict: Возвращает словарь формата: длина максимальной
              последовательности; максимальная последовательность
    """
    max_streak = 0
    temp_max_streak = 0
    streak: list[int] = list()
    result = {
        'length': 0,
        'streak': streak
    }
    left_point = 0
    right_point = 0

    # Ситуация когда список пуст или список из 1 или одного и того же элемента
    if len(nums) == 0 or len(set(nums)) == 1:
        return result

    for i in range(1, len(nums)):
        if nums[right_point] < nums[i]:
            temp_max_streak += 1
            right_point += 1
        else:
            if max_streak < temp_max_streak:
                # Забираем длину последовательности и саму последовательность
                max_streak = max(max_streak, temp_max_streak)
                streak = nums[left_point:left_point + max_streak + 1]

            # Обнуляем точки списка и длину этого списка
            left_point = i
            right_point = i
            temp_max_streak = 0

    # На случай если, в цикле дошли до последнего элемента еще раз проверим
    if temp_max_streak > max_streak:
        streak = nums[left_point:right_point + 1]

    # Заполняем возвращаемый словарь
    result['length'] = len(streak)
    result['streak'] = streak

    return result


if __name__ == '__main__':
    nums = [1, 3, 2, 5, 8, 4, 7]
    # nums = [3, 2, 1]
    # nums = []
    # nums = [3, 3, 3]
    print(longest_increasing_streak(nums))
