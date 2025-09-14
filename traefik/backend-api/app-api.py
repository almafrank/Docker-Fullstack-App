from flask import Flask , request, jsonify
from redis import Redis
import os


app=Flask(__name__)
redis_host = os.getenv("DB_REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_POST", 6379)) #web post
redis=Redis(host=redis_host, port=redis_port,decode_responses=True)

# homepage 
@app.route('/')
def home():
    return "Message Link Site!!"



@app.route('/visits', methods=['GET'])
def get_all_visits():
    visit_count = redis.incr('visits')
    return jsonify({"visits": visit_count})



#post message 
@app.route('/postmessage', methods=['POST'])
def post_message():
    data = request.get_json()
    if not data or 'msg' not in data:
        return jsonify({"error": "Missing 'msg' in request body"}), 400
    redis.set('message', data['msg'])
    return jsonify({"message": data['msg']}), 201

#get message
@app.route('/getmessage', methods=['GET'])
def get_message():
    message = redis.get('message')
    if not message:
        return jsonify({"message": None})
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)