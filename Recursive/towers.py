# Implementing an algorithm that solves the Towers of Hanoi

def moveDisk(n, src, dest, recLevel):
    tab = recLevel - 1
    print(tab*"\t" + "Recursion Level = " + str(recLevel))
    print(tab*"\t" + f"Moving Disk {n} from Source {src} to Destination {dest}")
    print(tab*"\t" + "n=" + str(n) + ", src=" + str(src) + ", dest=" + str(dest) + "\n")

def _towers(n, src, dest, recLevel, steps):
    recLevel += 1
    steps += 1
    
    if (n==1):
        moveDisk(n, src, dest, recLevel)
    else:
        temp = 6-src-dest
        steps = _towers(n-1, src, temp, recLevel, steps)
        moveDisk(n, src, dest, recLevel)
        steps = _towers(n-1, temp, dest, recLevel, steps)
    return steps

def towers(n , src, dest):
    print(f"\ntowers({n}, {src}, {dest})\n")
    steps = _towers(n, src, dest, 0, 0)
    print(f"Hence, there are {steps} moves for this problem")

def main():
    print("Towers of Hanoi Program\n")
    nSuccess = False
    srcSuccess = False
    destSuccess = False

    while not nSuccess:
        try:
            n = input("How many disks (>0): ")
            n = int(n)
            if n <=0:
                raise ValueError
            nSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    while not srcSuccess:
        try:
            src = input("What is the source pin (1-3): ")
            src = int(src)
            if src<=0 or src>=4:
                raise ValueError
            srcSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    while not destSuccess:
        try:
            dest = input("What is the destination pin (1-3): ")
            dest = int(dest)
            if dest<=0 or dest>=4:
                raise ValueError
            destSuccess = True
        except ValueError:
            print("\nThat is not a valid input, please try again")

    if src == dest:
        print("\nThe disks are already in the correct position")
        print("Hence, there are 0 moves for this problem")
    else:
        towers(n, src, dest)

if __name__ == "__main__":
    main()
