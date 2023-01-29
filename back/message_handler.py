from flask import Flask, request, jsonify


# app = None
messageCallback = None

class MessageHandler:

    def __init__(self, callback,app,cross_origin):
        # app = Flask(__name__)
        messageCallback = callback

        @app.route('/add')
        def add():         
            print(request.args)
            data = request.args
            action = 'create'
            return messageCallback(action, data)

        @app.route('/update')           
        def loan_book():         
            print(request.args)
            data = request.args
            action = 'create'
            return messageCallback(action, data)

        @app.route('/getAll')       
        def getAll():         
            print(request.args)
            data = request.args
            action = 'getAll'
            return messageCallback(action, data)

        @app.route('/delete')           
        def delete():         
            print(request.args)
            data = request.args
            action = 'delete'
            return messageCallback(action, data)

        if __name__ == '__main__':
            # run app in debug mode on port 5000
            app.run(debug=True, port=5000)