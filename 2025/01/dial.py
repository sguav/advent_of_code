import os
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))


class Dial:
    """
    The base class representing our dial
    """

    def __init__(self):
        self.head = 50
        self.zero_counter = 0
        self.zero_clicks = 0
        self.__overflow_thresh__ = 99
        self.__underflow_thresh__ = 0
        print("Dial created, starting at: ", self.head)

    """ Addition for our dial
        Automatically consider overflow
        and add it to click counts
    """
    def add(self, amount):
        amount = int(amount)
        until_zero = (self.__overflow_thresh__ + 1) if self.head == 0 else ((self.__overflow_thresh__ + 1) - self.head) % (self.__overflow_thresh__ + 1)

        if amount <= until_zero:
            zero_clicks = 0
        else:
            zero_clicks = 1 + (amount - until_zero - 1) // (self.__overflow_thresh__ + 1)

        if zero_clicks:
            print(f"-- The dial CLICKED through zero {zero_clicks} times  -- |", end='')
            self.zero_clicks += zero_clicks

        raw = self.head + int(amount)
        # Modulus operation on dial
        self.head = (raw) % (self.__overflow_thresh__ + 1)
        self.zero_counter += 1 if self.head == 0 else 0

    """ Subtraction for our dial
        Automatically consider UNDERflow
        and add it to click counts
    """
    def sub(self, amount):
        amount = int(amount)
        until_zero = (self.__overflow_thresh__ + 1) if self.head == 0 else self.head

        if amount <= until_zero:
            zero_clicks = 0
        else:
            zero_clicks = 1 + (amount - until_zero - 1) // (self.__overflow_thresh__ + 1)

        if zero_clicks:
            print(f"-- The dial CLICKED through zero {zero_clicks} times  -- |", end='')
            self.zero_clicks += zero_clicks

        raw = self.head - int(amount)

        # Modulus operation on dial
        self.head = (raw) % (self.__overflow_thresh__ + 1)
        self.zero_counter += 1 if self.head == 0 else 0

    """ Add rotations as add/sub with given over/underflow limit"""
    def rotate(self, instr):
        direction = instr[0]
        amount = int(instr[1:-1])

        print(f"{direction} {amount} | ", end='')

        # Select + or - according to dir
        if direction == "L":
            # Subtract
            self.sub(amount)
        else: # Assuming it's correct, without "R" check
            # Add
            self.add(amount)

        print(f" Dial: {self.head} | Zero count: {self.zero_counter}")

def main():
    d = Dial()
    input_file = "test" if (len(sys.argv) > 1 and  sys.argv[1] == '-debug') else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        while l := f.readline():
            d.rotate(l)

    print(f"Password is zero counter = ", d.zero_counter)
    print(f"Zero clicks are = ", d.zero_clicks)
    print(f"Method 0x434C49434B password is = ", d.zero_counter + d.zero_clicks)

if __name__ == '__main__':
    import sys
    sys.exit(main())