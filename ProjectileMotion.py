"""Gets user input to determine the height and time a ball will 
hit the groud using user input for initial height and velocity in feet per second."""

# --------------------
# Lucas Bigler
# CS 1300
# 3/7/2023
# ---------------------


def mainFunction():
    # Analyze projectile motion using other defs inside this main function.
    h, v = userInput()
    print("The maximum height of the ball will be " +
          "{0:.2f} feet.".format(calculateMaximumHeight(h, v)))
    print("The ball will slam against the ground after approximately " +
          "{0:.2f} seconds.".format(timeToHitGround(h, v)))


def userInput():
    """Gathers user input

    Returns:
        Int: Both the initial height and velocity as integers
    """
    # Takes in user input + creative element of doing input
    # checking for a number instead of a character or word
    h = input("Enter the initial height of the ball: ")
    while not h.isdigit():
        print("Please enter a number instead of a character!")
        h = input("Enter the initial height of the ball: ")

    v = input("Enter the initial velocity of the ball: ")
    while not v.isdigit():
        print("Please enter a number instead of a character!")
        v = input("Enter the initial velocity of the ball: ")

    # Changes the string "numbers" to actual numbers so other functions can use them.
    h = int(h)
    v = int(v)
    return h, v


def heightOfBall(h, v, t):
    """Returns height of ball after t seconds

    Args:
        h (Int): Initial height gathered from the user
        v (Int): Initial velocity gathered from the user
        t (Int): Time in seconds

    Returns:
        Float: Height of ball after t seconds
    """
    # Return height of ball after t seconds
    return h + v * t - 16 * t * t


def calculateMaximumHeight(h, v):
    """Returns the maximum height of the ball.

    Args:
        h (Int): Initial height gathered from the user
        v (Int): Initial velocity gathered from the user

    Returns:
        Float: Maximum height of ball
    """
    return heightOfBall(h, v, v / 32)


def timeToHitGround(h, v):
    """Calculates the time when the ball will hit the ground

    Args:
        h (Int): Initial height gathered from the user
        v (Int): Initial velocity gathered from the user

    Returns:
        Float: Time when ball hits the ground
    """
    t = .01
    while heightOfBall(h, v, t) >= 0:
        t += .01
    return t


mainFunction()
