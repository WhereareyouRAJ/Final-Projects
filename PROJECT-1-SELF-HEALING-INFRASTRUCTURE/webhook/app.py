from flask import Flask, request
import subprocess

app = Flask(__name__)  

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Alert received:", data)
    print("Webhook triggered!")
    
    try:
        # Use direct docker command 
        result = subprocess.run(["docker", "restart", "nginx"], 
                               capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return f"Alert received but error occurred: {result.stderr}", 500
        print("Nginx container restarted successfully")
        return "Alert received and nginx restarted", 200
    except Exception as e:
        print(f"Error restarting container: {e}")
        return f"Alert received but error occurred: {e}", 500

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5001, debug=True)
