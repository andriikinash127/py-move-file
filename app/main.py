import os


def move_file(command: str) -> None:
    list_of_comands = command.split()
    source = list_of_comands[1]
    destination = list_of_comands[2]
    if list_of_comands[0] != "mv":
        return
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source, "r") as file:
        counter = file.read()
    with open(destination, "w") as file:
        file.write(counter)
    os.remove(source)
