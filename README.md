Basic Python Port Scanner
A lightweight command-line port scanner written in Python using standard socket networking. It checks ports up to a user-defined limit on a target IP address and logs all discovered open ports to a text file.

Features
Dynamic Port Range: Accepts user input to define the target IP address and maximum port number to scan.

TCP Socket Probing: Uses socket.AF_INET and socket.SOCK_STREAM for standard IPv4 TCP connection attempts.

Timeout Protection: Includes a 1-second socket timeout (settimeout(1)) to keep scanning from hanging on non-responsive ports.

Error Code Checking: Uses connect_ex() to safely receive status codes (0 for success) without throwing unhandled exceptions.

Persistent Log Creation: Appends each open port found directly into result.txt.

Automatic Summary: Reads and displays the complete contents of result.txt on the terminal once the scan completes.

File Structure
Plaintext
├── port_scanner.py     # Main Python port scanner script
├── result.txt          # Output file containing open ports (auto-generated)
└── README.md           # Project documentation
Output Schema
Active ports are appended line-by-line in result.txt:

Plaintext
Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
How to Run
Prerequisites
Python 3.x installed on your system.

Steps
Open your terminal or command prompt.

Execute the Python script:

Bash
python port_scanner.py
Enter the target IP address and the highest port number when prompted:

Plaintext
Enter target ip address : 127.0.0.1
Enter maximum port number to scan : 1000

Disclaimer
This utility is created strictly for educational purposes and authorized security testing. Scanning network hosts without explicit authorization from the owner is illegal.
