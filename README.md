# Memes for everyone

A **Python function** that gives you a set of the memes, which together are the most valuable and can fit into your USB stick.

Done for [Clearcode](https://clearcode.pl/) as a recruitment task.

## Algorithm

To solve this problem, I used solution to a 0-1 Knapsack problem with a Dynamic Programming algorithm.
This solution will run in O(nW) time and O(nW) space, where n is the number of memes and W is the USB capacity.
To see more information about algotihm, please check [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem) 

## Prerequisites

This project uses:
* **Python 3.7.1**

And following Python packages:
* **NumPy**

## Getting Started

First, you need to clone or download the repository. On Linux you can do that typing this command:
```
git clone https://github.com/AdamBukowczyk/Clearcode_intern_2019
```
Then, import the *calculate* function from *main.py* file:
```
import calculate from main
```

### How it works

Preapere the function data of following format:

```
# size of your pendrive in GiB
usb_size = 1

# a list of 3-element tuples, each with the name, size in MB, and price in caps
memes = [
        ('rollsafe.jpg', 205, 6),
        ('sad_pepe_compilation.gif', 410, 10),
        ('i_am_the_senate.gif', 605, 12)
    ]
```

Execute function:

```
calculate(usb_size, memes)
```
And get output:
```
(22, {'i_am_the_senate.gif', 'sad_pepe_compilation.gif'})
```

## Running the tests

The function was tested using **unittest** built-in module.

To run these tests, you need to typing:
```
>>> python3 tests.py
```
## Authors

* **Adam Bukowczyk**  - [AdamBukowczyk](https://github.com/AdamBukowczyk)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

* [PurpleBooth](https://gist.github.com/PurpleBooth) for creating this amazing README template