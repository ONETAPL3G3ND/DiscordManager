def get_arg(ctx):


    command = ctx.message.content
    command = command.split(' ', 1)[-1]

    args = command.split('-')  # Разделение по "-"
    parsed_args = []

    for arg in args:
        # Удаляем начальные и конечные пробелы и символы кавычек
        arg = arg.strip().strip('"')

        # Для параметров вида amount(99) или bool(True)
        if '(' in arg:
            key, value = arg.split('(')
            value = value.rstrip(')')
            if value.isdigit():  # Если значение - число, преобразуем в int
                value = int(value)
            elif value.lower() == 'true':  # Если значение - 'true', возвращаем True
                value = True
            elif value.lower() == 'false':  # Если значение - 'false', возвращаем False
                value = False
            parsed_args.append((key.strip(), value))
        else:
            parsed_args.append(arg)

    return tuple(parsed_args)