from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy-like')
def proxy_like():
    uid = request.args.get('uid')
    server = request.args.get('server_name', 'vn')

    url = f"https://sixuuii-k3ch.onrender.com/like?server_name={server}&uid={uid}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Origin": "https://yourdomain.com",  # sửa thành web bạn
        "Referer": "https://yourdomain.com/"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)

        return Response(
            res.content,
            status=res.status_code,
            content_type=res.headers.get('Content-Type', 'application/json')
        )
    except Exception as e:
        return {"error": str(e)}, 500


# 🔥 FIX CORS
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)