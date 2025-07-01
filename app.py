import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Pedidos",     
    page_icon="📊",                        
    layout="wide"                          
)
# Dados fornecidos
total_pedidos = {
    "Mogi Alpha": 14,
    "Indaiatuba": 8,
    "São Carlos": 2,
    "Total": 24,
    "Total Bidu": 19
}

servicos_agendados = {
    "Mogi Alpha": 165,
    "Indaiatuba": 82,
    "São Carlos": 24,
    "Total": 24,
    "Total Bidu": 19
}

# Filtrar apenas as unidades (sem "Total" e "Total Bidu")
unidades = ["Mogi Alpha", "Indaiatuba", "São Carlos"]

# Criar DataFrame
df = pd.DataFrame({
    "Unidade": unidades,
    "Total de Pedidos": [total_pedidos[unidade] for unidade in unidades],
    "Serviços Agendados": [servicos_agendados[unidade] for unidade in unidades]
})

# Converter de wide para long para facilitar o gráfico de barras agrupadas
df_melted = df.melt(id_vars="Unidade", var_name="Tipo", value_name="Quantidade")

# Criar gráfico
fig = px.bar(df_melted, x="Unidade", y="Quantidade", color="Tipo", barmode="group",
             title="Total de Pedidos vs Serviços Agendados por Unidade")

# Mostrar no Streamlit
st.plotly_chart(fig)
