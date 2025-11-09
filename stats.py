def total_words(content):
    num_words = len(content.split())
    return f"Found {num_words} total words"

def char_count(content):
    chars = {}
    for c in content:
        if c.lower() in chars:
            chars[c.lower()] = chars[c.lower()] + 1
        else:
            chars[c.lower()] = 1
    return chars

def sort_on(items):
    return items['num']

def list_dict(char_dict):
    list_char_dict = []
    for c in char_dict:
        list_char_dict.append({
            'char': c,
            'num': char_dict[c],
        })
    list_char_dict.sort(reverse=True, key=sort_on)
    return list_char_dict