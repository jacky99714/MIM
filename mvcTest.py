from flask import Flask, request


@app.route("/test", methods=['GET'])
def test():
    return 'OOL'
