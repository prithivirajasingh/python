def searchtext(pattern, filetype='', location='', subfolder=True):
    """
    A generator function which searches for a regex pattern inside the contents of files in a directory.\n
    Default filetype: All filetypes.\n
    Default location: Current location of the python file.\n
    Deafult subfolder search: Set to True (subfolder search enabled) by default\n

    :param pattern: (Required) Search pattern. Example: pattern=r'(\d{3})-(\d{3})-(\d{4})'
    :param filetype: (Optional) Part of filename or extension can be supplied. Example: filetype='.txt'
    :param location: (Optional) Top directory to search.
    :param subfolder: (Optional) Set to False if subfolder search is not required. Example: subfolder=False
    :return: A list. [-2] if empty pattern is supplied, [-1] if directory does not exist, [0] if no match found, ['filePath', lineNumber, 'matchedWord'] if found
    """
    import os
    import re
    if pattern == '':
        # print('Pattern cannot be empty!')
        yield [-2]
        return
    if location == '':
        location = os.getcwd()
    if not os.path.isdir(location):
        # print('Invalid directory!')
        yield [-1]
        return
    matchfound = False
    for folders, subfolders, files in os.walk(location):
        for item in files:
            if location != folders and subfolder == False:
                break
            if filetype in item:
                filename = folders + '/' + item
                try:
                    with open(filename, 'r') as f:
                        for index, eachline in enumerate(f.readlines()):
                            match = re.findall(pattern, eachline)
                            if match != []:
                                matchfound = True
                                value = []
                                value.append(filename)
                                value.append(index + 1)
                                value.extend(match)
                                try:
                                    yield value
                                except GeneratorExit:
                                    # print('Iteration stopped!')
                                    return
                except:
                    continue
    if matchfound == False:
        # print('No match found!')
        yield [0]
        return

# USAGE EXAMPLE:
# pattern = r'(\d{3})-(\d{3})-(\d{4})'
# pattern = re.compile(r'happenings.+THE', re.DOTALL | re.IGNORECASE)
# for matches in searchtext(pattern):
#     print(matches)
