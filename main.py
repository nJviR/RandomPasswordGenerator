from Generator.Generator import Generator

def main() -> int:
    len_num = int(input("Enter a number from 0 to 50: "))
    if len_num <= 0 or len_num >= 50:
        print("Try entering a different number")
    else:
        gener = Generator(len_num)
        print(f"{gener.createpass()}")

    return 0

if __name__ == "__main__":
    main()
