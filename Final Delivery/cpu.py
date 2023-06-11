import os
import sys
import time

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

curr_route = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curr_route, 'instructions.asm')
save_file = os.path.join(curr_route, 'save.txt')

enable_saving = True
enable_default_postition = True

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class coord:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, target):
        return coord(self.x + target.x, self.y + target.y) 
    
    def __sub__(self, target):
        return coord(self.x - target.x, self.y - target.y) 
    
    def __mul__(self, const):
        return coord(self.x * const, self.y * const)
    
    __rmul__ = __mul__

    def __lt__(self, const):
        if self.x < const and self.y < const: return True
        return False
    
    def __le__(self, const):
        if self.x <= const and self.y <= const: return True
        return False
    
    def __gt__(self, const):
        if self.x > const and self.y > const: return True
        return False
    
    def __ge__(self, const):
        if self.x >= const and self.y >= const: return True
        return False
    
    def __eq__(self, const):
        if self.x == const and self.y == const: return True
        return False
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def set(self, n_coord):
        self = n_coord

pos = coord(5, 5)
curr_dir = 0

if os.path.exists(save_file):
    with open(save_file, "r") as file:
        lines = file.readlines()
        pos_vec = lines[0].split(",")
        n_dir = int(lines[1])
        file.close()
    pos = coord(int(pos_vec[0]), int(pos_vec[1]))
    curr_dir = n_dir
else:
    with open(save_file, "w") as file:
        file.write("5,5")
        file.close()
    pos = coord(5, 5)

if enable_default_postition:
    pos = coord(5, 5) # Debug set coordinates to default
    curr_dir = 0 # Debug set coordinates to default
dir = [coord(1, 0), coord(0, 1), coord(-1, 0), coord(0, -1)]

def print_table(pos, curr_dir):
    clear_terminal()

    print("╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗")
    for y in range(1, 11):
        print("║", end="")
        for x in range(1, 11):
            curr = coord(x, y)

            if curr.x == pos.x and curr.y == pos.y:
                if curr_dir == 0: print("  ▶  ║", end="")
                elif curr_dir == 1: print("  ▼  ║", end="")
                elif curr_dir == 2: print("  ◀  ║", end="")
                elif curr_dir == 3: print("  ▲  ║", end="")
            else:
                print("     ║", end="")

        print()
        if y < 10: print("╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣")
        else: print("╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝")

def move(pos, curr_dir):
    print_table(pos, curr_dir)

    with open(input_file, "r") as file:
        lines = file.readlines()

        for line in lines:
            instr = line.split(",")
            instr[1] = instr[1].split("\n")[0]
            
            time.sleep(1)

            if instr[0] == "MOV":
                amount = int("0" + instr[1])

                f_pos = pos
                for i in range(amount):
                    n_pos = pos + dir[curr_dir]
                    if n_pos < 11 and n_pos >= 1:
                        pos = n_pos
                        print_table(pos, curr_dir)
                        time.sleep(1)
                        continue
                    pos = f_pos
                    print_table(pos, curr_dir)
                    print("<< Movimiento Incorrecto >>")
                    return pos, curr_dir

                continue

            if instr[0] == "TURN":
                if instr[1] == "360": continue

                if instr[1] == "90": 
                    curr_dir += 1
                elif instr[1] == "180":
                    curr_dir += 2
                elif instr[1] == "270":
                    curr_dir += 3
                else:
                    print("Incorrect angle")

                if curr_dir > 3:
                    curr_dir = (curr_dir - 3) - 1

                
                print_table(pos, curr_dir)
                continue

        file.close()

    return pos, curr_dir

pos, curr_dir = move(pos, curr_dir)

if enable_saving:
    with open(save_file, "w") as file:
        print("Saving...")
        print(f"New position: {pos}")
        print(f"New direction: {curr_dir}")
        file.write(f"{pos.x},{pos.y}\n{curr_dir}")
        file.close()
