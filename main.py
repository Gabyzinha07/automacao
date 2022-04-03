import pandas as pd
from twilio.rest import Client

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"]. values[0]
        print(f"No mes {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")

        # Your Account SID from twilio.com/console
        account_sid = "AC4869346e84ccbc351e627a869d4b00f2"
        # Your Auth Token from twilio.com/console
        auth_token = "a7fee008b455a68ac648367141107920"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+55***********",
            from_="+19388000494",
            body=f"No mes {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")







