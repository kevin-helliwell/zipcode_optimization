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
    if zip_digit == "0":
        borders = (0, 1)
    if zip_digit == "1":
        borders = (1, 2, 4)
    if zip_digit == "2":
        borders = (1, 2, 3, 4)
    if zip_digit == "3":
        borders = (2, 3, 4, 6, 7)
    if zip_digit == "4":
        borders = (1, 2, 3, 4, 5, 6)
    if zip_digit == "5":
        borders = (4, 5, 6, 8)
    if zip_digit == "6":
        borders = (3, 4, 5, 6, 7, 8)
    if zip_digit == "7":
        borders = (3, 6, 7, 8)
    if zip_digit == "8":
        borders = (5, 6, 7, 8, 9)
    if zip_digit == "9":
        borders = (8, 9)
    for border in borders:
        list.extend(zip_to_states[border])
    print(list, len(list))


if __name__ == '__main__':
    main()
