from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info


def main():
    # Test 1: "read the contents of main.py" -> get_file_content({'file_path': 'main.py'})
    print("Test 1: get_file_content('.', 'main.py')")
    result = get_file_content(".", "main.py")
    print(result)
    print()

    # Test 2: "write 'hello' to main.txt" -> write_file({'file_path': 'main.txt', 'content': 'hello'})
    print("Test 2: write_file('.', 'main.txt', 'hello')")
    result = write_file(".", "main.txt", "hello")
    print(result)
    print()

    # Test 3: "run main.py" -> run_python_file({'file_path': 'main.py'})
    print("Test 3: run_python_file('.', 'main.py')")
    result = run_python_file(".", "main.py")
    print(result)
    print()

    # Test 4: "list the contents of the pkg directory" -> get_files_info({'directory': 'pkg'})
    print("Test 4: get_files_info('.', 'pkg')")
    result = get_files_info(".", "pkg")
    print(result)
    print()


if __name__ == "__main__":
    main()
