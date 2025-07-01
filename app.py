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
    "Serviços Agendados - Maio": [165, 82, 24, 271, 271],
    "Total Perdidos - Maio": [14, 8, 2, 24, 19]
}

# Dados de junho
dados_junho = {
    "Unidade": ["Mogi Alpha", "Indaiatuba", "São Carlos", "Total", "Total Bidu"],
    "Serviços Agendados - Junho": [111, 58, 15, 184, 184],
    "Total Perdidos - Junho": [18, 14, 1, 33, 14]
}

# Criar DataFrames
df_maio = pd.DataFrame(dados_maio)
df_junho = pd.DataFrame(dados_junho)

# Unir os dados
df = pd.merge(df_maio, df_junho, on="Unidade")

# GRÁFICO 1 - SERVIÇOS AGENDADOS
df_agendados = df[["Unidade", "Serviços Agendados - Maio", "Serviços Agendados - Junho"]].set_index("Unidade").reset_index()
df_agendados_melt = df_agendados.melt(id_vars="Unidade", var_name="Mês", value_name="Quantidade")

fig_agendados = px.line(
    df_agendados_melt,
    x="Unidade",
    y="Quantidade",
    color="Mês",
    markers=True,
    text="Quantidade",
    title="📈 Comparativo - Serviços Agendados (Maio x Junho)",
    color_discrete_map={
        "Serviços Agendados - Maio": "#1f77b4",
        "Serviços Agendados - Junho": "#2ca02c"
    }
)
fig_agendados.update_traces(textposition="top center")

st.plotly_chart(fig_agendados)

# GRÁFICO 2 - PEDIDOS PERDIDOS
df_perdidos = df[["Unidade", "Total Perdidos - Maio", "Total Perdidos - Junho"]].set_index("Unidade").reset_index()
df_perdidos_melt = df_perdidos.melt(id_vars="Unidade", var_name="Mês", value_name="Quantidade")

fig_perdidos = px.line(
    df_perdidos_melt,
    x="Unidade",
    y="Quantidade",
    color="Mês",
    markers=True,
    text="Quantidade",
    title="📉 Comparativo - Pedidos Perdidos (Maio x Junho)",
    color_discrete_map={
        "Total Perdidos - Maio": "#ff7f0e",
        "Total Perdidos - Junho": "#d62728"
    }
)
fig_perdidos.update_traces(textposition="top center")

st.plotly_chart(fig_perdidos)
