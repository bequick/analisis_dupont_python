import pandas as pd
import os 
import sys
import json

def main(argv):
    #read_excel_book(argv[1])
    show_excel(argv[1])

def read_json():
    with open("conf/balance.json", "r") as read_file:
        return json.load(read_file)

def show_excel(archivo):
    xl = pd.ExcelFile(archivo)
    df = xl.parse('Balance')
    df_data = pd.DataFrame(df)
    print(df_data)

def read_excel_book(archivo):
    data = read_json()
    linea = data['4Q15']
    trimestre = os.path.basename(archivo).replace(".xlsx","").split("Q")
    quarter = trimestre[0]
    anio = trimestre[1]
    xl = pd.ExcelFile(archivo)
    df = xl.parse('Balance')
    df_data = pd.DataFrame(df)
    data_b = df_data.iloc[[int(linea)],[2]]   
    print(df_data)
    """
    df = xl.parse('Estado de Resultados')
    
    df_data_er = pd.DataFrame(df)
    data_e = df_data_er.iloc[[33],[3]]   
    bn = data_e.iloc[0].values 
    patrimonio = data_b.iloc[0].values 
    roe = bn / patrimonio 
    print(data_b)
    fila = [(anio,quarter,bn,patrimonio, roe)]
    roe_trimestral = roe_trimestral.append(fila,ignore_index=True)
    print(roe_trimestral)
    """


if __name__ == "__main__":
    main(sys.argv)