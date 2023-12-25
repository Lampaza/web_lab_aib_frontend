def get_text_lines():
    text_lines = []
    while True:
        line = input()
        if not line:
            break
        text_lines.append(line)
    return text_lines

def count_characters(text_lines):
    text = '\n'.join(text_lines)

    char_count = {}
    maxh = 0

    lines = text.split('\n')
    for line in lines:
        for char in line:
            if char == ' ':
                continue
            char_count[char] = char_count.get(char, 0) + 1
            maxh = max(maxh, char_count[char])

    return char_count, maxh

def print_histogram(char_count, maxh):
    unique_chars = sorted(char_count.keys())

    for i in range(maxh, 0, -1):
        print(''.join('#' if char_count.get(tt, 0) >= i else ' ' for tt in unique_chars))

    print(''.join(unique_chars))

def main():
    text_lines = get_text_lines()
    char_count, maxh = count_characters(text_lines)
    print_histogram(char_count, maxh)

if __name__ == "__main__":
    main()