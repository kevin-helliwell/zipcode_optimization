def main():
    states0 = ["CT", "MA", "ME", "NH", "NJ", "RI", "VT"]
    states1 = ["DE", "NY", "PA"]
    states2 = ["MD", "NC", "SC", "VA", "WV"]
    states3 = ["AL", "FL", "GA", "MS", "TN"]
    states4 = ["IN", "KY", "MI", "OH"]
    states5 = ["IA", "MN", "MT", "ND", "SD", "WI"]
    states6 = ["IL", "KS", "MO", "NE"]
    states7 = ["AR", "LA", "OK", "TX"]
    states8 = ["AZ", "CO", "ID", "NM", "NV", "UT", "WY"]
    states9 = ["AK", "CA", "HI", "OR", "WA"]
    zip_to_states = {0: states0, 1: states1, 2: states2, 3: states3,
                     4: states4, 5: states5, 6: states6, 7: states7,
                     8: states8, 9: states9}

    user_input = input("Please enter a zipcode.\n")
    zip_digit = user_input[0]
    list = []
    match zip_digit:
        case "0":
            borders = (0, 1)
        case "1":
            borders = (1, 2, 4)
        case "2":
            borders = (1, 2, 3, 4)
        case "3":
            borders = (2, 3, 4, 6, 7)
        case "4":
            borders = (1, 2, 3, 4, 5, 6)
        case "5":
            borders = (4, 5, 6, 8)
        case "6":
            borders = (3, 4, 5, 6, 7, 8)
        case "7":
            borders = (3, 6, 7, 8)
        case "8":
            borders = (5, 6, 7, 8, 9)
        case "9":
            borders = (8, 9)
        case _:
            raise Exception("Not a zipcode")
    for border in borders:
        list.extend(zip_to_states[border])
    print(list, len(list))


if __name__ == '__main__':
    main()
