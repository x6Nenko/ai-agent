#!/usr/bin/env python3
import subprocess
import sys


def run_test(description, prompt, verbose=True):
    """Run a test by executing main.py with the given prompt."""
    print(f"\n{'='*60}")
    print(f"TEST: {description}")
    print(f"PROMPT: {prompt}")
    print(f"{'='*60}")

    cmd = ["python3", "main.py", prompt]
    if verbose:
        cmd.append("--verbose")

    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

    if result.returncode != 0:
        print(f"ERROR: Process exited with code {result.returncode}")
        return False

    return True


def main():
    print("Testing AI Agent Functions")
    print("="*60)

    tests = [
        ("List directory contents", "List the files in the current directory"),
        ("Get file contents", "Show me the contents of add.py"),
        ("Write new file", "Create a new file called test_output.txt with the content 'This is a test file created by the AI agent'"),
        ("Run Python tests", "Execute the tests.py file"),
    ]

    passed = 0
    failed = 0

    for description, prompt in tests:
        if run_test(description, prompt, verbose=True):
            passed += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    print(f"{'='*60}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
