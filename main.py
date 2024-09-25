from controllers.main_window import ListBookWindow
from flask import Flask, request, jsonify,send_from_directory,render_template,redirect
from werkzeug.utils import secure_filename
import pandas as pd

# Crear una instancia de ListBookWindow
list_book_window = ListBookWindow()

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

#Métodos POST

@app.route('/consultaxDNINombresApellidos', methods=['POST'])
def consultaxDNINombresApellidos():
    try:
        data = request.get_json()
        Typeconsulta = str(data.get('Typeconsulta', ''))#Si es 0 busca por DNI y si es 1 busca por nomb y apellidos
        n_dni = data.get('N_DNI', '')
        Nom = data.get('Nombres', '').upper()  # Convertir a mayúsculas
        Ap_Pat = data.get('Ap_Paterno', '').upper()  # Convertir a mayúsculas
        Ap_Mat = data.get('Ap_Materno', '').upper()  # Convertir a mayúsculas

        if Typeconsulta!='0' and Typeconsulta!='1':
            return jsonify({"error":f"Typeconsulta debe ser solo 0 o 1: {Typeconsulta}"})
        
        if Typeconsulta=='0':
            # Validación del DNI
            if not n_dni or len(n_dni) != 8 or not n_dni.isdigit():
                    return jsonify({"error": "DNI inválido. Debe ser un número de 8 dígitos"}), 400
        elif Typeconsulta=='1':
            # Validación de campos:
            # Caso 1: Todos los campos deben ser diferentes de vacío
            # Caso 2: Nom puede estar vacío, pero Ap_Pat y Ap_Mat deben ser diferentes de vacío
            if (not Nom and (not Ap_Pat or not Ap_Mat)) or (not Ap_Pat or not Ap_Mat):
                return jsonify({"error": "Debe ingresar Ap_Paterno y Ap_Materno, y opcionalmente Nombres"}), 400
        
        # Consultar nombres y apellidos
        resultado = list_book_window.ConsultaxDNINombresApellidos(Typeconsulta,n_dni,Nom, Ap_Pat, Ap_Mat)
       
        # Verificar si el resultado es válido
        if resultado:
            return jsonify(resultado), 200
        else:
            return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
    except Exception as e:
        return jsonify({"error": f"Ha ocurrido un error: {str(e)}"}), 500



@app.route('/cargamasivaDNI', methods=['POST'])
def cargamasivaDNI():

    if 'archivo_excel' not in request.files:
        return jsonify({"error": "No se ha subido ningún archivo"}), 400

    archivo = request.files['archivo_excel']

    if archivo.filename == '':
        return jsonify({"error": "El archivo no tiene nombre"}), 400

    # Verifica si es un archivo válido de Excel
    if archivo and (archivo.filename.endswith('.xlsx') or archivo.filename.endswith('.xls')):
        filename = secure_filename(archivo.filename)

        try:
            # Leer el archivo Excel directamente en un DataFrame
            df = pd.read_excel(archivo,dtype={'DNI': str})

            # Supongamos que la función `seleccionar_archivo_xlsx` hace algún tipo de procesamiento
            resultado = list_book_window.seleccionar_archivo_xlsx(df)
            # Realiza operaciones con list_book_window...
            #list_book_window.stop_spark()
            
            # Verificar si el resultado es válido
            if resultado:
                return jsonify(resultado), 200
            else:
                return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Formato de archivo no soportado"}), 400


@app.route('/cargamasivaplatillaDNI', methods=['POST'])
def cargamasivaplantillaDNI():

    if 'archivoplantilla_excel' not in request.files:
        return jsonify({"error": "No se ha subido ningún archivo"}), 400

    archivo = request.files['archivoplantilla_excel']

    if archivo.filename == '':
        return jsonify({"error": "El archivo no tiene nombre"}), 400

    # Verifica si es un archivo válido de Excel
    if archivo and (archivo.filename.endswith('.xlsx') or archivo.filename.endswith('.xls')):
        filename = secure_filename(archivo.filename)

        try:
            # Leer el archivo Excel directamente en un DataFrame
            df = pd.read_excel(archivo,dtype={'DNI': str})

            # Supongamos que la función `seleccionar_archivo_xlsx` hace algún tipo de procesamiento
            plantilla= list_book_window.seleccionar_archivo_Plantilla_xlsx(df)
            # Realiza operaciones con list_book_window...
            #list_book_window.stop_spark()
            
            # Verificar si el resultado es válido
            if plantilla:
                return jsonify(plantilla), 200
            else:
                return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Formato de archivo no soportado"}), 400
    

@app.route('/Sispad.ico')
def favicon():
    return send_from_directory('static', 'Sispad.ico', as_attachment=False)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception as e:
        print(f"Error occurred: {e}")


