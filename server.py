from flask import Flask, request, render_template,redirect, url_for
import sqlite3
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/VP')
def VP():
    return render_template('VP.html')

@app.route('/VS')
def VS():
    return render_template('VS.html')

@app.route('/SP')
def SP():
    return render_template('SP.html')

@app.route('/About_us')
def About_us():
    return render_template('About_us.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        enf = request.form['enfermedad']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM velas where enfermedad = '{enf}'")
        message = c.fetchall()
        print(message)
        conn.close()
        return render_template('SP.html',message=message)


@app.route('/send_orden', methods=['POST','GET'])
def send_orden():
    print('no ha entrado al if')
    if request.method == 'POST':
        print('entro al if')
        intencion = request.form['intencion']
        print(intencion)
        color = request.form['color']
        aroma = request.form['aroma']
        mensaje = request.form['mensaje']
        fecha = '8/3/2025'
        cantidad = request.form['cantidad']
        nombre = request.form['nombre']
        email = request.form['email']

        conn = sqlite3.connect('database.db')
        table_name = "pedidos"
        c = conn.cursor()
        c.execute(f"SELECT id FROM pedidos order by id desc limit 1")
        query = c.fetchall()
        id_ = query[0][0]+1
        df = pd.DataFrame([[id_,intencion,color,aroma,mensaje,fecha,cantidad,nombre,email]],
                          columns = ["id","intencion","color","aroma","mensaje","fecha","cantidad","nombre","email"])
        print(df)
        df.to_sql(table_name, conn, if_exists='append', index=False)
        conn.close()
        message = "tu pedido se mando"

        return render_template('VP.html',message=message)
    
if __name__ == '__main__':
    app.run(debug=True)
