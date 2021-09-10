import streamlit as st
import numpy as np
from Graphs.Grafo import Graph
from Graphs.Djikstra import Djikst
from Graphs.arestas import aresta

st.write(
"""
**Aeroportos USA**
"""
)

#Criando Sidebar
st.subheader("Escolha os dois Aeroportos:")

vertices=333

adj, distance = Graph(aresta,vertices)
ap1 = st.selectbox(options=list(range(1, vertices)), label='Aeroporto 1')
ap2 = st.selectbox(options=list(range(1, vertices)), label='Aeroporto 2')

if st.button('BUSCAR'):
    dist, path = Djikst(adj, distance, ap1-1, ap2-1)
    path= str(path)
    path=path.split()
    path[0]=str(ap1)
    st.success(f'A distância entre os aeroportos {ap1} e {ap2} é {dist}')
    st.success(f"O menor caminho é: {path}")#{'→'.join(path)}