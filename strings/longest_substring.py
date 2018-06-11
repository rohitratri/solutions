def longest_substring(s):
    sub_start = 0
    sub_len = 0
    longest_sub_len = sub_len
    longest_sub_start = sub_start
    char_cache = {}
    for char_pos in xrange(len(s)):
        char = s[char_pos]
        print char, char_cache, sub_start
        _prev_char_pos = char_cache.get(char)
        if not _prev_char_pos or (_prev_char_pos < sub_start):
            sub_len += 1
        else:
            if sub_len > longest_sub_len:
                longest_sub_len = sub_len
                longest_sub_start = sub_start
            sub_len = sub_len - (_prev_char_pos - sub_start)
            sub_start = _prev_char_pos + 1
        char_cache[char] = char_pos
    print longest_sub_len
    print s[longest_sub_start:longest_sub_start+longest_sub_len]

longest_substring('pwwkew')
