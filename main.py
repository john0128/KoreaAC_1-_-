import platform, psutil
from flask import Flask

def start() :
    global command
    command = input('NjPy>')
    if (command == 'asdf') :
        print('Assualt')
        
    if (command == 'cpuinfo') :
        print('Process information  :\t', platform.processor())
        print('Process Architecture :\t', platform.machine())
        
    if (command == 'raminfo') :
        print('RAM Size             :\t',str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)")
    
    if (command == 'dev_webserver') :
        app = Flask(__name__)
        @app.route("/")
        def MainPage() :
            return "<iframe src=''></iframe>"
        app.run(host="127.0.0.1", port=9898)

    if (command == 'copyright') :
        print("이 프로그램의 저작권은 나인주안(1조 길음중 이주안)에게 있습니다")

    if (command == 'exit') :
        return 1



start()
