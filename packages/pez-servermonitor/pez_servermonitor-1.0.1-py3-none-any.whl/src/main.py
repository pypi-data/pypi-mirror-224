import argparse
import os
import platform
import time

from src.containers import print_running_containers
from src.cpu import print_cpu_info
from src.disks import print_disk_info
from src.latency import print_latency_info
from src.memory import print_memory_info
from src.networking import print_network_info
from src.processes import print_cpu_usage_info, print_memory_usage_info
from src.services import print_process_info
from src.system import print_system_info
from src.utils import print_title_red


def check_os() -> None:
    """Checks if the OS is supported."""
    current_os = platform.system()
    if current_os in ("Windows", "Darwin"):
        print_title_red(
            f"{current_os} OS is not fully supported yet. Results may vary."
        )
        time.sleep(2)


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="System information tool.")
    parser.add_argument("-a", "--all", action="store_true", help="Show all information")
    parser.add_argument(
        "-s", "--system", action="store_true", help="Show only system information"
    )
    parser.add_argument(
        "-c", "--cpu", action="store_true", help="Show only CPU information"
    )
    parser.add_argument(
        "-m", "--memory", action="store_true", help="Show only memory information"
    )
    parser.add_argument(
        "-d", "--disk", action="store_true", help="Show only disk information"
    )
    parser.add_argument(
        "-n",
        "--network",
        action="store_true",
        help="Show only network and latency information",
    )
    parser.add_argument(
        "-ps", "--processes", action="store_true", help="Show only services information"
    )
    parser.add_argument(
        "-ct",
        "--containers",
        action="store_true",
        help="Show only running container (docker or podman) information",
    )
    parser.add_argument(
        "-cf",
        "--config",
        default=os.path.join(os.getenv("HOME", ""), ".config", "pez-sm", "config.yaml"),
        help="The path to the config file (default: ~/.config/pez-sm/config.yaml))",
    )

    return parser.parse_args()


def main() -> None:
    """Main function."""
    check_os()
    args = parse_args()
    try:
        config_file = args.config
        if args.all:
            print_all_info(config_file)
        elif args.system:
            print_system_info()
        elif args.cpu:
            print_cpu_info()
            print_cpu_usage_info()
        elif args.memory:
            print_memory_info()
            print_memory_usage_info()
        elif args.disk:
            print_disk_info()
        elif args.network:
            print_network_info()
            print_latency_info(config_file)
        elif args.processes:
            print_process_info(config_file)
        elif args.containers:
            print_running_containers()
        else:
            print("No arguments given. Use -h or --help for help.")
    except Exception as exception:
        print(f"An error occurred: {exception}")


def print_all_info(config_file: str) -> None:
    """
    Prints all system-related information.

    Args:
        config_file (str): The path to the config file.
    """
    print_system_info()
    print_cpu_info()
    print_cpu_usage_info()
    print_memory_info()
    print_memory_usage_info()
    print_disk_info()
    print_network_info()
    print_latency_info(config_file)
    print_process_info(config_file)
    print_running_containers()


if __name__ == "__main__":
    main()
