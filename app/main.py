import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]
    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)
    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    with open(source, "r") as f_in, open(destination, "w") as f_out:
        f_out.write(f_in.read())

    os.remove(source)
