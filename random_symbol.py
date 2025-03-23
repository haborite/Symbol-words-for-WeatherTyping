import random

def get_random_char():
    return random.choice("#$`'\"_")

def get_random_char2():
    return random.choice("({[@")

def get_random_closing_char(opening_char):
    pairs = {"'": "'", '"': '"', '`': '`'}
    return pairs.get(opening_char, random.choice("\%:*=+-/,<>|&~^"))

def get_random_closing_char2(opening_char):
    pairs = {"(": ")", "[": "]", "{": "}"}
    return pairs.get(opening_char, random.choice("!%;.?"))

def format_line(line):
    if line[-1] in "+-=*\/<>|&~^%":
        return line[:-1] + " " + line[-1]
    else:
        return line[:-1] + random.choice("abcdefghijklmnopqrstuvwxyz01234567890123456789") + line[-1]

def format_line2(line):
    if line[-1] in "+-=*\/<>|&~^":
        return line[:-1] + " " + line[-1]
    elif line[-1] in "%":
        return line[:-1] + random.choice("01234567890123456789") + line[-1]
    else:
        return line[:-1] + random.choice("abcdefghijklmnopqrstuvwxyz01234567890123456789") + line[-1]

def generate_section(lines, prefix_space=False):
    section = []
    for _ in range(lines // 2):
        first_char = random.choice([random.choice("0123456789"), get_random_char()])
        middle = f"{random.randint(1000, 9999)}"
        last_char = get_random_closing_char(first_char)
        line = f"{first_char}{middle}{last_char}"
        if prefix_space:
            line = " " + line
        line = format_line(line)
        section.append(line)
        section.append(line)  # Duplicate the line
    return "\n".join(section)

def generate_section2(lines, prefix_space=False):
    section = []
    for _ in range(lines // 2):
        first_char = random.choice([random.choice("0123456789"), get_random_char2()])
        middle = f"{random.randint(1000, 9999)}"
        last_char = get_random_closing_char2(first_char)
        line = f"{first_char}{middle}{last_char}"
        if prefix_space:
            line = " " + line
        line = format_line2(line)
        section.append(line)
        section.append(line)  # Duplicate the line
    return "\n".join(section)

# Generate sections
section_A = generate_section(2000)
section_B = "\n"
section_C = generate_section2(2000, prefix_space=True)

# Combine and save to file
output_text = f"{section_A}\n{section_B}{section_C}"

with open("symbols.txt", "w", encoding="utf-8") as file:
    file.write(output_text)