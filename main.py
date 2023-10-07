import random
def print_welcome(name):
    print(f'Hi {name}', 'Here are some fantasy names:')

def generate_first_name():
    generated_name = ""
    syllabel_count = range(random.randint(2,4))
    syllabels = ["al", "la", "wa", "ko", "vi", "fe", "tro"]
    for syllabel in syllabel_count:
        generated_name += syllabels[random.randint(0, 6)]
    return generated_name

def generate_last_name():
    generated_last_name = ""
    last_name1 = ["snake", "fish", "bird", "bear", "bronze", "silver", "huge"]
    last_name2 = ["hands", "eyes", "eye", "beard", "feet", "foot", "wind"]
    generated_last_name = last_name1[random.randint(0, 6)] + last_name2[random.randint(0, 6)]
    return generated_last_name

def print_generated_name():
    print(generate_first_name() + " " + generate_last_name())

print_welcome('Luke')
print_generated_name()
print_generated_name()
print_generated_name()