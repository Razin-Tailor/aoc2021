def main(data: list) -> int:
    answer = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            answer += 1
    print(answer)
    return 0


if __name__ == "__main__":
    fpath = "./input.txt"
    with open(fpath, "r") as f:
        data = f.readlines()
    data = [int(x.strip()) for x in data]
    raise SystemExit(main(data))
