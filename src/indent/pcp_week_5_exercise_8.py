# Exercise 8
class Human:
    def __init__(self, sex, age, bone_length):
        self.sex = sex
        self.age = age
        self.bone_length = bone_length


def b_length(human: Human) -> float:
    # indentation can be different in each code block, but it can disturb the readability!
    if human.sex == "m":
     height = 69.089 + 2.238 * human.bone_length
    elif human.sex == "w":
        height = 61.412 + 2.317 * human.bone_length
    if human.age < 30:
        return round(height, 2)
    else:
            age_difference = human.age - 30
            height_lost = age_difference * 0.06
            return round(height - height_lost, 2)


def main():
    old_human = Human("m", 80, 45)
    print(b_length(old_human))
    young_human = Human("m", 23, 45)
    print(b_length(young_human))


if __name__ == '__main__':
    main()
