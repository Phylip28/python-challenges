def lifeDigit(birth_date):
    birth_date = (
        birth_date.replace("/", "").replace("-", "").replace(" ", "").replace("0", "")
    )
    total_sum = sum(int(number) for number in birth_date)

    return reduceToOneDigit(total_sum)


def reduceToOneDigit(total_sum):
    if total_sum > 9:
        total_sum = sum(int(number) for number in str(total_sum))
        return reduceToOneDigit(total_sum)
    else:
        return total_sum


birth_date_result = lifeDigit(input("Enter your birth date: "))
print(f"Life Digit: {birth_date_result}")
