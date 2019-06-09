import numpy as np


def calculate(usb_size: int, memes: list):
    """
    Function that choose most valued set of memes for USB stick.
    Algorithm: dynamic solution of 0/1 knapsack problem.

    Parameters
    ----------
    usb_size : int
        The capacity of the USB stick in GiB.
    memes : list
        A list of 3-element tuples, each with the name, size in MiB,
        and price in caps per meme.

    Raises
    ------
    TypeError : usb_size is not int type
        Raise when parameter usb_size is not an int type.
    TypeError : memes is not a list
        Raise when parameter memes is not a list.
    TypeError : Wrong amount of an arguments inside a tuple
        Raise when one or more tuple inside a memes list has
        wrong amount of arguments.
    TypeError : Wrong data type of an argument inside a tuple
        Raise when one or more tuple inside a memes list has
        wrong type of arguments.


    Returns
    -------
    usb_content : tuple
        Solution consisting of a tuple with the total value of the memes used
        and a set of names of the used memes that should be used to maximize
        USB value.
    """

    # checks the correctness of parameters
    if type(usb_size) is not int:
        raise TypeError("usb_size is not an int type")

    if type(memes) is not list:
        raise TypeError("memes is not a list.")

    for meme in memes:
        if len(meme) != 3:
            raise TypeError("Wrong amount of the arguments inside a tuple.")
        elif not(
                isinstance(meme[0], str) and
                isinstance(meme[1], int) and
                isinstance(meme[2], int)
                ):
            raise TypeError("Wrong data type of an argument inside a tuple.")

    # or (meme[1] is not int) or (meme[2] is not int):
    # preapering data for solution
    # sorting memes table by capacity
    memes.sort(key=lambda memes: (memes[1]))
    # conversion from GiB to MiB
    usb_size *= 1024
    # init a two dimensional matrix filled by zeros,
    # needed to dynamic solution of problem
    matrix = np.zeros((len(memes), usb_size+1))

    # uses a Dynamic Programming Algorithm for a Knapsack 0-1 problem
    # m = matrix row representing memes
    # c = matrix column representing capacity
    for m in range(len(memes)):
        for c in range(usb_size + 1):
            if c < memes[m][1]:
                matrix[m][c] = matrix[m-1][c]
            else:
                matrix[m][c] = max(
                    memes[m][2] + matrix[m-1][c-memes[m][1]],
                    matrix[m-1][c]
                    )

    # the best posible price of USB
    best_price = int(matrix[len(memes) - 1][usb_size])

    # retrieving the memes names
    best_memes = set()
    c = usb_size

    for m in range(len(memes) - 1, 0, -1):
        if matrix[m][c] != matrix[m - 1][c]:
            best_memes.add(memes[m][0])
            c -= memes[m][1]
    if matrix[0][c] != 0:
        best_memes.add(memes[0][0])

    # solution of the problem
    return (best_price, best_memes)


if __name__ == '__main__':
    usb_size = 1
    memes = [
        ('rollsafe.jpg', 205, 6),
        ('sad_pepe_compilation.gif', 410, 10),
        ('yodeling_kid.avi', 605, 12)
    ]
    try:
        print(calculate(usb_size, memes))
    except TypeError as error:
        print(error)
