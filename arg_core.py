def get_arg(ctx):


    command = ctx.message.content
    command = command.split(' ', 1)[-1]

    args = command.split('-')
    parsed_args = []

    for arg in args:
        arg = arg.strip().strip('"')

        if '(' in arg:
            key, value = arg.split('(')
            value = value.rstrip(')')
            if value.isdigit():
                value = int(value)
            elif value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            parsed_args.append((key.strip(), value))
        else:
            parsed_args.append(arg)

    return tuple(parsed_args)