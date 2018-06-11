import socket

_200_ok = """
HTTP/1.1 200 OK
content-type: text/html
wtf: Really, you want to read this?
conent-length: {}
"""

html_sample = """
<!DOCTYPE html>
<html>
<body>
Hello, world!
</body>
</html>


"""

def validate_data(data):
    method_check = 0
    data = data.split('\r\n')
    for line in data:
        print line
        if not method_check:
            method = line[:3]
            print method
            if method not in ['GET', 'POST']:
                print 'Method not supported'
                return False
            method_check = 1
        else:
            header_arr = [x.strip() for x in line.split(':')]
            print header_arr
            if header_arr[0].lower() == 'host':
                print 'Looking for host: ', header_arr[1]
                return True 
            
        

def handle_client(conn):
    data = conn.recv(1000)
    if validate_data(data):
        response = _200_ok.format(len(html_sample)) + html_sample
        print response
        conn.send(response)
    print data
#    conn.close()

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('127.0.0.1', 8080))

    s.listen(5)

    try:
        while(1):
            conn, client_addr = s.accept()
            print client_addr
            handle_client(conn)
    finally:
        s.close()

