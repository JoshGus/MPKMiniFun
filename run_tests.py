import subprocess
import sys


def run_tests():
    print("Running tests...\n")

    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("Tests failed")
    else:
        print("All tests passed")


if __name__ == "__main__":
    run_tests()