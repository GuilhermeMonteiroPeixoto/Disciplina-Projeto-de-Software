import pandas as pd

Taxas_Servicos = pd.DataFrame(columns=['Nome','Taxas','Adicional'])

def addTaxaAdicional(Nome, Taxas_Servicos, Cad_Funcionario, new_value):
    if (Cad_Funcionario.Nome == Nome).any():
        Taxas_Servicos.iloc[Taxas_Servicos[Taxas_Servicos['Nome'] == Nome].index, Taxas_Servicos.columns.get_loc('Adicional')] = str(new_value)
        
    return Taxas_Servicos
