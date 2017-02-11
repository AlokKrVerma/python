def draw(rows, cols):
    row = rows
    for col in range(cols+1):
        print(" --- "* cols)
        if row != 0:
            print("|    " * (rows+1))
            row -= 1


def main():
    rows = int(input("please enter the rows :"))
    cols = int(input("please enter the columns:"))
    draw(rows, cols)


if __name__ == "__main__":
    main()
