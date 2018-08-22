from api import app

"""To prevent the app from running when the file or something in the file is imported
i.e if the file is run, the flask app will start, 
but if another file that imports app runs then it will not start
"""
if __name__ == '__main__':
    app.run(port=5000, debug=True)