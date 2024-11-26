def solution(number: str, requests: list[str]) -> list[int]:
    number = list(number)[::-1]
    one_count = number.count("1")
    one_count_history = []

    for request in requests:
        if request == "?":
            one_count_history.append(one_count)
        else:
            carry = True
            for i, digit in enumerate(number):
                if not carry:
                    continue
                elif digit == "0":
                    number[i] = "1"
                    carry = False
                    one_count += 1
                elif digit == "1":
                    number[i] = "0"
                    carry = True
                    one_count -= 1

            if carry:
                number.append("1")
                one_count += 1

    return one_count_history
