MAX_THRESHOLD = 3
MIN_THRESHOLD = 1

########## PART 1 ##########


def is_level_safe(levels):
    previous_level = None
    inc = 0
    dec = 0

    for level in levels:
        if previous_level is None:
            previous_level = level
            continue

        diff = int(level) - int(previous_level)

        if diff < 0:
            dec += 1
        elif diff > 0:
            inc += 1
        else:
            return False

        if abs(diff) > MAX_THRESHOLD or abs(diff) < MIN_THRESHOLD:
            return False

        previous_level = level

    if inc == 0 and dec != 0:
        return True
    elif dec == 0 and inc != 0:
        return True
    else:
        return False


def read_reports():
    with open("adventofcode2024/puzzles/day2/input.txt", "r") as file:
        num_safe = 0
        for report in file.read().splitlines():
            levels = report.split()
            isSafe = is_level_safe(levels)

            if isSafe:
                num_safe += 1

        return num_safe


########## PART 2 ##########


def is_levels_safe_damp(levels):
    if is_level_safe(levels):
        return True

    for iter, level in enumerate(levels):
        temp_levels = levels.copy()
        del temp_levels[iter]
        if is_level_safe(temp_levels):
            return True

    return False


def read_reports_damp():
    with open("adventofcode2024/puzzles/day2/input.txt", "r") as file:
        num_safe = 0
        for report in file.read().splitlines():
            levels = report.split()

            if is_levels_safe_damp(levels):
                num_safe += 1

        return num_safe


def main():
    num_safe = read_reports()
    print(num_safe)  # answer part 1
    num_safe_damp = read_reports_damp()
    print(num_safe_damp)  # answer part 2


if __name__ == "__main__":
    main()
