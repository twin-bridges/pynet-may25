import subprocess
from pathlib import Path


def subprocess_runner(cmd_list, cmd_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cmd_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


if __name__ == "__main__":

    cmd_list = ["/usr/bin/find", ".", "-name", "*.py"]
    cmd_dir = Path(".").resolve()
    cmd_dir = cmd_dir.parent.parent

    # import ipdb; ipdb.set_trace()

    std_out, std_err, ret_code = subprocess_runner(cmd_list, cmd_dir)

    for line in std_out.splitlines():
        if 'lesson2' in line:
            print(line)
