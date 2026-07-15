from flask import Flask, request, jsonify

app = Flask(__name__)

# 首页路由
@app.route('/')
def index():
    return "Flask服务运行正常！"

# GET问候接口
@app.route('/api/hello')
def hello():
    name = request.args.get("name", "访客")
    return jsonify({
        "code": 200,
        "message": f"你好{name}"
    })

# POST接收数据接口
@app.route('/api/data', methods=["POST"])
def data():
    return jsonify({"code": 200, "msg": "接收数据成功"})

# Render部署固定写法，不要改动
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)