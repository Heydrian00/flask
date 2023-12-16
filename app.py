from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Profile')
def Profile():
    return render_template('Profile.html', page_name = 'Profile')


@app.route('/Uppercase', methods=['GET', 'POST'])
def Uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Uppercase.html', result=result, page_name = 'Uppercase')

import math
def Circle_area(radius):
        
        if radius < 0:
            return 'Radius cannot be negative'
            
        area = math.pi*radius**2
        return area


@app.route('/Area_of_a_Circle', methods=['GET', 'POST'])
def Area_of_a_Circle():
    radius = 0
    area = 0
    if request.method == 'POST':
        radius = float(request.form['radius'])
        area = Circle_area(radius)
    return render_template('Area_of_a_Circle.html', radius=radius, area=area, page_name = 'Circle')

def Triangle_area(base, height):
    
    if base < 0 or height < 0:
        return 'Base and Height cannot be negative'

    area = (base * height) / 2
    return round(area, 2)

@app.route('/Area_of_a_Triangle', methods=['GET', 'POST'])
def Area_of_a_Triangle():
    base = 0
    height = 0
    area = 0

    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = Triangle_area(base, height)
        
    return render_template('Area_of_a_Triangle.html', base=base, height=height, area=area, page_name = 'Triangle')

if __name__ == "__main__":
    app.run(debug=True)
