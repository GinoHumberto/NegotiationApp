import streamlit as st
import pandas as pd
import datetime
import os
import plotly.express as px
import base64
import psycopg2

# 1. Configuración de Base de Datos SQL

def get_db_connection():
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=6543 
    )
    return conn


# ----------------- #
#       Título      #
# ----------------- #

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Cargar imagen
img_base64 = get_base64_image("Media/Logo.png")

# CSS para el contenedor
st.markdown(f"""
    <style>
    .header-container {{
        background-image: url('{img_base64}');
        background-size: contain; /* Cambiado a 'contain' para que el logo se vea completo */
        background-repeat: no-repeat; /* Evita que la imagen se repita */
        background-position: left center; /* Alinea la imagen a la izquierda */
        
        height: 200px; /* Definimos una altura fija para tener control */
        padding-top: 0px; /* Empuja el texto hacia abajo */
        padding-right: 20px;
        
        display: flex;
        align-items: flex-end; /* Alinea el contenido hacia la parte inferior */
        justify-content: flex-end; /* Mueve el contenido hacia la derecha */
    }}
    
    .header-text {{
        background-color: rgba(0, 0, 0, 0);
        text-align: right; /* Alinea el texto a la derecha dentro de su caja */
    }}
    </style>
    
    <div class="header-container">
        <div class="header-text">
            <h1>Universidad de Congreso</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

with st.sidebar:
    st.title('Menu')
    # Usamos radio botones para navegación o botones independientes
    opcion = st.radio("Selecciona:", 
                     ['Guía de estudio', 'Test de Thomas-Kilmann'])

# Lógica para mostrar contenido basado en la selección
if opcion == 'Guía de estudio':
    st.header('Guía de estudio')
    st.image('Media/negotiationguide.jpg')
    
    # Nivel 1: Conceptos Básicos
    with st.expander("1. Conflictos"):
        st.write("Definición: \nSituación en la que dos o más partes se sienten en oposición respecto a metas o métodos (Davis) \nProceso que surge cuando una parte percibe que otra afecta negativamente algo que le importa (Robbins)")
        
        # Nivel 2: Sub-conceptos
        with st.expander("Disciplinas"):
            st.markdown("""
            * Sociología y antropología
            * Psicología (Touzard, Conductual y Freud)
            * Económica
            * Derecho
            * Medicina/Fisiología
            """)
        
        with st.expander('Clasificación según Moore'):
            st.markdown('''
            * Conflictos de valores
            * Conflictos estructurales
            * Conflictos de intereses
            * Conflictos de relaciones personales
            * Conflictos de información o datos
            ''')

        with st.expander('Clasificación según Deutsch'):
            st.markdown('''
            * Verídico
            * Contingente 
            * Desplazado
            * Mal atribuido
            * Latente
            * Falso
            ''')


    with st.expander("2. Métodos alternativos"):
        st.markdown('''
        * _Endógeno_ (Sin intervención de terceros)
        * _Exógeno_ (Participan terceros agenos)
        * _Judiciales_ (Como el jucio y la mediación)
        * _Extrajudiciales_ (La negociación y el arbitraje)
        * _Adversariales_ (Ganador y perdedor)
        * _No adversariales_ (Consensúan la solución)
        ''')


    with st.expander("3. Escuelas de negociación"):
        with st.expander('Escuela Clásica'):
            st.write('Concepto de torta fija, fijar posiciones, la relación no importa...')
        with st.expander('Escuela Cooperativa'):
            st.write('Agrandar el tamaño de la torta, ganar-ganar...')
            st.subheader('Principios')
            st.markdown('''
            * Separar a las personas del problema
            * Concentrarse en los intereses y no en las posiciones
            * Crear opciones de beneficio mutuo
            * Establecer criterios objetivos
            ''')
            st.subheader('Elementos')
            st.markdown('''
                * Intereses (dentro)
                * Opciones (dentro)
                * Alternativas (fuera)
                * Legitimidad (dentro)
                * Comunicación (fuera)
                * Relación (fuera)
                * Compromiso (fuera)
            ''')
        with st.expander('Escuela de pensamiento lateral'):
            st.write('Consiste en generar ideas nuevas mediante la restructuración de conceptos existentes.')

    
    with st.expander('4. Capacidad y proceso'):
        with st.expander('Capacidad negociadora'):
            st.markdown('''
                * Información: Escucha activa, investigación...
                * Marketing mix: Producto, Precio, Plaza, Promoción
                * Poder de negociación: MAAN, Relaciones...
                * Habilidad negociadora: Capacidad constuida o nata...
            ''')
        with st.expander('Proceso'):
            st.markdown('''
                * Pre-Negociación (variables: verde, amari...)
                * Negociación formal (Aplicación del plan)
                * Contratación (Formalización del acuerdo)
                * Ejecución del contrato (Cumplimiento, puede tener proble...)
            ''')
        

    with st.expander('5. Estilos de negociación y herramientas de comunicación'):
        with st.expander('Estilos de negociación'):
            st.write('Los 5 estilos según Thomas Kilman (Duro, Blando, Regateador, Evasivo, Cooperativo)')
        with st.expander('Herramientas de la comunicación'):
            st.markdown('''
                * Percepción (La construcción de la realidad de cada uno...)
                * Persuación (Técnicas para convencer...)
                * Comunicación (verbal, no verbal...)
                * Parafraseo (Devolver lo escuchado de diferente forma)
                * Empatía (Comprender a la otra persona)
                * Pregunta de replanteo
                * Emociones (Recomendable ver en el libro)
            ''')

    with st.expander('6. Sí de acuerdo!'):
        st.info('Tip: Lean el libro!')


elif opcion == 'Test de Thomas-Kilmann':
    st.header('Test de Thomas-Kilmann')

    # Creo ambas divisiones
    tab_alumno, tab_profesor = st.tabs(['📝 Realizar Test', '📊 Resultados'])

    with tab_alumno:
        st.title('Bienvenido al Test')
        st.write(
            '''
            En cada par de afirmaciones elige la opción que más se parezca a tu manera habitual de actuar.

            Es posible que ambas opciones te representen un poco, o que ninguna te describa perfectamente. Aun así, intenta seleccionar la que consideres más cercana a tu comportamiento real.

            No hay respuestas buenas ni malas.
            '''
        )
        st.divider()

        # EN CASO DE QUERER USARLO EN EL SEGUNDO CUATRIMESTRE, CAMBIAR ESTA LINEA.
        semestre_actual = '2026-1C' 

        nombre = st.text_input('Coloca tu nombre')

        # Iniciamos un diccionario que cuente los puntajes de cada Tipo de negociador:
        puntos = {'Duro': 0, 'Colaborador': 0, 'Regateador': 0, 'Evasivo': 0, 'Blando': 0}

        # ------- Preguntas ------- #
        preguntas =[
        {"p": "Cuando surge una diferencia en un trabajo grupal...", "a": "A) A veces prefiero que otra persona tome la iniciativa para resolverlo.", "b": "B) Me gusta enfocarme en los puntos en los que ambos coincidimos.", "cat_a": "Evasivo", "cat_b": "Blando"},
        {"p": "Cuando aparecen opiniones distintas...", "a": "A) Intento encontrar una solución práctica que deje conformes a todos en parte.", "b": "B) Intento comprender tanto lo que necesito yo como lo que necesita la otra persona.", "cat_a": "Regateador", "cat_b": "Colaborador"},
        {"p": "Cuando tengo claro lo que quiero lograr...", "a": "A) Suelo mantener el rumbo de mi propuesta.", "b": "B) Prefiero cuidar el clima de la relación incluso cuando pensamos distinto.", "cat_a": "Duro", "cat_b": "Blando"},
        {"p": "Frente a un desacuerdo en equipo...", "a": "A) Intento encontrar una alternativa que funcione para todos.", "b": "B) A veces priorizo lo que el otro considera importante para mantener una buena dinámica.", "cat_a": "Regateador", "cat_b": "Blando"},
        {"p": "Cuando aparece un problema entre personas...", "a": "A) Prefiero construir una solución conjunta.", "b": "B) Prefiero evitar situaciones que puedan generar tensión.", "cat_a": "Colaborador", "cat_b": "Evasivo"},
        {"p": "Si una conversación empieza a volverse incómoda...", "a": "A) Prefiero tomar cierta distancia antes de seguir.", "b": "B) Intento sostener la alternativa que considero más adecuada.", "cat_a": "Evasivo", "cat_b": "Duro"},
        {"p": "Cuando surge un desacuerdo importante...", "a": "A) Prefiero darme tiempo antes de decidir cómo abordarlo.", "b": "B) Estoy dispuesto a flexibilizar algunos puntos para avanzar.", "cat_a": "Evasivo", "cat_b": "Regateador"},
        {"p": "En discusiones sobre decisiones importantes...", "a": "A) Suelo mantenerme firme en los objetivos que considero importantes.", "b": "B) Prefiero aclarar las diferencias desde el comienzo.", "cat_a": "Duro", "cat_b": "Colaborador"},
        {"p": "Frente a diferencias menores...", "a": "A) A veces siento que no es necesario profundizar demasiado.", "b": "B) Intento que la decisión final refleje lo que considero más conveniente.", "cat_a": "Evasivo", "cat_b": "Duro"},
        {"p": "Cuando estoy en una discusión...", "a": "A) Intento explicar a la otra persona el razonamiento detras.", "b": "B) Prefiero buscar una alternativa intermedia.", "cat_a": "Duro", "cat_b": "Regateador"},
        {"p": "Cuando aparece un problema entre compañeros...", "a": "A) Prefiero hablarlo de manera abierta cuanto antes.", "b": "B) Intento manejar la situación de forma que la relación no se desgaste innecesariamente.", "cat_a": "Colaborador", "cat_b": "Blando"},
        {"p": "En conversaciones donde puede generarse tensión...", "a": "A) A veces prefiero no marcar demasiado mi posición.", "b": "B) Estoy dispuesto a ceder en algunos aspectos si también consideran los míos.", "cat_a": "Evasivo", "cat_b": "Regateador"},
        {"p": "Cuando el grupo tiene opiniones divididas...", "a": "A) Intento encontrar una alternativa equilibrada.", "b": "B) Si considero que una idea es correcta, intento explicar mis razones y sostenerla.", "cat_a": "Regateador", "cat_b": "Duro"},
        {"p": "Cuando trabajo una diferencia con otra persona...", "a": "A) Comparto mi mirada y también me interesa escuchar la del otro.", "b": "B) Intento explicar por qué considero válida mi propuesta.", "cat_a": "Colaborador", "cat_b": "Duro"},
        {"p": "Cuando percibo tensión en una conversación...", "a": "A) Prefiero suavizar el intercambio para mantener un buen vínculo.", "b": "B) Intento evitar que la situación escale innecesariamente.", "cat_a": "Blando", "cat_b": "Evasivo"},
        {"p": "Cuando debo expresar un desacuerdo...", "a": "A) Intento cuidar la forma en que transmito lo que pienso, aunque no diga todo inmediatamente.", "b": "B) Intento explicar por qué considero que mi propuesta puede ser razonable y útil.", "cat_a": "Blando", "cat_b": "Duro"},
        {"p": "Cuando considero importante un objetivo...", "a": "A) Suelo mantenerme enfocado en alcanzarlo.", "b": "B) Prefiero evitar discusiones.", "cat_a": "Duro", "cat_b": "Evasivo"},
        {"p": "Cuando la otra persona valora mucho su postura...", "a": "A) A veces prefiero respetarla aunque piense distinto.", "b": "B) Estoy dispuesto a ajustar parte de mi postura si eso nos ayuda a avanzar.", "cat_a": "Blando", "cat_b": "Regateador"},
        {"p": "Frente a un conflicto pendiente...", "a": "A) Prefiero hablarlo y aclararlo cuanto antes.", "b": "B) A veces necesito tiempo antes de retomar el tema.", "cat_a": "Colaborador", "cat_b": "Evasivo"},
        {"p": "Cuando surge una diferencia importante...", "a": "A) Prefiero conversar el problema en profundidad para entender todas las posiciones.", "b": "B) Busco una solución donde ambas partes obtengan algo positivo.", "cat_a": "Colaborador", "cat_b": "Regateador"},
        {"p": "Cuando comienzo una conversación difícil...", "a": "A) Intento tener en cuenta lo que la otra persona necesita o espera.", "b": "B) Prefiero ir directamente al tema principal.", "cat_a": "Blando", "cat_b": "Duro"},
        {"p": "Cuando hay posiciones muy distintas...", "a": "A) Intento construir una alternativa intermedia.", "b": "B) Procuro que mi propuesta sea tomada en cuenta y analizada.", "cat_a": "Regateador", "cat_b": "Duro"},
        {"p": "En trabajos o decisiones compartidas...", "a": "A) Me interesa que todos sientan que sus necesidades fueron consideradas.", "b": "B) A veces confío en que otra persona pueda manejar mejor la situación.", "cat_a": "Colaborador", "cat_b": "Evasivo"},
        {"p": "Cuando noto que algo es muy importante para la otra persona...", "a": "A) Suelo ser flexible para acompañar esa necesidad.", "b": "B) Intento acercarnos a una solución equilibrada.", "cat_a": "Blando", "cat_b": "Regateador"},
        {"p": "Cuando creo que una propuesta va a funcionar bien...", "a": "A) Intento explicar claramente sus ventajas.", "b": "B) También tomo en cuenta lo que la otra persona espera o necesita.", "cat_a": "Duro", "cat_b": "Blando"},
        {"p": "Cuando aparecen diferencias dentro de un grupo...", "a": "A) Prefiero construir una salida intermedia.", "b": "B) Intento que todos se sientan considerados en el resultado final.", "cat_a": "Regateador", "cat_b": "Colaborador"},
        {"p": "En conversaciones donde podría generarse conflicto...", "a": "A) A veces prefiero esperar antes de expresar completamente mi postura.", "b": "B) Si algo es importante para el otro, puedo adaptarme.", "cat_a": "Evasivo", "cat_b": "Blando"},
        {"p": "Cuando siento que una decisión puede tener consecuencias importantes...", "a": "A) Suelo sostener activamente las ideas que considero correctas.", "b": "B) Prefiero trabajar junto con la otra persona para encontrar una salida.", "cat_a": "Duro", "cat_b": "Colaborador"},
        {"p": "Cuando aparecen posiciones enfrentadas...", "a": "A) Intento acercar las diferencias con una alternativa equilibrada.", "b": "B) A veces pienso que no vale la pena profundizar ciertas discusiones.", "cat_a": "Regateador", "cat_b": "Evasivo"},
        {"p": "Cuando surge un problema con otra persona...", "a": "A) Intento expresar mis diferencias sin afectar innecesariamente el vínculo.", "b": "B) Prefiero conversar el problema directamente para resolverlo juntos.", "cat_a": "Blando", "cat_b": "Colaborador"}
        ]

        # 1. Define las respuestas seleccionadas en el session_state
        for i in range(len(preguntas)):
            if f"q{i}" not in st.session_state:
                st.session_state[f"q{i}"] = None # Inicializa vacío

        # 2. Renderizar el formulario (sin sumar puntos aquí)
        with st.form("cuestionario"):
            for i, q in enumerate(preguntas):
                st.subheader(f"Pregunta {i+1}")
                # Asignamos el valor al state al interactuar
                st.radio(q["p"], [q["a"], q["b"]], key=f"q{i}")

            enviado = st.form_submit_button("Calcular Resultados")

        # 3. Calcular puntos SOLO cuando se presiona el botón
        if enviado:
            # Validación: Revisar si alguna pregunta quedó en None
            sin_responder = [i+1 for i in range(len(preguntas)) if st.session_state[f"q{i}"] is None]

            if sin_responder:
                st.error(f"Por favor, responde las siguientes preguntas: {sin_responder}")
            else:
                # Cálculo de puntos
                puntos = {'Evasivo': 0, 'Blando': 0, 'Regateador': 0, 'Colaborador': 0, 'Duro': 0}
                for i, q in enumerate(preguntas):
                    respuesta = st.session_state[f"q{i}"]
                    if respuesta == q["a"]:
                        puntos[q["cat_a"]] += 1
                    else:
                        puntos[q["cat_b"]] += 1

                # GUARDADO SEGURO CON TRY-EXCEPT
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()

                    cursor.execute('''
                        INSERT INTO resultados ("Fecha", "Semestre", "Nombre", "Duro", "Colaborador", "Regateador", "Evasivo", "Blando")
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        semestre_actual,
                        nombre, 
                        puntos['Duro'],
                        puntos['Colaborador'],
                        puntos['Regateador'],
                        puntos['Evasivo'],
                        puntos['Blando']
                    ))

                    conn.commit()
                    cursor.close()
                    conn.close()
                    st.success("¡Resultados guardados con éxito!")
                    # Lógica de empate inteligente
                    valor_maximo = max(puntos.values())
                    estilos_ganadores = [k for k, v in puntos.items() if v == valor_maximo]

                    if len(estilos_ganadores) > 1:
                        estilo_final = f"Empate entre: {', '.join(estilos_ganadores)}"
                    else:
                        estilo_final = estilos_ganadores[0]

                    st.success(f'Tu perfil predominante es: **{estilo_final}**')

                    # Gráfico para el alumno
                    df_plot = pd.DataFrame(list(puntos.items()), columns=['Estilo', 'Puntos'])
                    fig = px.bar(df_plot, x='Estilo', y='Puntos', color='Estilo', title="Distribución de tu Perfil")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(f"Error al guardar: {e}")


    with tab_profesor:
        st.header('Resultados')

        try:
            conn = get_db_connection()
            df_resultados = pd.read_sql_query("SELECT * FROM resultados", conn)
            conn.close()

            if not df_resultados.empty:
                st.metric(label='Total de respuestas en este grupo', value=len(df_resultados))

                # Calcular promedios por estilo
                columnas_estilos = ['Duro', 'Colaborador', 'Regateador', 'Evasivo', 'Blando']
                promedios = df_resultados[columnas_estilos].mean().reset_index()
                promedios.columns = ['Estilo', 'Promedio']

                # 1. Tabla con estilo predominante (con color de fondo)
                st.subheader("📋 Detalle Individual")
                # Función para encontrar el estilo máximo por fila
                df_resultados['Dominante'] = df_resultados[columnas_estilos].idxmax(axis=1)
                st.dataframe(df_resultados[['Fecha', 'Nombre', 'Dominante']], width='stretch')

                # Gráfico de promedio del curso
                fig_curso = px.bar(promedios, x='Estilo', y='Promedio', 
                                   color='Estilo', title="🧬 Promedio de Estilos del Curso")
                st.plotly_chart(fig_curso)

                st.subheader('🧬 Perfil Psicométrico Grupal (Radar)')
                fig_radar = px.line_polar(
                    promedios, 
                    r='Promedio', 
                    theta='Estilo', 
                    line_close=True,
                    markers=True
                )
                fig_radar.update_traces(fill='toself', fillcolor='rgba(26, 115, 232, 0.2)')
                st.plotly_chart(fig_radar, width='stretch')

                # 2. Histograma de los estilos dominantes
                st.subheader("🧬 Distribución de Estilos Dominantes")
                fig_hist = px.histogram(df_resultados, x='Dominante', color='Dominante', 
                                        title="¿Cuántos alumnos tienen cada estilo predominante?")
                st.plotly_chart(fig_hist)

                # Opción para descargar datos
                st.download_button("Descargar Resultados (CSV)", 
                                   df_resultados.to_csv(index=False), 
                                   "resultados_curso.csv", "text/csv")
            else:
                st.info("Aún no hay resultados registrados.")

        except Exception as e:
            st.error(f"Error al cargar datos del curso: {e}")

    
st.divider()
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>Desarrollado por <b>Anci Gino</b> <p> Con ayuda de <b>Florencia Molina, Victoria Sbriglio<b> | Cátedra de Negociaciones | Universidad de Congreso © 2026</p>
</div>
""", unsafe_allow_html=True)