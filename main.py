from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/sicarditv')
def proxy_stream():
    url = "https://vivo.solumedia.com:19360/sicarditv/sicarditv.m3u8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, stream=True)
        return Response(resp.iter_content(chunk_size=1024), content_type=resp.headers['Content-Type'])
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=8080)
