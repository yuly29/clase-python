from flask import Flask, render_template, request, jsonify
import pandas as pd 
import os
import openpyxl
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

ARCHIVO = "usuarios.xlsx"



@app.route("/procesar", methods=["POST"])
def procesar():
    data = request.get_json()
    nombre = data["nombre"]
    email = data["email"]
    edad = data["edad"]
    
    
    if not os.path.exists(ARCHIVO):
        df = pd.DataFrame(columns=["Nombre", "Email", "edad"])
        
        df.to_excel(ARCHIVO, index=False)
    
    df = pd.read_excel (ARCHIVO)
    df.loc[len(df)] = [nombre, email, edad]
    
    df.to_excel(ARCHIVO, index=False)
    print(df)
    
    #Calculos con numpy
    edades = df["edad"].to_numpy()
    promedio = np.mean(edades)
    
    #crear grafico con matplotlib
    plt.figure()
    plt.plot(edades, marker="o")
    plt.title("Edades ingresadas")
    plt.xlabel("Ingreso N°")
    plt.ylabel("edad")
    plt.grid(True)
    plt.show()
    plt.savefig("static/grafica.png")
    plt.close()
        
        
                              
    mensaje = f"Hola, {nombre}. ¡Tu información ha sido procesada con Python!, El promedio de las edades es {promedio}"
    return jsonify({"mensaje": mensaje})

   
    

if __name__ == "__main__":
    app.run(debug=True)
