from functions.write_file import write_file


def main():
    # Test 1: Write to existing file
    print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn\\'t lorem ipsum')")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print()

    # Test 2: Write to new file with nested directory
    print("Test 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print()

    # Test 3: Try to write outside working directory (should error)
    print("Test 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print()


if __name__ == "__main__":
    main()
