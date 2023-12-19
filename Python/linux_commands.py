import subprocess
import shlex


class LinuxCommander:

    def list_items(self, directory="."):
        cmd = f"ls {shlex.quote(directory)}"
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

    def move_or_copy(self, source, destination, is_copy=False):
        if is_copy:
            cmd = f"cp -r {shlex.quote(source)} {shlex.quote(destination)}"
        else:
            cmd = f"mv {shlex.quote(source)} {shlex.quote(destination)}"
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

    def remove(self, path):
        cmd = f"rm -r {shlex.quote(path)}"
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

    def create_file(self, file_path, content=""):
        with open(file_path, 'w') as file:
            file.write(content)
        return f"File {file_path} created."


# Example usage:
commander = LinuxCommander()
print(commander.list_items())  # List items in the current directory
print(commander.move_or_copy("source.txt", "destination.txt"))  # Move a file
print(commander.remove("new_file.txt"))  # Remove a file
print(commander.create_file("new_file2.txt", "Hello, world!"))  # Create a file with content
