from flask import Flask
from flask import jsonify
from flask import request
from manipulation import get_user, get_product, get_QS
import json
from handle import set_body, return_score
from flask_cors import CORS
from Common.ReadConfig import PARA

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 处理跨域问题

# 给接口返回赋值
user = get_user()
product = get_product()


@app.route('/zentao/userlist/', methods=['GET'])
def get_user():
	return jsonify(user)


@app.route('/zentao/productlist/', methods=['GET'])
def get_product():
	return jsonify(product)


@app.route('/zentao/score/', methods=['POST'])
def get_score():
	if request.method == 'POST':
		data = request.data  # 获取的是字符串
		j_data = json.loads(data)  # 转换成dict
		score = get_QS(j_data['begindate'], j_data['enddate'])
		if not data:  # data是否为空
			return jsonify("fail,please check your post body")
		else:
			condition = set_body(j_data['p_name'], j_data['name'])
			result = return_score(condition, score)
			return jsonify(result)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(PARA['port']), debug=False, threaded=True)
# app.run(debug=True, threaded=True)
