def solution(s: str):
    ditcionray = {"zero": 0,
                  "one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9	}

    # while True:
    #     isEnd = False

    for _ in range(3):
        for key in ditcionray:
            num = ditcionray[key]
            a = s.find(key)
            if a > -1:
                s = s[:a] + str(num) + s[len(key):]
                print(s[:a], str(num), s[len(key):])
                print(_, s)

                break
            # if isEnd:

                # break


solution("one4seveneight")
