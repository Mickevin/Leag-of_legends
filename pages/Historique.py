from functions import *

st.set_page_config(page_title="Leag of Legends Dashboard",
                     page_icon="https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600",
                     layout="wide")

show_sidebar()

database = DataBase('database_lol')

st.title("Historique des Champions")
#st.video("https://www.leagueoflegends.com/static/hero-c35bd03ceaa5f919e98b20c905044a3d.webm", start_time=0, format='video/webm')

df = pd.DataFrame(database.select_table('champions'))

if st.checkbox("Afficher l'historique des champions en fonction de la date de collecte"):
    date = st.selectbox('Choisir la date de collecte', df['time'].unique())
    st.write(df[df.time == date])

if st.checkbox("Afficher l'historique des champions en fonction du rôle"):
    role = st.multiselect('Choisir le rôle', df['role'].unique())
    st.write(df[df.role.apply(lambda x: x in role)])

if st.checkbox("Afficher l'historique des champions en fonction du nom"):
    name = st.selectbox('Choisir le nom', df['id_champion'].unique())
    st.write(df[df.id_champion == name])


st.title("League of Legends Bot !")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Posez-moi votre question sur les champions de League of Legends !"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chat_openAI(prompt, database)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})