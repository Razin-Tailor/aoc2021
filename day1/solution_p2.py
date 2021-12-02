from math import ceil


def slice(data: list, n: int) -> list:
    modified_data = []
    for i, _ in enumerate(data):
        if i < len(data) - 2:
            temp = []
            temp.append(data[i])
            temp.append(data[i + 1])
            temp.append(data[i + 2])
            modified_data.append(temp)

    modified_data = [x for x in modified_data if len(x) == n]

    return modified_data


def main(data: list) -> int:
    answer = 0
    n = 3
    modified_data = slice(data, n)
    for i in range(len(modified_data) - 1):
        if sum(modified_data[i + 1]) > sum(modified_data[i]):
            answer += 1
    print(answer)
    return 0


if __name__ == "__main__":
    fpath = "./input.txt"
    with open(fpath, "r") as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]
    raise SystemExit(main(data))
