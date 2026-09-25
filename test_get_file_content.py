from functions.get_file_content import get_file_content


def test() -> None:
    print("")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    result = get_file_content("calculator", "main.py")
    print(f"main.py: {result}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"pkg/calculator.py: {result}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print(f"/bin/cat: {result}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"pkg/does_not_exist.py: {result}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("")


if __name__ == "__main__":
    test()
