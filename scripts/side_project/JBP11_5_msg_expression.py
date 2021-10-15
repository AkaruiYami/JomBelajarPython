"""Generate message base on the number of people in given list.

    Receive a list of people's name.
    Output message based on the list.
    If there is 4 or more names in the list, only show 2 names.

    Example 1:
        Input:
        
        > Ahmad, Amir, Rasyid

        Output:

        > Hello, Ahmad, Amir and Rasyid.

    Example 2:
        Input:

        > Ahmad, Amir, Rasyid, Sabri, Hamzah

        Output:

        > Hello, Ahmad, Amir and 3 others.

"""


def get_response(list_people):
    msg = {
        1: "Hello, {}.",
        2: "Hello, {} and {}.",
        3: "Hello, {}, {}, and {}.",
        4: "Hello, {}, {} and {n_other} others.",
    }
    return msg[min(4, len(list_people))].format(
        *list_people[:3], n_other=len(list_people[2:])
    )


if __name__ == "__main__":
    names = input().split(",")
    names = [name.strip() for name in names]
    msg = get_response(names)
    print(msg)
