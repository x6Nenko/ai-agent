from functions.write_file import write_file
from functions.run_python_file import run_python_file


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

    # Test 4: Run Python file without arguments (should print usage instructions)
    print("Test 4: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(result)
    print()

    # Test 5: Run Python file with arguments
    print("Test 5: run_python_file('calculator', 'main.py', ['3 + 5'])")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print()

    # Test 6: Run tests.py
    print("Test 6: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()

    # Test 7: Try to run file outside working directory (should error)
    print("Test 7: run_python_file('calculator', '../main.py')")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print()

    # Test 8: Try to run nonexistent file (should error)
    print("Test 8: run_python_file('calculator', 'nonexistent.py')")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print()


if __name__ == "__main__":
    main()
