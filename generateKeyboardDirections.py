def generate_directions(steps, direction):
    result = []

    for i in range(steps):
        result.append(direction)

    return result


def guess_directions(current_pos, next_pos, axis):
    directions = []

    if axis == "vertical":
        if current_pos > next_pos:
            directions.extend(generate_directions(current_pos - next_pos, "up"))
        if current_pos < next_pos:
            directions.extend(generate_directions(next_pos - current_pos, "down"))

    if axis == "horizontal":
        if current_pos > next_pos:
            directions.extend(generate_directions(current_pos - next_pos, "left"))
        if current_pos < next_pos:
            directions.extend(generate_directions(next_pos - current_pos, "right"))

    return directions


def enter_text(text):
    text_arr = list(text)
    directions = []

    # starting from 'a' [0, 0]
    current_pos_i = 0
    current_pos_j = 0

    for k in range(len(text_arr)):
        try:
            char = str(text_arr[k])

            # support for uppercase characters (should use "shift" button)
            if char.isupper():
                # find index of "shift" button
                next_pos = get_character_index("shift")
                next_pos_i = next_pos[0]
                next_pos_j = next_pos[1]

                # generate directions to "shift" button
                directions.extend(guess_directions(current_pos_i, next_pos_i, "vertical"))
                directions.extend(guess_directions(current_pos_j, next_pos_j, "horizontal"))
                directions.append("select")

                # set current position into "shift" button
                current_pos_i = next_pos_i
                current_pos_j = next_pos_j

                # go back to character that should be uppercase
                next_pos = get_character_index(char)
                next_pos_i = next_pos[0]
                next_pos_j = next_pos[1]
            else:
                next_pos = get_character_index(char)
                next_pos_i = next_pos[0]
                next_pos_j = next_pos[1]

            directions.extend(guess_directions(current_pos_i, next_pos_i, "vertical"))
            directions.extend(guess_directions(current_pos_j, next_pos_j, "horizontal"))
            directions.append("select")

            k += 1
            current_pos_i = next_pos_i
            current_pos_j = next_pos_j

        except Exception as e:
            return e

    return directions


def get_character_index(char):
    result = [-1, -1]

    for i in range(len(keyboard)):
        if char.lower() in keyboard[i]:
            result[0] = i
            result[1] = keyboard[i].index(char.lower())
        else:
            continue

    if result[0] == -1 & result[1] == -1:
        raise Exception("Only symbols from defined keyboard are allowed")
    else:
        return result


def main():
    text = str(input("Enter Text:\n"))

    print(enter_text(text), "\n")

    print("Keymap is:")
    for i in range(len(keyboard)):
        print(keyboard[i])


keyboard = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'shift'],
        ['h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6', ' '],
        ['o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'backspace'],
        ['v', 'w', 'x', 'y', 'z', '-', '_', '@', '.', '0', 'enter']
    ]

main()
