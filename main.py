import random
def print_welcome(name):
    print(f'Hi {name}', 'Here are some fantasy names:')

def generate_name():
    generated_name = ""
    syllabel_count = range(random.randint(2,4))
    syllabels = ["al", "la", "wa", "ko", "vi", "fe", "tro"]
    for syllabel in syllabel_count:
        generated_name += syllabels[random.randint(0, 6)]
    print(generated_name)

print_welcome('Luke')

generate_name()
generate_name()
generate_name()