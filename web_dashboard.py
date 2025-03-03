from flask import Flask, render_template, jsonify
import network_monitor
print(dir(network_monitor))
from network_monitor import get_active_networks
from alert_system import get_alerts

app = Flask(__name__)

alerts = []

@app.route("/")
def dashboard():
    networks = get_active_networks()
    return render_template("index.html", networks=networks)

@app.route('/alerts')
def alerts():
    alerts = get_alerts()
    return render_template('alerts.html', alerts=alerts)


@app.route('/networks')
def networks():
    return jsonify(get_active_networks())

@app.route("/add_alert/<msg>")
def add_alert(msg):
    alerts.append(msg)
    return "Alert added"

if __name__ == "__main__":
    app.run(debug=True, host="192.168.176.92", port=5000)
