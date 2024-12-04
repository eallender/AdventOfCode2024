def read_locationID():
    list1 = []
    list2 = []

    with open("adventofcode2024/puzzles/day1/input.txt", "r") as file:
        lines = file.read().splitlines()

        for line in lines:
            words = line.split()
            list1.append(words[0])
            list2.append(words[1])

    return list1, list2


def sort_locationID(list1, list2):
    list1.sort()
    list2.sort()

    return list1, list2


def get_distance(list1, list2):
    dist = 0

    for iter in range(len(list1)):
        dist += abs(int(list1[iter]) - int(list2[iter]))

    return dist


def get_similarity_score(list1, list2):
    score = {}
    for item in list1:
        score[item] = 0

    for item in list2:
        if item in score:
            score[item] += 1

    return score


def compute_score(score):
    sum = 0
    for key in score:
        sum += score[key] * int(key)

    return sum


def main():
    list1, list2 = read_locationID()
    list1, list2 = sort_locationID(list1, list2)
    dist = get_distance(list1, list2)
    print(dist)  # part 1 answer

    score = get_similarity_score(list1, list2)
    sum = compute_score(score)
    print(sum)  # part 2 answer


if __name__ == "__main__":
    main()
