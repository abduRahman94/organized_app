from routes import urls
from factory import create_app


app = create_app('config')
app.register_blueprint(urls)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)





