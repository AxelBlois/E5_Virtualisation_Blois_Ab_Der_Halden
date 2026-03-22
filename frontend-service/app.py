import requests
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet Virtualisation</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.1); text-align: center; max-width: 600px; width: 100%; }
        h1 { color: #2c3e50; margin-bottom: 20px; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        .status-card { background-color: #e8f4fd; border-left: 5px solid #3498db; padding: 20px; border-radius: 8px; margin-top: 20px; text-align: left; }
        .status-title { font-weight: bold; color: #2980b9; margin-bottom: 5px; text-transform: uppercase; font-size: 0.8em; }
        .status-message { color: #34495e; font-size: 1.1em; line-height: 1.5; word-wrap: break-word; }
        .badge { display: inline-block; padding: 5px 12px; border-radius: 20px; background-color: #27ae60; color: white; font-size: 0.9em; margin-bottom: 15px; }
        footer { margin-top: 30px; font-size: 0.8em; color: #bdc3c7; }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">System Online</div>
        <h1>Projet Virtualisation</h1>
        <div class="status-card">
            <div class="status-title">Backend & Database Connection Status</div>
            <div class="status-message">{{ backend_data }}</div>
        </div>
        <footer>ESIEE Paris - Distributed Systems Project</footer>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    try:
        response = requests.get("http://backend-service/api/hello")
        data = response.json()
        message = f"{data['message']} <br><br> <strong>Database Info:</strong> {data.get('database', 'No DB info found')}"
        if "(Connected to" in data['message']:
             message = data['message']
    except Exception as e:
        message = f"Connection error: {str(e)}"
    
    return render_template_string(HTML_TEMPLATE, backend_data=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)