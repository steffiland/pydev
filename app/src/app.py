# https://www.docker.com/blog/containerized-python-development-part-1/

# debugger
#import ptvsd
#ptvsd.enable_attach(address=('0.0.0.0', 5678))


from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World, edit and refresh rules!"

if __name__ == "__main__":
   server.run(host='0.0.0.0')
