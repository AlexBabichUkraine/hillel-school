def arguments(variable, *args, keyword_arg, **kwargs):
    print(variable)
    print(f'{keyword_arg=}')
    print(args)
    print(kwargs)
    print(kwargs['x'])
    return kwargs['x'] * kwargs['y'] * kwargs['z']


print(arguments(109, 0, keyword_arg=10, x=19, y=19, z=23))
