from functools import wraps
from flask import Flask, request, make_response, jsonify
from chatbot_graph import *

app = Flask(__name__)
query = ChatBotGraph()


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


@app.route('/')
def main_page():
    return '<h1>Main Page of KBQA-Medical</h1>'


# @app.route('/ask/')
# def ask_empty():
#     return 'Ready to answer...'


# @app.route('/ask/<string:message>')
# def ask(message):
#     sent = message
#     ans = query.chat_main(sent)
#     return ans

@app.route('/ask', methods=['GET'])
@allow_cross_domain
def ask():
    sent = request.values['msg']
    app.logger.info(sent)
    # app.logger.info(request.values['ischatbot'])
    ans = query.chat_main(str(sent))
    app.logger.info(ans)
    # return jsonify(ans)
    return ans


@app.route('/getToast', methods=['GET'])
@allow_cross_domain
def get_toast():
    sent = request.values['info']
    ans = query.chat_main(sent.encode('utf-8'))
    return jsonify(ans)


if __name__ == '__main__':
    app.run(debug=True)
