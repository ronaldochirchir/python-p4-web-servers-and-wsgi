from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # Print client information to console
    print(f'This web server is running at {request.remote_addr}')
    print(f'Request method: {request.method}')
    print(f'Request path: {request.path}')
    
    # Create and return a response
    return Response(
        'A WSGI generated this response!\n'
        f'You accessed: {request.path}\n'
        f'Your IP: {request.remote_addr}',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )