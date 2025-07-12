def string_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    text = text.lower()
    counts = {}
    
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_character_count(char_dict):
    sorted_chars = []
    
    for char, count in char_dict.items():
        sorted_chars.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    sorted_chars.sort(reverse = True, key = sort_on)
    return sorted_chars    