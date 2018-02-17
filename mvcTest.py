from flask import Flask, request


@app.route("/test", methods=['GET'])
def callback():
    return 'OOL'
