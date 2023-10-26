import http.client
import http.server
import time

import requests

import json
def send_request_to_ai_server(request_body):
    ai_server_host = '117.17.191.49'  # AI 서버 호스트 주소
    ai_server_port = 12000  # AI 서버 포트

    ai_server_path = '10.50.99.242:12000'  # AI 서버의 엔드포인트 경로
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


def main():
    i=1
    while (i):
        request_data = requests.request(method="POST", url="117.17.191.49:12000")

        response_status, response_data = send_request_to_ai_server(request_data)

        print(f'Response Status: {response_status}')

        # AI 서버에서 받은 결과 데이터 (예: JSON 형식)
        result_data = json.dumps([('file', open('./media/summed.txt')), ('file', open('./media/background.png')),
                       ('file', open('./media/summed.txt'))])

        response_status, response_data = send_result_to_spring(result_data)

        print(f'Response Status: {response_status}')

        i=0
        time.sleep(1)


if __name__ == '__main__':
    main()
