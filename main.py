from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')
@app.route('/junior')
def showJunior():
    return render_template('junior.html',relation='pet',age='8',name='Junior!')
@app.route('/dad')
def showdad():
    return render_template('dad.html',relation='father',age='51',name='Naveen')
@app.route('/mom')
def showmom():
    return render_template('mom.html',relation='mother',age='51',name='Madhavi')
@app.route('/brother')
def showbro():
    return render_template('brother.html',relation='brother',age='22',name='Arnav')
@app.route('/me')
def showme():
    return render_template('arjun.html',age='15',name='Arjun')
app.run(debug = True)