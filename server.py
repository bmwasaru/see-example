from flask import Flask, Response, render_template
import time

app = Flask(__name__)

# Route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Function to stream server-sent events
def event_stream():
    while True:
        # Generate a new event every 5 seconds
        time.sleep(5)
        yield f"data: Notification at {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

# Route for the server-sent events
@app.route('/notifications')
def notifications():
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
