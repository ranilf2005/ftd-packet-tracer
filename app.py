from flask import Flask, render_template, request, jsonify
from ftd_ssh import ssh_command, parse_interfaces

# Replace these with your FTD's info (or load securely from environment)
FTD_HOST = '192.168.30.30'
FTD_USER = 'admin'
FTD_PASS = 'C@L0dmz!123'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interfaces')
def interfaces():
    return jsonify(["GigabitEthernet0/0", "GigabitEthernet0/1"])

@app.route('/packet-tracer', methods=['POST'])
def packet_tracer():
    data = request.json
    cmd = (
        f"packet-tracer input {data['input_ifc']} {data['protocol']} "
        f"{data['src_ip']} {data['src_port']} {data['dst_ip']} {data['dst_port']} "
        f"detailed out {data['output_ifc']}"
    )
    output = ssh_command(FTD_HOST, FTD_USER, FTD_PASS, cmd)
    # Adjust result parsing based on FTD's actual packet-tracer output!
    result = 'PASS' if 'result: allow' in output.lower() else 'FAIL'
    return jsonify({'result': result, 'details': output})

if __name__ == '__main__':
    app.run(debug=True)
