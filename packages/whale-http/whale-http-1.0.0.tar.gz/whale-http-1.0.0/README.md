## whale-http
    
Fork from [http-prompt](https://github.com/httpie/http-prompt) which is a interactive http cli tool.
    
Add project feature. Http requests are organized in project.
    
Project settings and history are stored in a project directory.


### installation

#### pypi:

    pip install whale-http

#### from source:
    
clone this repo first,
    
    git clone https://github.com/yuexl/whale-http.git

then install

    cd whale-http
    python setup.py install


### usage

Create project:

    whale-http new -n foo -u http://localhost:8000

The command above will create a project named foo, and auto active into interactive mode.

You can also start cli using command below, if have exited the cli mode.

    whale-http -p foo

Delete project:

    whale-http delete -n foo


Also can change project with 'cp ' command, when program is running. 

Since whale-http inherate from http-prompt, so all the [http-prompt](https://github.com/httpie/http-prompt) commands are available.