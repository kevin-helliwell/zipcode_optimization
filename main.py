def main():
    zip_to_states = {0: ["CT", "MA", "ME", "NH", "NJ", "RI", "VT"], 1: ["DE", "NY", "PA"], 2: ["MD", "NC", "SC", "VA", "WV"], 3: ["AL", "FL", "GA", "MS", "TN"], 4: ["IN", "KY", "MI", "OH"], 5: [
        "IA", "MN", "MT", "ND", "SD", "WI"], 6: ["IL", "KS", "MO", "NE"], 7: ["AR", "LA", "OK", "TX"], 8: ["AZ", "CO", "ID", "NM", "NV", "UT", "WY"], 9: ["AK", "CA", "HI", "OR", "WA"]}

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
