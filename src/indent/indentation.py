def temperature(temperature: int) -> str:
    if temperature > -273:
        # indention can be different in each code block
                if temperature > 35:
                    return "hot"
                elif 25 < temperature < 35:
                    return "warm"
                elif 15 < temperature < 25:
                    return "medium"
                else:
                    return "cold"
    else:
        return "not possible!"


def main():
    print(temperature(-100))
    print(temperature(30))
    print(temperature(16))


if __name__ == '__main__':
    main()


# Java example of temperature function
#
# public String temperature(int temp){
#         if(temp > -273) {
#             if(temp > 35) {
#                 return "hot";
#             } else if(temp > 25 && temp < 35) {
#                 return "warm";
#             } else if(temp > 15 && temp < 25) {
#                 return "medium";
#             } else {
#                 return "cold";
#             }
#         } else{
#             return "not possible!";
#         }
#     }
