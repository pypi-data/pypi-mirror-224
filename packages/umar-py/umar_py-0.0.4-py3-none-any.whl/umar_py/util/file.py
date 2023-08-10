import os


def read_files(dir_path: str, ext: str | None = None):
    """
    Reads and yields the contents of files from a directory, optionally filtered by extension.

    Args:
        dir_path (str): The path to the directory containing the files.
        ext (str | None, optional): The optional extension to filter files. Default is None.

    Yields:
        str: The contents of files in the directory, sorted by filename's numeric prefix.

    Example:
        To read all '.txt' files from the 'data' directory:
        >>> for content in read_files('data', ext='.txt'):
        ...     print(content)
    """
    file_names = os.listdir(dir_path)

    if ext:
        file_names = [file_name for file_name in file_names if file_name.endswith(ext)]

    sorted_file_names = sorted(file_names, key=lambda x: int(x.split('.')[0]))

    for file_name in sorted_file_names:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r') as file:
            yield file.read()
