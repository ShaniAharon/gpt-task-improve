from flask_app import create_app

app = create_app()

if __name__ == '__main__':# it will run the file only if we run it directly
    app.run(debug=True)#rerun the code after changes remove it in prod