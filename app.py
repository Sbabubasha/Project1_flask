from flask import Flask


FAI=Flask(__name__)


@FAI.route('/basha')
def Basha():
    return 'this is the first project in flask'

@FAI.route('/Redmi')
def Redmi():
    return 'this is the redmi laptop'

if __name__=='__main__':
    FAI.run(debug=True)
    FAI.run(debug=True)

