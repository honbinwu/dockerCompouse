from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings
import base64

# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

# setup flask app
app = Flask(__name__)

# setup swagger online document
swagger = Swagger(app)

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# create user restful API
@app.route('/create_user', methods=['POST'])
@app.route('/',methods=['GET','POST'])
@swag_from('apidocs/api_create_user.yml')
def create_user():
    if request.method == 'POST':
        username=request.values['username']
        password=request.values['password']
        if (username=="")or(password==""):
           return "<h1>input error! please enter again</h1>"
        else:
            encry = base64.b64encode(password.encode('utf-8')).decode()


            logging.info('username:', username)
            logging.info('password:', encry)

            message = dict()
            message['username'] = username
            message['password'] = encry

    # push username and password
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
            channel = connection.channel()

            channel.queue_declare(queue='task_queue', durable=True)
    #message = ' '.join(sys.argv[1:]) or "NPTU Cloud Computing"

            message = json.dumps(message)
            logging.info('message:', message)

            channel.basic_publish(
                exchange='',
                routing_key='task_queue',
                body=message,
                properties=pika.BasicProperties(delivery_mode=2)
            )

            connection.close()

    # reture requests
    
            return render_template('createuser.html',mes='Create user successed,your username='+username)

    else:
        return render_template('createuser.html',mes="")


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
