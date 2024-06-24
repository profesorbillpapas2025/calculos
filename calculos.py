import streamlit as st
import math

# Función para calcular el área y el perímetro de un rectángulo
def calcular_rectangulo(largo, ancho):
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    return area, perimetro

# Función para calcular el área y el perímetro de un cuadrado
def calcular_cuadro(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro

# Función para calcular el área y el perímetro de un círculo
def calcular_circulo(radio):
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Configuración de la aplicación de Streamlit
st.title("Calculadora de Área y Perímetro")

# Selección del tipo de figura geométrica
figura = st.selectbox("Selecciona la figura geométrica", ["Rectángulo", "Cuadro", "Círculo"])

if figura == "Rectángulo":
    largo = st.number_input("Ingresa el largo", min_value=0.0, step=0.1)
    ancho = st.number_input("Ingresa el ancho", min_value=0.0, step=0.1)
    if st.button("Calcular"):
        area, perimetro = calcular_rectangulo(largo, ancho)
        st.write(f"Área del Rectángulo: {area}")
        st.write(f"Perímetro del Rectángulo: {perimetro}")

elif figura == "Cuadro":
    lado = st.number_input("Ingresa el lado", min_value=0.0, step=0.1)
    if st.button("Calcular"):
        area, perimetro = calcular_cuadro(lado)
        st.write(f"Área del Cuadro: {area}")
        st.write(f"Perímetro del Cuadro: {perimetro}")

elif figura == "Círculo":
    radio = st.number_input("Ingresa el radio", min_value=0.0, step=0.1)
    if st.button("Calcular"):
        area, perimetro = calcular_circulo(radio)
        st.write(f"Área del Círculo: {area}")
        st.write(f"Perímetro del Círculo: {perimetro}")
