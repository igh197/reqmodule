import http.client

import requests


def send_request_to_ai_server(request_body):
    ai_server_host = '10.50.99.242'  # AI 서버 호스트 주소
    ai_server_port = 8081  # AI 서버 포트

    ai_server_path = '10.50.99.242:8081/'  # AI 서버의 엔드포인트 경로
    headers = {'Content-Type': 'application/json'}  # 요청 헤더 설정 (JSON 예제)

    try:
        connection = http.client.HTTPConnection(ai_server_host, ai_server_port)
        connection.request('POST', ai_server_path, body=request_body, headers=headers)

        response = connection.getresponse()
        response_data = response.read()

        return response.status, response_data

    except Exception as e:
        return 500, str(e)  # 에러 처리 (500 Internal Server Error)


def send_result_to_spring(result_data):
    spring_server_host = '127.0.0.1'  # Spring 서버 호스트 주소
    spring_server_port = 8080  # Spring 서버 포트

    spring_server_path = '/api/file/share'  # Spring 서버의 엔드포인트 경로
    headers = {'Content-Type': 'application/json'}  # 요청 헤더 설정 (JSON 예제)

    try:
        connection = http.client.HTTPConnection(spring_server_host, spring_server_port)
        connection.request('POST', spring_server_path, body=result_data, headers=headers)

        response = connection.getresponse()
        response_data = response.read()

        return response.status, response_data

    except Exception as e:
        return 500, str(e)
