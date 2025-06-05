"""

You should use the following function for this exercise:

def subprocess_runner(cmd_list, cmd_dir=None):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cmd_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)

Using the same "ping -c 3 127.0.0.1" command, call the subprocess_runner function. Your
function call will look as follows:

cmd_list = ["ping", "-c", "3", "127.0.0.1"]
std_out, std_err, returncode = subprocess_runner(cmd_list)

At the end of this function call, the std_out variable should have captured the output of
the ping command execution. This output should contain a line similar to the following:

3 packets transmitted, 3 received, 0% packet loss, time 2048ms

Find this line in the output and extract the percent packet loss. Print only this
percent packet loss to standard output.

Your output should look similar to the following:

$ python exercise5.py 

Percent Packet Loss:  0% packet loss

"""
import subprocess
from rich import print


def subprocess_runner(cmd_list, cmd_dir=None):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cmd_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


if __name__ == "__main__":

    ping_cmd = "ping -c 3 127.0.0.1"
    cmd_list = ping_cmd.split()
    std_out, std_err, returncode = subprocess_runner(cmd_list)

    print()
    for line in std_out.splitlines():
        if "packets transmitted" in line:
            fields = line.split(",")
            packet_loss = fields[2]
            print(f"Percent Packet Loss: {packet_loss}")
    print()
