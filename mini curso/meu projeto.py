
import pandas as pd

# importar a base de dados
tabela_vendas=pd.read_excel('vendas.xlsx')

# visualizar a base de daos
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturameno por loja
faturamento=tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos vendidos por loja
Quantidade=tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(Quantidade)

print('_' * 45)

# ticket médio por produto por loja
ticket_medio= (faturamento['Valor Final'] / Quantidade ['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print (ticket_medio)

#enviar um email com relatorio
import win32com.client as win32
Outlook = win32.Dispatch('Outlook.application')
mail = Outlook.CreateItem(0)
mail.To = 'Ticianablue@gmail.com'
mail.Subject = 'Relatorio de vanda das lojas'
mail.HTMLBody =f'''
<p>Prezados.</p>

<p>Segue O Relatório com as Vendas das lojas.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade vendidas:</p>
{Quantidade.to_html()}

<p>Ticket Médio por produto em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}


<p>Qualquer dúvida estou à disposição.</p>

<p>Assim...</p>
 <p>deve Rodrigo Cabral</p> 
'''

mail.Send()

print('Email Enviado')