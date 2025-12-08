import os
import sys
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))

DEBUG = (os.environ.get("DEBUG") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-debug'))
TEST = (os.environ.get("TEST") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-test'))
# print(f"Debug env var is {DEBUG}")

def debugprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def testprint(*args, **kwargs):
    if TEST:
        print(*args, **kwargs)

class TachyonBeam:
    """
    Represents the instant of a tachyon beam as per problem
    Has method to update the resulting splitting
    """

    def __init__(self, manifold) -> None:
        testprint("> Initializing tachyon beam:")
        self.manifold = manifold
        self.height = len(manifold)
        self.width = len(manifold[0])
        self.beam = [0] * self.width
        self.split_cnt = 0
        testprint(f">> Acquired width: {self.width}  | Split count = {self.split_cnt}")
        # self.beam[len(self.beam)//2] = 1 # I think we can skip this init and check where 'S' is
        for i, c in enumerate(manifold[0]):
            if c == "S":
                self.beam[i] = 1
        testprint(f">> Calibrated beam start point:\n   {self.beam}")

    def split_beam(self, index):
        if self.beam[index]:
            if not self.beam[index - 1]:
                self.beam[index - 1] = 1
            if not self.beam[index + 1]:
                self.beam[index + 1] = 1
            self.split_cnt += 1
            self.beam[index] = 0

    def tick_splitter(self, manifold_line):
        if len(manifold_line) != self.width:
            print(f"! ERROR: Manifold line is wrong width ({len(manifold_line)} != {self.width})")
        for idx,c in enumerate(manifold_line):
            if c == '^':
                if self.beam[idx]:
                    self.split_beam(idx)
                    testprint(f">> Split beam at {idx} on tachyon '{c}' splitter | {self.split_cnt}")
            else:
                continue

    def beam_manifold(self):
        testprint("> Start tachyon beam split through manifold:")
        for line in self.manifold[1:]:
            self.tick_splitter(line)
        testprint("> Done splitting tachyon beam through manifold")

    def quantum_split(self):
        """
        Count total 'quantum' timelines (part 2)
        (DP)
        """
        height = self.height
        width = self.width

        # Find start position of S
        for idx, ch in enumerate(self.manifold[0]):
            if ch == "S":
                start_beam = idx
                break
        else:
            raise ValueError("No starting S found")

        # ways[idx] = how many timelines reach column idx at current row
        ways = [0] * width
        ways[start_beam] = 1

        total = 0  # timelines that exit off-grid

        for row in range(0, height - 1):
            next_ways = [0] * width
            next_row = self.manifold[row + 1]

            for idx, n in enumerate(ways):
                if n == 0:
                    continue

                if next_row[idx] == "^":
                    # left branch
                    lc = idx - 1
                    if lc < 0:
                        total += n # One timeline, as it exits the manifold
                    else:
                        next_ways[lc] += n

                    # right branch
                    rc = idx + 1
                    if rc >= width:
                        total += n # One timeline, as it exits the manifold
                    else:
                        next_ways[rc] += n

                else:
                    # go straight
                    next_ways[idx] += n

            ways = next_ways

        # At final row, all paths exit
        total += sum(ways)
        return total


def main():

    lines = []

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        for l in f:
            lines.append(l.strip())

    # testprint(lines)

    beam = TachyonBeam(manifold=lines)
    beam.beam_manifold()
    testprint(f"   {beam.beam}")
    print(f"Beam has split {beam.split_cnt} times")
    # Part 1: 1687

    print(f"Beam splits worlds {beam.quantum_split()} times")
    # Part 2: 8811937976367


if __name__ == '__main__':
    import sys
    sys.exit(main())