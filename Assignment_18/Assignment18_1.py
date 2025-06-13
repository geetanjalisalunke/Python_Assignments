import os

def main():
    print("Enter the name of file that you want to read")
    filename = input().strip()

    ret = os.path.exists(filename)
    print("Exists:", ret)

if __name__ == "__main__":
    main()
