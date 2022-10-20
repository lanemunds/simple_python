from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return"2nd letter: {}".format(name[1])    

@app.route('/puppylatin/<name>')
def puppylat(name):
    pupname = ''
    if name[-1] == "y":
        pupname = name[:-1] + "iful"
    else:
        pupname = name + 'y'
        
    return "<h1> Your puppy latin name is: {}".format(pupname)        
    


if __name__ == '__main__':
    app.run()