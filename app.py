import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Pedidos",
    page_icon="📊",
    layout="wide"
)

# Dados de maio
dados_maio = {
    "Unidade": ["Mogi Alpha", "Indaiatuba", "São Carlos", "Total", "Total Bidu"],
    "Maio - Serviços Agendados": [165, 82, 24, 24, 19],
    "Maio - Total Perdidos": [14, 8, 2, 24, 19]
}

# Dados de junho (print)
dados_junho = {
    "Unidade": ["Mogi Alpha", "Indaiatuba", "São Carlos", "Total", "Total Bidu"],
    "Junho - Serviços Agendados": [111, 58, 15, 184, 184],
    "Junho - Total Perdidos": [18, 14, 1, 33, 14]
}

# Criar DataFrames
df_maio = pd.DataFrame(dados_maio)
df_junho = pd.DataFrame(dados_junho)

# Mesclar horizontalmente
df = pd.merge(df_maio, df_junho, on="Unidade")

# Transformar para formato longo
df_melted = df.melt(id_vars="Unidade", var_name="Categoria", value_name="Quantidade")

# Criar gráfico
fig = px.bar(
    df_melted,
    x="Unidade",
    y="Quantidade",
    color="Categoria",
    barmode="group",
    title="Comparativo de Pedidos Perdidos e Serviços Agendados - Maio x Junho"
)

# Mostrar no Streamlit
st.plotly_chart(fig)
