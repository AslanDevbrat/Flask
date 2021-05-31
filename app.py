from flask import Flask, jsonify

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'item': [
            {
                'name': 'My Item',
                'price': '15.99'
            }
        ]

    }
]


# POST /store data: {name:}
@app.route('/store', methods=["POST"])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
