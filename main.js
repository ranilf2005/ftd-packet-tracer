window.onload = function() {
    fetch('/interfaces')
        .then(response => response.json())
        .then(interfaces => {
            let inputSel = document.getElementById('input_ifc');
            let outputSel = document.getElementById('output_ifc');
            interfaces.forEach(function(iface) {
                let opt1 = document.createElement('option');
                opt1.value = iface;
                opt1.text = iface;
                inputSel.appendChild(opt1);

                let opt2 = document.createElement('option');
                opt2.value = iface;
                opt2.text = iface;
                outputSel.appendChild(opt2);
            });
        });
    
    document.getElementById('packetTracerForm').onsubmit = async function(e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const payload = Object.fromEntries(formData.entries());
        const response = await fetch('/packet-tracer', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        const result = await response.json();
        document.getElementById('result').textContent = `Result: ${result.result}\nDetails:\n${result.details}`;
    };
};
