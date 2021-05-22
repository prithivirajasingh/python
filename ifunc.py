def ifunc(**kwargs):
    '''
    Function to get user input
    :param kwargs: itext='', irange=[], iformat=string/integer
    :return: Returns user input
    '''
    # Debug - print arguments
    # print(kwargs['irange'])

    # Assign default itext
    if not 'itext' in kwargs:
        kwargs['itext'] = 'Enter input: '
    # Assign iformat if not defined
    if not 'iformat' in kwargs:
        kwargs['iformat'] = str
        if 'irange' in kwargs:
            if type(kwargs['irange'][0]) == int:
                kwargs['iformat'] = int

    # Check if irange is defined
    if 'irange' in kwargs:
        # Check mismatch in irange and iformat
        if type(kwargs['irange'][0]) == str and kwargs['iformat'] == str or type(kwargs['irange'][0]) == int and kwargs['iformat'] == int:
            pass
        else:
            print('irange and iformat does not match')
            return
        # Loop for input until all conditions are satisfied
        while True:
            x = input(kwargs['itext'])
            if kwargs['iformat'] == str:
                if not x in kwargs['irange']:
                    print('Input not in expected range.')
                    continue
                y = x
                break
            else:
                # Try converting string input to int
                try:
                    y = int(x)
                    if not y in kwargs['irange']:
                        print('Input not in expected range.')
                        continue
                    break
                except ValueError:
                    print('Integer input expected.')
        # print(y)
        return y
    # Code to execute if irange is not defined
    else:
        while True:
            x = input(kwargs['itext'])
            if kwargs['iformat'] == str:
                y = x
                break
            else:
                # Try converting string input to int
                try:
                    y = int(x)
                    break
                except ValueError:
                    print('Integer input expected.')
        # print(y)
        return y


# x = ifunc(irange=['a','b','cde'])
# print(x)
# print(type(x))
