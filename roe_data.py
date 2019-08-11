import sys
import sources
import pandas as pd
import os 
import json

locations = []
roe_trimestral = []

def main(argv):
    global locations 
    locations = read_json()
    ruta = "C:\\Users\\devel\\Downloads\\SQM\\Financieros"
    lst_sources = sources.Sources(ruta).walk_folder()
    for file in lst_sources:
        if '.xlsx' in file:
            read_excel_book(file)

def read_json():
    with open("conf/balance.json", "r") as read_file:
        return json.load(read_file)


def read_excel_book(archivo):
    global roe_trimestral
    trimestre_str = os.path.basename(archivo).replace(".xlsx","")
    trimestre = trimestre_str.split("Q")  #os.path.basename(archivo).replace(".xlsx","").split("Q")
    quarter = trimestre[0]
    anio = trimestre[1]
    
    xl = pd.ExcelFile(archivo)
    df = xl.parse('Balance')
    df_data = pd.DataFrame(df)
    print(trimestre_str)
    linea_balance = locations[trimestre_str]
    data_b = df_data.iloc[[int(linea_balance)],[2]]   

    df = xl.parse('Estado de Resultados')
    df_data = pd.DataFrame(df)
    data_e = df_data.iloc[[33],[3]]   
    
    bn = data_e.iloc[0].values 
    patrimonio = data_b.iloc[0].values 
    roe = bn / patrimonio 
    fila = [(anio,quarter,bn,patrimonio, roe)]

    print(fila)
    #roe_trimestral = roe_trimestral.append(fila,ignore_index=True)
    #print(roe_trimestral)
        

if __name__ == "__main__":
    main(sys.argv)