import pandas as pd


def files():
    # Preparación del archivo cl_transacciones
    cl_transacciones_df = pd.read_csv('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\'
                                      'CL_TRANSACCIONES_2022-02-26.csv', encoding='latin1', delimiter=';')
    cl_transacciones_df.to_csv('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\CL_TRANSACCIONES.csv', index=False,
                               encoding='latin1')

    # Preparación del archivo transbank
    transbank_df = pd.read_csv('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\Transbank 26 feb.csv',
                               encoding='latin1', skiprows=16, index_col=None, delimiter=";", parse_dates=True)
    transbank_df.to_csv('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\Transbank.csv', encoding='latin1')

    # Preparación del archivo sencillito
    sencillito_df = pd.read_excel('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\SENCILLITO-20220226.xls',
                                  skiprows=1)
    sencillito_df.to_csv('C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\SENCILLITO.csv', index=False)
