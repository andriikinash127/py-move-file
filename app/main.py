import os


def move_file(command: str) -> None:
    list_of_comands = command.split()
    if len(list_of_comands) != 3 or list_of_comands[0] != "mv":
        return
    _, source, destination = list_of_comands
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source, "r") as file_1, open(destination, "w") as file_2:
        file_2.write(file_1.read())
    os.remove(source)
