from bottle import get, post, route, run, request, view, static_file, template, response
import bottle
import sqlite3

#@route('/search_athlet')
#@view('olympics_searchathlet')
#def teilnahme_an():
#	olympic = sqlite3.connect('olympic.db')
#	content = select * from sportler a, wettkampf b where a.id = b.sportler_id;
#	return {"content" : content ,"get_url" : bottle.url}
olympic = sqlite3.connect('olympic.db')
SELECT T1.ID, T2.sportler_id
FROM sportler T1, wettkampf T2
WHERE T1.ID = T2.sportler_id
olympic.commit()
