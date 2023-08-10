<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>PEZ-ServerMonitor
</h1>
<h3>◦ Monitor with ease, PEZ-Server does it all!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/timmyb824/PEZ-ServerMonitor.git?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/timmyb824/PEZ-ServerMonitor.git?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/timmyb824/PEZ-ServerMonitor.git?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/timmyb824/PEZ-ServerMonitor.git?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The PEZ Server Monitor is a system information tool that allows users to retrieve various types of information about their system. It offers functionalities to gather CPU details, memory information, disk space usage, network activity, process status, container information, and system statistics such as OS type, uptime, and hostname. The tool provides a robust and succinct overview of the system's performance, enabling users to monitor and troubleshoot any potential issues efficiently.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture where different components are organized into separate files. Each file focuses on a specific aspect of system monitoring, such as disk info, network info, process info, etc. The main.py file acts as the entry point and orchestrates the retrieval and display of different types of information based on user input. The use of modules allows for easy maintainability and extensibility of the system. |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. While each file has brief comments explaining their purpose, there is no centralized documentation that provides an overview of the system, its components, and how to use it. This makes it challenging for new developers to understand and contribute to the project. |
| **🔗 Dependencies**    | The codebase relies on several external libraries, including `psutil`, `tabulate`, `yaml`, and `subprocess`. These libraries are used for various tasks such as retrieving system information, formatting data, parsing configuration files, and executing shell commands. The use of these libraries enhances the functionality of the system and makes it easier to work with system-level data. |
| **🧩 Modularity**      | The codebase demonstrates good modularity by separating different functionalities into separate files. Each file focuses on a specific aspect of system monitoring and can be easily swapped or extended without affecting other parts of the system. This modularity allows for easier maintenance, testing, and customization of the monitoring tool. However, there could be further improvements by organizing related files into directories or modules to provide better organization and reduce potential naming conflicts. |
| **✔️ Testing**          | The codebase does not include any tests. Lack of tests makes it difficult to ensure the correctness and stability of the functionality provided by the system. Implementing a testing strategy, such as unit tests or integration tests, would greatly improve the reliability and maintainability of the codebase. |
| **⚡️ Performance**      | The codebase utilizes efficient libraries like `psutil` and `subprocess` to gather system information, reducing the impact on performance. However, without any benchmarking or profiling data, it is challenging to assess the overall performance of the system. Regular monitoring and optimization of resource usage, such as reducing unnecessary system calls or optimizing data retrieval, can further enhance the performance of the tool. |
| **🔐 Security**        | The codebase does not address security directly, as it primarily focuses on system monitoring. However, it is worth noting that the codebase relies on external libraries and system commands. Proper validation and sanitization of inputs, as well as implementing secure communication channels when interacting with external systems, should be considered to ensure the security of the monitoring tool and the systems it interacts with. |
| **🔀 Version Control** | The codebase is stored on

---


## 📂 Project Structure


```bash
repo
├── README.md
├── config.yaml
├── poetry.lock
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── config_parser.py
│   ├── constants.py
│   ├── container_info.py
│   ├── cpu_info.py
│   ├── disk_info.py
│   ├── latency_info.py
│   ├── main.py
│   ├── mem_info.py
│   ├── network_info.py
│   ├── process_info.py
│   ├── system_info.py
│   └── utils.py
└── tests
    └── __init__.py

3 directories, 18 files
```

---

## 🧩 Modules

<details closed><summary>Src</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [disk_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/disk_info.py)           | The code snippet retrieves disk space information using the psutil library and presents it in a tabular format using the tabulate library. It filters out certain mountpoints and calculates disk space in GB. The result is printed with headers.                                                                                                                                                                                                                    |
| [config_parser.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/config_parser.py)   | This code snippet imports the `yaml` module and a constant `ROOT_DIR` from another file. It defines a function `parse_config_file()` that takes a file path as a parameter and returns the content of the specified YAML configuration file as a Python dictionary.                                                                                                                                                                                                   |
| [constants.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/constants.py)           | The code snippet imports the'os' module and defines a constant variable'GET_WAN_IP' which stores a URL. It also sets the'ROOT_DIR' variable to the current directory path. The commented out lines suggest potential usage for ping hosts, service names, service hosts, enabling temporary storage, and disk preferences.                                                                                                                                            |
| [latency_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/latency_info.py)     | This code snippet imports necessary modules and defines functions to check the latency of hosts, calculate average latency, and print latency information. It uses multithreading to ping multiple hosts concurrently and displays the average round-trip delay along with per-host delay information.                                                                                                                                                                |
| [system_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/system_info.py)       | The code snippet provides functions to obtain and print system information, including OS type, distribution, kernel, uptime, last boot, hostname, architecture, number of users, and current datetime.                                                                                                                                                                                                                                                                |
| [process_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/process_info.py)     | The code snippet checks the status of various services by establishing a socket connection to each service's port and host. It then prints a table displaying the service name, port, and status (Up or Down). Additionally, it fetches the count of running processes and prints it.                                                                                                                                                                                 |
| [utils.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/utils.py)                   | The code snippet provides three functions:-"print_title" prints a title in green, with a bold and uppercase formatting. It takes a string argument "title".-"bold" returns a string with ANSI escape codes for bold formatting. It takes a string argument "text".-"print_bold_kv" prints a key-value pair with the label in bold and the value. It takes label and value strings as arguments.                                                                       |
| [container_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/container_info.py) | This code snippet checks if Docker or Podman is installed on the system, retrieves information about running containers, and prints the information in a tabular format. It utilizes subprocess, regular expressions, and the tabulate library.                                                                                                                                                                                                                       |
| [mem_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/mem_info.py)             | The code snippet retrieves memory information from the system and displays it using tabulate. It calculates and prints the total memory, free memory, memory usage percentage, swap total, swap free, and swap usage percentage.                                                                                                                                                                                                                                      |
| [network_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/network_info.py)     | The code snippet retrieves network information such as LAN and WAN IP addresses, network activity (bytes sent and received), and prints the information in a formatted table.                                                                                                                                                                                                                                                                                         |
| [main.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/main.py)                     | The code snippet is a system information tool that allows the user to retrieve different types of information about their system. It uses command-line arguments to specify which type of information to display, such as CPU, memory, disk, network, processes, and containers. The tool provides options to show all information or specific types of information. It achieves this by calling specific functions from different modules based on the user's input. |
| [cpu_info.py](https://github.com/timmyb824/PEZ-ServerMonitor.git/blob/main/src/cpu_info.py)             | The code snippet retrieves and prints various system information including CPU details, CPU usage, system temperature, process count, and load average. It uses the `psutil` and `os` modules to gather the data from the system.                                                                                                                                                                                                                                     |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the PEZ-ServerMonitor repository:
```sh
git clone https://github.com/timmyb824/PEZ-ServerMonitor.git
```

2. Change to the project directory:
```sh
cd PEZ-ServerMonitor
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using PEZ-ServerMonitor

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
