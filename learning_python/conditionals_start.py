#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    elif (x== y):
        st = "both the same!!"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"

if __name__ == "__main__":
    main()

def inputConditional():
    x = input("Enter x number here: ")
    y = input("Enter y number here: ")
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(st)

inputConditional()
