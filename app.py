from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Intermediate Lab</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f6f8;
                margin-top: 100px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to my Cloud Run Intermediate Lab</h1>
            <p>You can now learn more about me in the following sections, I love coding and building cloud applications but I also enjoy playing music.</p>

            <button onclick="location.href='/about_me'" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                About Me
            </button>
        </div>
    </body>
    </html>
    """

@app.route('/about_me')
def about_me():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Me</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f6f8;
                margin-top: 100px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👤 About Me</h1>
            <p>I am a developer working on cloud applications.</p>

            <button onclick="location.href='/'" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                Home
            </button>

            <button onclick="location.href='/music'" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                Music
            </button>

            <h1>Would you like to get data about the highest score Hacker News Posts using BigQuery?</h1>
            <button onclick="location.href='/query'" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                Get Data
            </button>
        </div>
    </body>
    </html>
    """

@app.route('/music')
def music():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Music</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f6f8;
                margin-top: 100px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎷 VISIT MY YOUTUBE CHANNEL!</h1>
            <p>Join me on my musical journey!</p>

            <button onclick="window.open('https://www.youtube.com/@jaansaax', '_blank')" 
                    style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                Visit YouTube Channel
            </button>

            <button onclick="location.href='/'" 
                    style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                Home
            </button>
        </div>
    </body>
    </html>
    """

@app.route('/query')
def query_bigquery():
    client = bigquery.Client()

    query = """
SELECT title, score
FROM `bigquery-public-data.hacker_news.full`
WHERE score IS NOT NULL
ORDER BY score DESC
LIMIT 10
"""

    query_job = client.query(query)
    results = query_job.result()

    titles = [row.title for row in results]
    return f'Top titles in Hacker News: {", ".join(titles)}'


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)