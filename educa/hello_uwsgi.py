def application (env, start_reponse) :
    start_reponse('200 OK',[
        ('content-Type', 'text/html')
    ])
    return [b"<h3>Hello uWSGI !</h3>"]