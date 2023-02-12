from futmx import create_app

app = create_app('development')

if '__main__' == __name__:
    app.run(debug=True)
