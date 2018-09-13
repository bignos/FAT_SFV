# This module analyse data from raw extracted value from official html file
# [STATE]   : POC ( Unfinished )
# [AUTHOR]  : bignos@gmail.com

# coding=utf-8

import os               # for path and basename
import lxml.html        # for parse XML
import re               # for Regular expression

# -[ Data ]-
character_html_directory_path = './resources/framedata/html/'

# -[ Private Function ]-


def _read_html_file(path):
    """ Private function read file and return content on a string
        path:   {str}   Path of the character file
        Return: {str}   The content of the file
        Throw FileNotFoundError if the file in path is not found
        Throw PermissionError if you don't have permission to read the file
    """
    with open(path, 'rt', encoding='utf-8') as document:
        result = document.read()
    return result


def _get_all_character_files(character_html_directory_path):
    return [character_html_directory_path + filepath for filepath in os.listdir(character_html_directory_path)
            if filepath.endswith('.html')]


def _columns_analyse(character_html_directory_path, xpath_pattern):
    character_html_files = _get_all_character_files(character_html_directory_path)
    data_list = list()
    for character_file in character_html_files:
        character_data = _read_html_file(character_file)
        character_data_tree = lxml.html.fromstring(character_data)

        for tr in character_data_tree.xpath('//table[@class="frameTbl"][@vtrigger="1"]/tr'):
            if tr.xpath('./td') != []:
                frame_startup = tr.xpath(xpath_pattern)
                data_list.append([frame_startup, os.path.basename(character_file)])

        for tr in character_data_tree.xpath('//table[@class="frameTbl"][@vtrigger="2"]/tr'):
            if tr.xpath('./td') != []:
                frame_startup = tr.xpath(xpath_pattern)
                data_list.append([frame_startup, os.path.basename(character_file)])

    unique_pattern = dict()
    for element in data_list:
        clean_pattern = _get_pattern(element[0])
        clean_pattern = ''.join(clean_pattern) if isinstance(clean_pattern, list) else clean_pattern
        if clean_pattern not in unique_pattern.keys():
            counter = 1
            real_values = list()
        else:
            counter = unique_pattern[clean_pattern][1] + 1
            real_values = unique_pattern[clean_pattern][0]

        real_values.append((element[0], element[1]))
        if clean_pattern:
            unique_pattern[clean_pattern] = [real_values, counter]

    for pattern in sorted(unique_pattern.keys()):
        frequency = unique_pattern[pattern][1]
        values_and_files = unique_pattern[pattern][0]
        print('{} : {}'.format(pattern, frequency))
        if r'\W' in pattern or frequency <= 20:
            for value in values_and_files:
                print('\t{} {}'.format(value[0], value[1]))
        else:
            print('\t{} {}'.format(values_and_files[0][0], values_and_files[0][1]))


def _get_pattern(value):
    if isinstance(value, list) and value != []:
        if len(value) == 1:
            return _get_pattern(value[0])
        else:
            return [_get_pattern(val) for val in value]
    elif isinstance(value, str):
        return _get_pattern_from_string(value.strip())
    else:
        return 'None'


def _get_pattern_from_string(value):
    if value == '':
        return None
    regex_char_type_list = [r'\d', r'\w', r'\+', r'\-', '±', '×', '○',
                            r'\*', r'\/', r',', r'\|', r'\s', r'\(', r'\)', r'\W']
    char_type_to_clean = [r'\d', r'\w', r'\s']
    pattern = list()
    for char in value:
        for char_type in regex_char_type_list:
            if re.match(char_type, char):
                pattern.append(char_type)
                break  # Only one type can be append

    pattern_string = ''.join(pattern)
    return _clean_pattern(pattern_string, char_type_to_clean)


def _clean_pattern(pattern, char_type_list):
    result = pattern
    for char_type in char_type_list:
        regex = r'(\{}){{1,}}'.format(char_type)
        replace = r'\{}+'.format(char_type)
        result = re.sub(regex, replace, result)

    return result


# -[ Main ]-
if __name__ == '__main__':
    _columns_analyse(character_html_directory_path, './td[2]/text()')
