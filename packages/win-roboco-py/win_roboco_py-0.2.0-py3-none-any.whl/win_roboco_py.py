from pathlib import Path
from typing import List
import subprocess
import sys

def _run_robocopy(command: List[str], num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_file: bool = False) -> int:
    command.insert(0, 'robocopy')

    # Retries and wait period
    command.append(f"/r:{num_retries}")
    command.append("/w:1")

    if verbose:
        command.append("/v")
        command.append("/x")
    if dry_run:
        command.append("/l")
    if large_file:
        command.append("/j")
        command.append("/mt:8")

    print(" ".join(command))

    with subprocess.Popen(command, text=True, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE) as process:
        for out in process.stdout:
            print(out)

        process.wait()
        if process.returncode >= 8:
            print(f"robocopy returned error code: {process.returncode}", file=sys.stderr)
        return process.returncode


#
def copy_file(source_file: Path, destination_dir: Path, num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_file: bool = False) -> bool:
    cmd = []
    cmd.append(str(source_file.parents[0]))
    cmd.append(str(destination_dir))
    cmd.append(str(source_file.name))

    result = _run_robocopy(cmd, num_retries, verbose, dry_run, large_file)
    return result < 8

#
def move_file(source_file: Path, destination_dir: Path, num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_file: bool = False):
    cmd = []
    cmd.append(str(source_file.parents[0]))
    cmd.append(str(destination_dir))
    cmd.append(str(source_file.name))
    cmd.append("/mov")

    result = _run_robocopy(cmd, num_retries, verbose, dry_run, large_file)
    return result < 8

#
def copy_directory(source_dir: Path, destination_dir: Path, num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_files: bool = False) -> bool:
    cmd = []
    cmd.append(str(source_dir))
    cmd.append(str(destination_dir))

    result = _run_robocopy(cmd, num_retries, verbose, dry_run, large_files)
    return result < 8

#
def move_directory(source_dir: Path, destination_dir: Path, num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_files: bool = False) -> bool:
    cmd = []
    cmd.append(str(source_dir))
    cmd.append(str(destination_dir))
    cmd.append("/move")

    result = _run_robocopy(cmd, num_retries, verbose, dry_run, large_files)
    return result < 8

#
def mirror_directory(source_dir: Path, destination_dir: Path, num_retries: int = 10, verbose: bool = False, dry_run: bool = False, large_files: bool = False) -> bool:
    cmd = []
    cmd.append(str(source_dir))
    cmd.append(str(destination_dir))
    cmd.append("/mir")

    result = _run_robocopy(cmd, num_retries, verbose, dry_run, large_files)
    return result < 8
