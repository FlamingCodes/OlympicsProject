from bottle import get, post, route, run, request, view, static_file, template
import bottle
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
@view('olympics_temp')

def welcome():
    con = "Hello " + request.forms.get("name") + " !"
    return { "content" : con, "get_url" : bottle.url}

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
    

run(host='localhost', port=8080, debug=True)
