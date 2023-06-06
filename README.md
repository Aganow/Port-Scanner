# Port Scanner

A simple port scanning tool for educational purposes.

## Overview

The Port Scanner is a Python script that allows you to scan a target host for open ports. It uses socket programming to establish connections to the specified ports and checks if they are open or closed.

Please note that this tool is meant for educational purposes only and should not be used for any malicious activities. Always ensure you have proper authorization before scanning any target host.

## Features

- Scans a target host for open ports
- Supports scanning multiple ports
- Prints the list of open ports

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `port_scanner.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `port_scanner.py` file.

3. Modify the `target_host` variable in the `main()` function to the IP address or domain name of the target host you want to scan.

4. Optionally, modify the `target_ports` variable in the `main()` function to specify the ports you want to scan. By default, the script scans ports 80, 443, 22, 21, and 3389.

5. Run the script by executing the following command:

   ```bash
   python port_scanner.py
   ```

6. The script will start scanning the specified target host and ports. Once the scan is complete, it will display the list of open ports found, if any.

## Disclaimer

This tool is provided for educational purposes only. The author and the contributors are not responsible for any misuse or illegal activities performed with this tool. Always ensure you have proper authorization before scanning any target host.

## License

This project is licensed under the [MIT License](LICENSE).
