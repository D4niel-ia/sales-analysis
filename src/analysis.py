import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    df['Revenue'] = df['gross income']  # ajustar conforme dataset
    return df

def receita_anual_mensal(df):
    monthly = df.groupby(['Year','Month'])['Revenue'].sum().reset_index()
    sns.barplot(x='Month', y='Revenue', data=monthly, palette="Blues_d")
    plt.title("Receita Mensal")
    plt.xticks(rotation=45)
    plt.savefig("prints/revenue_month.png")
    plt.show()

def receita_por_pagamento(df):
    sns.countplot(x="Payment", data=df, palette="Set2")
    plt.title("Distribuição por Método de Pagamento")
    plt.savefig("prints/revenue_payment.png")
    plt.show()

def receita_por_produto(df):
    product_revenue = df.groupby("Product line")["Revenue"].sum().reset_index()
    fig = px.bar(product_revenue, x="Product line", y="Revenue",
                 title="Receita por Linha de Produto", color="Revenue")
    fig.write_image("prints/revenue_by_product.png")
    fig.show()

def receita_por_cliente(df):
    customer_rev = df.groupby("Customer type")["Revenue"].sum().reset_index()
    fig = px.pie(customer_rev, values="Revenue", names="Customer type",
                 title="Participação no Faturamento por Tipo de Cliente")
    fig.write_image("prints/revenue_by_customer.png")
    fig.show()

if __name__ == "__main__":
    df = carregar_dados("data/supermarket_sales.csv")
    receita_anual_mensal(df)
    receita_por_pagamento(df)
    receita_por_produto(df)
    receita_por_cliente(df)

# Salvar o DataFrame tratado
df.to_csv("data/supermarket_sales_clean.csv", index=False)

# Exportar gráficos como imagens (para README)
fig.write_image("prints/revenue_by_product.png")