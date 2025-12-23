def get_num_words(contents):
    num_words = len(contents.split())
    return num_words

def get_character_count(contents):
    character_count = {}
    for c in contents:
        c = c.lower()
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def get_character_list(character_count):
    character_count_report = []
    for key,value in character_count.items():
        if key.isalpha():
            character_count_report.append({"char": key, "num": value})
    return character_count_report

def sort_on(items):
    return items["num"]

def sort_character_list(character_list):
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    


