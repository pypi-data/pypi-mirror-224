#/usr/bin/env python3

# [dev] : s41r4j
# [git] : https://github.com/s41r4j/simpex

# [desc]: - simplifies the process of using regex in python
#         - 'simpex' stands for 'simple regex' (also name of class/package) 
#         - give a sample data set, this package will return a regex pattern 
#         - it has default data sets for common patterns (email, phone, etc.)


# imports
import re
import random
import requests
import json


# class
class simpex():
    def __init__(self, data_set = None, num = False, acu = False):
        self.data_set = data_set
        self.pattern = ''
        self.numbered_approach = num # focus on number of characters (or not)
        self.accuracy = acu # accuracy of pattern (default: 0; range: 0-1)
    
        # regex characters
        self.regex_characters = {
            'anchors': {
                'start_of_string': '\A',
                'start_of_line': '^',
                'end_of_string': '\Z',
                'end_of_line': '$',
                'word_boundary': '\b',
                'not_word_boundary': '\B',
                'start_of_word': '\<',
                'end_of_word': '\>'
            },
            'character_classes': {
                'control_character': '\c',
                'white_space': '\s',
                'not_white_space': '\S',
                'digit': '\d',
                'not_digit': '\D',
                'word': '\w',
                'not_word': '\W',
                'hexadecimal_digit': '\\x',
                'octal_digit': '\O'
            },
            'quantifiers': {
                'zero_or_more': '*',
                'one_or_more': '+',
                'zero_or_one': '?'
            },
            'escape_sequences': {
                'escape_following_character': '\\',
                'begin_literal_sequence': '\Q',
                'end_literal_sequence': '\E'
            },
            'metacharacters': { # always add '\' before these characters
                'caret': '^',
                'square_bracket': '[',
                'dot': '.',
                'dollar': '$',
                'curly_brace': '{',
                'asterisk': '*',
                'open_parenthesis': '(',
                'backslash': '\\',
                'plus': '+',
                'close_parenthesis': ')',
                'less_than': '<',
                'greater_than': '>',
                'at_sign': '@'
            },
            'special_characters': {
                'new_line': '\n',
                'carriage_return': '\r',
                'tab': '\t',
                'vertical_tab': '\v',
                'form_feed': '\f',
                'octal_character': '\\xxx',
                'hex_character': '\\xhh'
            },
            'groups_and_ranges': {
                'any_character_except_new_line': '.',
                'a_or_b': '(a|b)',
                'group': '(...)',
                'passive_non_capturing_group': '(?:...)',
                'range': '[abc]',
                'not_range': '[^abc]',
                'lowercase': '[a-z]',
                'uppercase': '[A-Z]',
                'digit': '[0-9]',
                'group_subpattern_number': '\\x'
            },
            'pattern_modifiers': {
                'global_match': 'g',
                'case_insensitive': 'i*',
                'multiple_lines': 'm*',
                'treat_string_as_single_line': 's*',
                'allow_comments_and_whitespace_in_pattern': 'x*',
                'evaluate_replacement': 'e*',
                'ungreedy_pattern': 'U*'
            },
            'string_replacement': {
                'nth_non_passive_group': '$n',
                'before_matched_string': '$`',
                'after_matched_string': '$\'',
                'last_matched_string': '$+',
                'entire_matched_string': '$&'
            },
            'posix': {
                'upper_case_letters': '[:upper:]',
                'lower_case_letters': '[:lower:]',
                'all_letters': '[:alpha:]',
                'digits_and_letters': '[:alnum:]',
                'digits': '[:digit:]',
                'hexadecimal_digits': '[:xdigit:]',
                'punctuation': '[:punct:]',
                'space_and_tab': '[:blank:]',
                'blank_characters': '[:space:]',
                'control_characters': '[:cntrl:]',
                'printed_characters': '[:graph:]',
                'printed_characters_and_spaces': '[:print:]',
                'digits_letters_and_underscore': '[:word:]'
            },
            'assertions': {
                'lookahead_assertion': '?=',
                'negative_lookahead': '?!',
                'lookbehind_assertion': '?<=',
                'negative_lookbehind': ['?!=', '?<!'],
                'once_only_subexpression': '?>',
                'comment': '?#'
            },
            'multipart_characters': {
                # 'exactly': '{n}'
                'exact_start': '{',
                'exact_end': '}',
                # 'n_or_more': '{n,}'
                'n_or_more_start': '{',
                'n_or_more_end': ',}',
                # 'n_or_less': '{,n}'
                'n_or_less_start': '{,',
                'n_or_less_end': '}',
                # 'n_to_m': '{n,m}'
                'n_to_m_start': '{',
                'n_to_m_mid': ',',
                'n_to_m_end': '}',
                # 'condition_if_then': '?()'
                'if_then_start': '?(',
                'if_then_end': ')',
                # 'condition_if_then_else': '?()\|'
                'if_then_else_start': '?(',
                'if_then_else_mid': ')',
                'if_then_else_end': '\|',
            }
        }

    # check if data set is provided & have at least 3 items    
    def regex(self):
        if self.data_set is None:
            return '[simpex-err: no data set provided]'
        elif len(self.data_set) < 3:
            return '[simpex-err: min 3 items required]'
        elif len(self.data_set) > 10:
            return '[simpex-err: max 100 items allowed]'
        else:
            return self.create_pattern()

    # create pattern
    def create_pattern(self):
        # dividing data set into learning set and testing set
        learning_set = self.data_set[:int(len(self.data_set) * 0.8)] # 80%
        testing_set = self.data_set[int(len(self.data_set) * 0.8):]  # 20%

        # IMP items:
        # - first item  = main/base & minimum (pattern)
        # - second item = maximum (pattern)

        # understanding the pattern with learning set
        if self.numbered_approach: # numbered approach (if character size is a requirement)
            # phone number: 9885795625, 9164975864 (10 digits)
            # [in numbered approach, we will write a pattern for each character]

            # checking if maximum items have same length
            s, n = 0, 0 # similar, not similar
            for item in self.data_set:
                if len(str(item)) == len(str(self.data_set[0])): s += 1
                else: n += 1
            if s < n: return '[simpex-err: most of the items should have same length]'

            # creating a list of probable patterns
            guessed_patterns = []

            # convert each single item into list of characters
            for item in learning_set:
                arr_item = list(str(item))
                
                # making a pattern for each character
                temp_pattern = []
                for i in arr_item:
                    # match regex of `i` & `regex_characters`
                    if re.match(self.regex_characters['groups_and_ranges']['digit'], i):
                        temp_pattern.append('\d')
                    elif re.match(self.regex_characters['groups_and_ranges']['lowercase'], i):
                        temp_pattern.append('[a-z]')
                    elif re.match(self.regex_characters['groups_and_ranges']['uppercase'], i):
                        temp_pattern.append('[A-Z]')
                    else:
                        got_something = False
                        for key, value in self.regex_characters['metacharacters'].items():
                            if i == value:
                                temp_pattern.append('\\' + i)
                                got_something = True
                                break
                        if not got_something:
                            temp_pattern.append('\\' + i)
                        #     return '[simpex-err: unknown character]'

                # compressing/removing double characters (`multipart_characters`)
                prev = ''
                repeat_count = 0
                temp_pattern2 = []
                for i in temp_pattern:
                    if i != prev:
                        # adding to `temp_pattern2`
                        if repeat_count != 0:
                            temp_pattern2.append('{' + str(repeat_count+1) + '}')
                        temp_pattern2.append(i)
                        
                        prev = i # setting up `prev` value
                        repeat_count = 0 # resetting `repeat_count`
                        
                    else: # `i` == `prev`
                        repeat_count += 1

                # for last character if it is repeated                       
                if repeat_count != 0:
                        temp_pattern2.append('{' + str(repeat_count+1) + '}')

                # add pattern to `guessed_patterns`
                guessed_patterns.append(''.join(temp_pattern2))

            # selecting the most common pattern
            self.pattern = max(set(guessed_patterns), key = guessed_patterns.count)

                
        else: # non numbered approach
            # random numbers: 12345678, 46547685962471 (length varies)
            # [in non numbered approach, we will write a pattern for each item]
            
            def filter(temp_pattern, check = 0, prv = None): 
                # if previous element is not `a-z`, `A-Z` or `0-9` then add `[` else add `]`
                if check == 0 and temp_pattern[-1] not in ['a-z', 'A-Z', '0-9']:
                    if temp_pattern[-1] in [value for key, value in self.regex_characters['metacharacters'].items()] or ']+\\' in temp_pattern[-1]:
                        temp_pattern.append('[')
                elif check == 1 and temp_pattern[-1] in ['a-z', 'A-Z', '0-9']:
                    temp_pattern.append(']')
                elif check == 2 and prv != None:
                    # `prv` is not in `temp_pattern` until `[` (go reverse)
                    for i in reversed(temp_pattern):
                        if i == '[': break
                        elif i == prv: return temp_pattern
                    temp_pattern.append(prv)

                return temp_pattern
               
            # creating a list of probable patterns
            guessed_patterns = []

            # convert each single item into list of characters
            for item in learning_set:
                arr_item = list(str(item))
                
                # making a pattern for each item
                temp_pattern = []
                temp_pattern.append('^') # start of string
                for i in arr_item:
                    # match regex of `i` & `regex_characters`
                    if re.match(self.regex_characters['groups_and_ranges']['digit'], i):
                        temp_pattern = filter(temp_pattern)
                        temp_pattern = filter(temp_pattern, 2, '0-9')
                    elif re.match(self.regex_characters['groups_and_ranges']['lowercase'], i):
                        temp_pattern = filter(temp_pattern)
                        temp_pattern = filter(temp_pattern, 2, 'a-z')
                    elif re.match(self.regex_characters['groups_and_ranges']['uppercase'], i):
                        temp_pattern = filter(temp_pattern)
                        temp_pattern.append('A-Z')
                    else:
                        got_something = False
                        for key, value in self.regex_characters['metacharacters'].items():
                            if i == value:
                                temp_pattern.append(']+\\' + i)
                                got_something = True
                                break
                        if not got_something:
                            temp_pattern.append('\\' + i)
                        #     return '[simpex-err: unknown character]'

                temp_pattern = filter(temp_pattern, 1)
                temp_pattern.append('*$') # end of string

                # add pattern to `guessed_patterns`
                guessed_patterns.append(''.join(temp_pattern))

            # selecting the most common pattern
            self.pattern = max(set(guessed_patterns), key = guessed_patterns.count)


        # checking pattern accuracy w/ `testing_set`
        if self.accuracy:
            accuracy = 0
            for item in testing_set:
                if re.match(self.pattern, str(item)):
                    accuracy += 1

            accuracy = accuracy/len(testing_set) * 100
            

            # return {'regex': self.pattern, 'accuracy': self.accuracy}
            # return self.pattern
            return {'regex': self.pattern, 'accuracy': accuracy}  
            
        return self.pattern

    # API(s)
    def api(self, use = 0):

        # checking if `use` is in range 
        if use > -1 and use < 6:

            if use == 0: # info
                return '[simpex-info: (available api) `1:saasbase.dev`, `2:autoregex.xyz`, `3:regex.ai`, `4:regex.murfasa.com`]'

            elif use == 1:
                # sending request
                response = requests.post('https://saasbase.dev/api/tools/regex-generator', data={"input":self.data_set} if type(self.data_set) == str else {"input":self.data_set[0]})
                
                # checking response
                if response.status_code == 200:
                    self.pattern = str(json.loads(response.json()['answer'])['regex'])
                else:
                    return '[simpex-err: api (1) error]'
                
            elif use == 2:
                # post request payload
                if type(self.data_set) == list:
                    payload = {"message":self.data_set[0],"isEnglish":'true'}
                elif type(self.data_set) == str:
                    payload = {"message":self.data_set,"isEnglish":'true'}

                # sending request
                response = requests.post('https://www.autoregex.xyz/api/gptv2', data = payload)

                # checking response
                if response.status_code == 200:
                    self.pattern = str(response.json()['message'])
                else:
                    return '[simpex-err: api (2) error]'

            elif use == 3:
                # post request payload
                if type(self.data_set) == list:
                    payload = {"prompt":self.data_set[0]}
                elif type(self.data_set) == str:
                    payload = {"prompt":self.data_set}

                # sending request
                response = requests.post('https://regex.murfasa.com/api/', json=payload)

                # checking response
                if response.status_code == 200:
                    self.pattern = str(response.json()['bot'])
                else:
                    return '[simpex-err: api (3) error]' 

            elif use == 4:
                # post request payload
                if type(self.data_set) == list:
                    payload = '{\"user_text\":\"'+self.data_set[0].replace('\n', '\\n')+'\", \"user_highlight\":[]}'
                elif type(self.data_set) == str:
                    payload = '{\"user_text\":\"'+self.data_set.replace('\n', '\\n')+'\", \"user_highlight\":[]}'
                
                # sending request
                response = requests.post('https://regex.ai/api/run', data=payload)
                
                # checking response
                if response.status_code == 200:
                    self.pattern = [str(i).replace('\n', '') for i in response.json()['agent_output']]
                else:
                    return '[simpex-err: api (4) error]' 

        else:
            return '[simpex-err: api selector out of range (1-4)]'
        

        return self.pattern

    # built-in patterns
    def pattern(self, pattern):
        if pattern == 'LIST':
            return '[simpex-info: (available patterns) `email`, `phone`, `url`, `ipv4`, `ipv6`, `mac`, `credit_card`]'
        elif pattern == 'email':
            return r'^[a-zA-Z0-9\_\-]+@[a-zA-Z0-9\_\-]+\.[a-zA-Z0-9]*'
        elif pattern == 'phone': # +1 123 456 7890, +1-123-456-7890, +91234567890, 123 456 7890, 123-456-7890, 1234567890
            return r'^(\+?\d{1,2}\s?)?([\s\-]?\d{1,3}|\(\d{1,4}\))[\s\-]?\d{1,4}[\s\-]?\d{2,4}$'
        elif pattern == 'url': # http(s), subdomains, subdirectories
            return r'^(http(s)?:\/\/)?[a-zA-Z0-9\-\_]+\.?[a-zA-Z0-9\-\_]+\.[a-zA-Z0-9\-\_]+(\/[a-zA-Z0-9\-\_]+)*'
        elif pattern == 'ipv4': # 192.168.0.1, 127.0.0.1
            return r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        elif pattern == 'ipv6': # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
            return r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        elif pattern == 'mac': # ff:ff:ff:ff:ff:ff
            return r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        elif pattern == 'credit_card': # 1234-1234-1234-1234, 1234123412341234
            return r'^(\d{4}-){3}\d{4}|\d{16}$'
        else:
            return '[simpex-err: pattern not found]'

