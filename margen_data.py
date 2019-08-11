import pandas as pd
import numpy as np 
import sys
import os  


margen_trimestral = pd.DataFrame()

def main(argv):
    walk_folder(argv)
    margen_trimestral.rename(columns={0: 'Anio', 1: 'Quarter', 2:'Ingresos',3: 'Resultado', 4:'ROE'},inplace=True)
    #margen_trimestral.groupby('Quarter')
    margen_trimestral.sort_values(['Quarter'])
    writer = pd.ExcelWriter("C:\\Users\\devel\\Downloads\\SQM\\Financieros\\Margen\\margen_trimestral.xlsx", engine='xlsxwriter')
    margen_trimestral.to_excel(writer,sheet_name="Margen")
    writer.save()
    print(margen_trimestral)

def read_excel_book(archivo):
    global margen_trimestral
    xl = pd.ExcelFile(archivo)
    df = xl.parse('Estado de Resultados')
    df_data = pd.DataFrame(df)
    data = df_data.iloc[[5,33],[3]] 
    
    trimestre = os.path.basename(archivo).replace(".xlsx","").split("Q")
    quarter = trimestre[0]
    anio = trimestre[1]
    ingresos = data.iloc[0].values 
    resultado = data.iloc[1].values 
    margen = ingresos / resultado 
    fila = [(anio,quarter,ingresos,resultado, margen)]
    #matris = np.matrix(margen_trimestral)
    margen_trimestral = margen_trimestral.append(fila,ignore_index=True)

def walk_folder(argv):
    files = []
    ruta = "C:\\Users\\devel\\Downloads\\SQM\\Financieros"
    #r= dirpath, d=dirnames, f=filenames    
    for (r,d,f) in os.walk(ruta):
        for file in f:
            if '.xlsx' in file:
                files.append(os.path.join(r,file)) 

    for f in files:
        read_excel_book(f)

if __name__ == "__main__":
    main(sys.argv)