import random

# The Coin class simulates a coin that can be flipped.
class Coin:
    # The __init__ method initializes the data attributes.
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value of sideup.
    def get_sideup(self):
        return self.sideup

def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin ...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

# Call the main function.
main()
