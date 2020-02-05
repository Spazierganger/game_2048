import rotation
import random


class Tablet:
    def __init__(self):
        self.pad = [[0 for i in range(4)] for j in range(4)]
        self.add_two()
        # self.pad[1] = [4, 4, 4, 4]
        # self.pad = [[j * 4 + i for i in range(4)] for j in range(4)]

    def show_pad(self):
        for i in range(4):
            print(self.pad[i])
        print()

    def game_over(self):
        for i in range(4):
            cur_line = self.pad[i]
            if min(cur_line) == 0:
                return False
        return True

    def add_two(self):
        while True:
            row, column = random.randint(0, 3), random.randint(0, 3)
            if self.pad[row][column] == 0:
                self.pad[row][column] = 2
                break

    def local_rotation(self):
        rotation.rotate(self.pad)
        self.show_pad()

    def move_right(self):
        for i in range(4):
            cur_line = self.pad[i]
            if max(cur_line) == 0:
                continue
            # first move the numbers onto the right side
            for j in range(4):
                if cur_line[j] == 0:
                    cur_line = [cur_line[j]] + cur_line[0:j] + cur_line[j+1:]
            # then add the pairs
            for j in range(3):
                if cur_line[-1 - j] == cur_line[-2 - j]:
                    cur_line[-1 - j] *= 2
                    cur_line[0: -1 - j] = [0] + cur_line[0: -2 - j]
                elif cur_line[-2 - j] == 0:
                    break
            self.pad[i] = cur_line

    def play(self):
        while not self.game_over():
            key = input()
            if key == "w":
                for i in range(1):
                    self.local_rotation()
                self.move_right()
                for i in range(3):
                    self.local_rotation()
            elif key == "s":
                for i in range(3):
                    self.local_rotation()
                self.move_right()
                for i in range(1):
                    self.local_rotation()
            elif key == "a":
                for i in range(2):
                    self.local_rotation()
                self.move_right()
                for i in range(2):
                    self.local_rotation()
            elif key == "d":
                self.move_right()

            self.add_two()
            self.show_pad()


if __name__ == '__main__':
    new_tab = Tablet()
    new_tab.show_pad()
    new_tab.play()
