from controllers.main_window import ListBookWindow
from flask import Flask, request, jsonify,send_from_directory,render_template,redirect
import os
import threading
import logging

# Crear una instancia de ListBookWindow
list_book_window = ListBookWindow()

app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    return render_template('index.html')



#Métodos POST
#Método POST
@app.route('/consultaDNI-Tipo1', methods=['POST'])
def consultaDNI_Tipo1():
    data = request.get_json()
    n_dni = data.get('N_DNI')
    if n_dni:
        resultado = list_book_window.ConsultaDNI(n_dni)
        return jsonify(resultado)
    return jsonify({"error": "No se ha proporcionado DNI"}), 400




'''
@app.route('/consultaDNI-Tipo2', methods=['POST'])
def consultaDNI_Tipo2():
    data = request.get_json()
    dep = data.get('Departamento')
    prov = data.get('Provincia')
    distr = data.get('Distrito')
    sect = data.get('Sector')
    N_aleatorio = int(data.get('N_aleatorio'))
    #Comprobando si el shape de Sector estadistico tiene geometry
    file_shape=RutaShape(dep)
    shape_sector=gpd.read_file(file_shape[0])
    shape_sector=shape_sector[(shape_sector['NOMBDEP']==dep)&(shape_sector['NOMBPROV']==prov)&(shape_sector['NOMBDIST']==distr)]
    lista_sector=shape_sector["NOM_SE"].to_numpy().tolist()

    logging.info(f"Datos recibidos: dep={dep}, prov={prov}, distr={distr}, sect={sect}, N_aleatorio={N_aleatorio}")
    
    try:
        if str(lista_sector[-1]) == 'nan':
            html_filepath = ViewModel.ProcesarModel(dep, prov, distr, sect, N_aleatorio,"NULL")
        else:
            html_filepath = ViewModel.ProcesarModel(dep, prov, distr, sect, N_aleatorio,"NO NULL")

        logging.info(f"html_filepath generado: {html_filepath}")

        if html_filepath is None:
            raise ValueError("El procesamiento del modelo devolvió None")

        filename = os.path.basename(html_filepath)
        directory = os.path.dirname(html_filepath)
        response = send_from_directory(directory=directory, path=filename)
        threading.Thread(target=delete_file, args=(html_filepath,)).start()
        return response, 200
    except Exception as e:
        logging.error(f"Tipo de error: {type(e).__name__}")
        logging.error(f"Mensaje de error: {str(e)}")
        return jsonify({"error": f"Error al generar el mapa: {str(e)}"}), 500
    
'''

@app.route('/geopandasIcon.ico')
def favicon():
    return send_from_directory('static', 'geopandasIcon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

