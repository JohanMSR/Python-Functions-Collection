def read_file(filename: str) -> str:
    """Read contents of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")

def write_file(filename: str, content: str) -> None:
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename: str, content: str) -> None:
    """Append content to a file."""
    with open(filename, 'a') as file:
        file.write(content) 