from functions.get_file_content import get_file_content


def main():
    # Test 1: Read main.py
    print("Test 1: get_file_content('calculator', 'main.py')")
    result = get_file_content("calculator", "main.py")
    print(result)
    print()

    # Test 2: Read pkg/calculator.py
    print("Test 2: get_file_content('calculator', 'pkg/calculator.py')")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print()

    # Test 3: Try to read outside working directory (should error)
    print("Test 3: get_file_content('calculator', '/bin/cat')")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

    # Test 4: Try to read non-existent file (should error)
    print("Test 4: get_file_content('calculator', 'pkg/does_not_exist.py')")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print()


if __name__ == "__main__":
    main()
