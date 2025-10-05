from functions.get_files_info import get_files_info


def main():
    # Test 1: Current directory
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print()

    # Test 2: Subdirectory
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    # Test 3: Absolute path outside working directory
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(f"    {result}")
    print()

    # Test 4: Relative path outside working directory
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(f"    {result}")


if __name__ == "__main__":
    main()
