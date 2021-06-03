def searchtext(pattern, filetype='', location='', subfolder=False):
    """
    A generator function which searches for a regex pattern inside the contents of files in a directory.\n
    Default filetype: All filetypes.\n
    Default location: Current location of the python file.\n
    Deafult subfolder search: Set to false (subfolder search disabled) by default\n
    :param pattern: (Required) Search pattern. Example: pattern=r'(\d{3})-(\d{3})-(\d{4})'
    :param filetype: (Optional) Part of filename or extension can be supplied. Example: filetype='.txt'
    :param location: (Optional) Top directory to search.
    :param subfolder: (Optional) Set to True if subfolder search is required. Example: subfolder=True
    :return: A list. [-1] if directory does not exist, [0] if no match found, ['filePath', lineNumber, 'matchedWord'] if found
    """
    import os
    import re
    if pattern == '':
        print('Pattern cannot be empty!')
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
                                yield value
                except:
                    continue
    if matchfound == False:
        # print('No match found!')
        yield [0]
        return


pattern = r'(\d{3})-(\d{3})-(\d{4})'
# pattern = r'\d{3}-\d{3}-\d{4}'
for matches in searchtext(pattern=pattern, filetype='.txt', subfolder=True):
    print(matches)
