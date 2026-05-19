def input_raise(ex: Exception) -> Exception:
    """Функция по обработке exeption

    Args:
        ex (Exception): Ошибка, которая отработала

    Returns:
        Exception: Возвращает ошибку для тернарного оператора
    """
    raise ex


def print_error_log(ex: Exception) -> None:
    """Функция печати ошибки в лог-файл

    Args:
        ex (Exception): Ошибка, для печати в лог
    """
    with open('error_log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{str(ex)}\n')


def process_grades(records: list[str]) -> dict:
    """Функция по обработке журнала успеваемости

    Args:
        records (list[str]): Список строк формата "Фамилия: оценка"

    Returns:
        dict: Возвращает словарь формата: количество успешно распарсенных
              записей; среднее арифметическое успешно обработанных;
              фамилии тех, у кого оценка >= 60; количество строк,
              которые не удалось обработать
    """
    result: dict = {
        'valid_count': 0,
        'average': 0.0,
        'passed': list(),
        'skipped': 0
    }

    for record in records:
        try:
            data = record.split(': ')

            # Если длина списка не 2 или
            # ключ или значение для словаря пустые
            if len(data) != 2 or data[0] == '' or data[1] == '':
                input_raise(ValueError(
                    f'Не удалось преобразовать строку: {data}. '
                    'Ошибка формата входящей строки'
                    )
                )

            # Проверяем формат Оценки
            if data[1].isnumeric():
                if int(data[1]) >= 60:
                    result['passed'].append(data[0])
            else:
                input_raise(ValueError(
                    f'Не удалось преобразовать строку: {data}. '
                    'Ошибка формата второго значения'
                    )
                )

            result['average'] += int(data[1])
            result['valid_count'] += 1
        except ValueError as e:
            print_error_log(e)
            result['skipped'] += 1
        except Exception as e:
            print_error_log(e)
            result['skipped'] += 1

    # На текущий момент хранилась общая сумма, переписываем на среднее
    result['average'] = (
                        round(result['average'] / result['valid_count'], 1)
                        if result['valid_count'] != 0
                        else result['average']
    )
    result['passed'].sort()

    return result


if __name__ == '__main__':
    data: list[str] = [
        "Иванов: 85",
        "Петров: 42",
        "Сидоров: abc",
        "Козлов: 90",
        ": 55",
        "Иванов: 70"
    ]

    print(process_grades(data))
