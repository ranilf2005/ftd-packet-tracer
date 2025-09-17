# ftd-packet-tracer

Objective:
Develop a web application that:

Uses Python to SSH into Cisco Secure Firewall FTD.
Retrieves and displays available interfaces via a web GUI.
Allows an engineer to run Packet Tracer (the FTD tool, not Cisco’s simulation software) on a selected interface via the GUI.
Displays pass/fail results on the web interface.

Solution Overview

Architecture Steps

SSH Connection Layer

Use a Python library (such as paramiko) to SSH into the FTD.
Run CLI commands to list available interfaces.
Run the Packet Tracer command as needed.
Web Server Layer

Use a lightweight Python web framework (such as Flask or FastAPI).
Provide endpoints:
To list interfaces.
To trigger Packet Tracer on a specific interface and present results.
Web GUI Layer

Use HTML/JavaScript (or a lightweight front-end framework) to display interface options and results.
Make AJAX calls to Flask endpoints.

Sample Directory Structure

<img width="461" height="199" alt="image" src="https://github.com/user-attachments/assets/d113eaef-17c6-462a-8b85-52d5f81345f8" />


Parameters to Collect from User

Input Interface (e.g., GigabitEthernet0/1)
Output Interface (e.g., GigabitEthernet0/2)
Source IP Address (e.g., 192.168.1.10)
Source Port (e.g., 12345)
Destination IP Address (e.g., 8.8.8.8)
Destination Port (e.g., 80)
Protocol (e.g., tcp, udp)

Updated User Flow

User opens web GUI.
Page loads and fetches available input/output interfaces from FTD.
User selects input interface, output interface, protocol, and fills in source/destination IP and port.
User clicks "Run Packet Tracer."
Backend SSHes to FTD, runs the packet-tracer command with parameters, returns pass/fail and details.
Result is displayed on the GUI.


How to Deploy and Run

Step 1: Clone/Create the project structure

Copy the above files and folders as shown.


Step 2: Install dependencies

<img width="262" height="86" alt="image" src="https://github.com/user-attachments/assets/7f98fad9-dd5a-470b-b58c-6ca5a3c4a003" />


Step 3: Edit credentials

Edit app.py and set FTD_HOST, FTD_USER, FTD_PASS at the top with your device info.


TIP: For security, consider using environment variables for these values in production.


Step 4: Run the Flask server

<img width="149" height="57" alt="image" src="https://github.com/user-attachments/assets/e56c596d-1552-40be-ac47-8331f985e3b2" />

The server will start on http://127.0.0.1:5000.


Step 5: Access the Web GUI

Open your browser and visit http://127.0.0.1:5000.


<img width="892" height="199" alt="image" src="https://github.com/user-attachments/assets/2efc0976-ddb9-47f2-995b-d03514b01d6e" />


<img width="408" height="291" alt="image" src="https://github.com/user-attachments/assets/5a8594ad-0865-45b2-8d8f-25cfd9c3da5d" />


