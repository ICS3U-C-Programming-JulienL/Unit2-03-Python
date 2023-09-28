#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: September 28, 2023
# This program displays the circumference of a circle with user input

import constants


def main():
    # get the radius
    print("Calculating the Circumference of a Circle")
    radius = float(input("What is the radius of your circle (cm)?"))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("The circumference is {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
