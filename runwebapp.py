from bottle import get, post, route, run, request
@route('/')
@route('/hello')
def hello():
    return '''
        <form action="/welcome" method="post">
            <input type="text" value="name" name="name"/>
            <input type="text" value="age" name="age"/>
            <input type="submit" value="submit"/> 
        </form>'''

@route('/welcome', method='POST')
def welcome():
    return "Hello " + request.forms.get('name') + ", you are " + request.forms.get('age') + " old!"

run(host='localhost', port=8080, debug=True)
