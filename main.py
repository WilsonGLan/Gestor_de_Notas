from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    title='Inicio'
    route = '/ Inicio'
    return render_template('inicio.html', title=title, route=route)


@app.route('/courses')
def courses():
    title = 'Administrar asignaturas'
    route = '/ Administrar asignaturas'
    return render_template('adminCourses.html', title=title, route=route)
    #params = request.args.get('nombre_param', 'valor_por_defecto')   
    #return 'El parametro es {}'.format(params) 

@app.route('/registerActivities')
def registerActivities():
    title = 'Registrar actividades'
    route = '/ Registrar actividades'
    return render_template('registerActivities.html', title=title, route=route)


if __name__ == '__main__':    
    app.run(debug=True)