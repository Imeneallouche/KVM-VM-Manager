# KVM-VM-Manager

A Python-based interactive tool for managing virtual machines on KVM/QEMU using the `libvirt` API. This tool provides a simple command-line interface to perform essential VM operations such as listing, starting, and stopping virtual machines.

<br><br>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Commands Overview](#commands-overview)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

<br><br>

## Introduction

Managing virtual machines can often be complex, especially when dealing with multiple VMs on a KVM/QEMU environment. The **KVM-VM-Manager** simplifies this process by providing a user-friendly interface to perform common VM management tasks using the `libvirt` API.

<br><br>

## Features

- List all virtual machines, both running and defined (but not running)
- Start a specified virtual machine
- Stop a running virtual machine (with an option for a graceful shutdown)
- Display the name of the hypervisor
- Retrieving the IP address of a VM

<br><br>

## Prerequisites

Before running the tool, ensure you have the following installed on your system:

- **KVM/QEMU**: A complete virtualization solution for Linux.
- **libvirt**: A toolkit to manage virtualization platforms.
- **Python 3.x**: The programming language used for this project.
- **Virt-Manager** (optional): A GUI-based tool for managing VMs.

To install the required packages on a Debian-based system like Kali Linux, use:

```bash
sudo apt update
sudo apt install -y libvirt-daemon libvirt-clients libvirt-python virt-manager
```

<br><br>

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Imeneallouche/KVM-VM-Manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd KVM-VM-Manager
   ```
3. Install the required Python packages (if any).

<br><br>

## Usage

1. Start the `libvirtd` service:
   ```bash
   sudo systemctl start libvirtd
   sudo systemctl enable libvirtd
   ```
2. Run the Python script:
   ```bash
   python3 vm_manager.py
   ```
3. Follow the on-screen prompts to manage your virtual machines.

<br><br>

## Commands Overview

### Main Menu Options:

1. **0 - Hypervisor Name**: Displays the name of the hypervisor host.
2. **1 - List Virtual Machines**: Lists all defined and running VMs.
3. **2 - Start a Virtual Machine**: Allows you to start a specified VM.
4. **3 - Stop a Virtual Machine**: Stops a running VM (forcefully or gracefully).
5. **4 - Get VM IP Address**: retrives IP addresses of chosen VM (the VM chosen should be UP AND RUNNING).
6. **5 - Quit**: Exits the program.

<br><br>

## Future Enhancements

- Add support for more advanced VM management features, such as snapshots and resource allocation.
- Improve error handling and input validation for a more robust user experience.

<br><br>

## Contributing

Contributions are welcome! If you have ideas for improvements or find any bugs, please open an issue or submit a pull request. Make sure to follow the contribution guidelines.

<br><br>

Thank you for checking out the **KVM-VM-Manager** project! Happy virtual machine managing!
