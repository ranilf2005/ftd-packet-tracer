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


