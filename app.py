import streamlit as st

#--------------------------------------------------------------------------------Sidebar

st.sidebar.image("logo.png")
st.sidebar.title("Music Park")

estilo = ['POP', 'Sertanejo', 'Pagode', 'Samba', 'Rock']

cantor = {
    'POP' : ["Miley Cyrus", "Pablo Vittar", "David Kusher"],
    'Sertanejo' : ["Marília Mendonça", "Simone Mendes"],
    'Pagode' : ["Tiaguinho", "Ferrugem"],
    'Samba' : ["Alcione", "Zeca Pagodinho"],
    'Rock' : ["Freddie Mercury", "Ozzy Osbourne"] }

opcao = st.sidebar.selectbox(f"Qual estilo de música você procura", estilo)

if opcao:
    opcao_cantor = st.sidebar.selectbox(
        "selecione o cantor:",
        cantor[opcao]
    )


if opcao == "POP" and opcao_cantor == "Miley Cyrus":
    st.video('https://www.youtube.com/watch?v=19IG7ZfaxZ8')

elif opcao == "POP" and opcao_cantor == "Pablo Vittar":
    st.video('https://www.youtube.com/watch?v=T4vUVMO_Ewk')

elif opcao == "POP" and opcao_cantor == "David Kusher":
    st.video('https://www.youtube.com/watch?v=pjyN3rOhJl4')

elif opcao == "Sertanejo" and opcao_cantor == "Marília Mendonça":
    st.video('https://www.youtube.com/watch?v=UDVr3ab3NVM')

elif opcao == "Sertanejo" and opcao_cantor == "Simone Mendes":
    st.video('https://www.youtube.com/watch?v=KPQkb2AuXSw')

elif opcao == "Pagode" and opcao_cantor == "Tiaguinho":
    st.video('https://www.youtube.com/watch?v=Zl6X0BLV6bk')

elif opcao == "Pagode" and opcao_cantor == "Ferrugem":
    st.video('https://www.youtube.com/watch?v=o3dknP3jclw')

elif opcao == "Samba" and opcao_cantor == "Alcione":
    st.video('https://www.youtube.com/watch?v=WrCuw1U0lq8')

elif opcao == "Samba" and opcao_cantor == "Zeca Pagodinho":
     st.video('https://www.youtube.com/watch?v=Nm5N4iFLU0g')

elif opcao == "Rock" and opcao_cantor == "Freddie Mercury":
    st.video("https://www.youtube.com/watch?v=7gpVj_fzv4o")

elif opcao == "Rock" and opcao_cantor == "Ozzy Osbourne":
    st.video('https://www.youtube.com/watch?v=G3LvhdFEOqs')

# ------------------------------------------------------------------Button


if opcao == "POP" and opcao_cantor == "Miley Cyrus":
    st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/5YGY8feqx7naU7z4HrwZM6')

elif opcao == "POP" and opcao_cantor == "Pablo Vittar":
  st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/6tzRZ39aZlNqlUzQlkuhDV')

elif opcao == "POP" and opcao_cantor == "David Kusher":
   st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/33NVpKoXjItPwUJTMZIOiY')

elif opcao == "Sertanejo" and opcao_cantor == "Marília Mendonça":
   st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/1yR65psqiazQpeM79CcGh8')

elif opcao == "Sertanejo" and opcao_cantor == "Simone Mendes":
   st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/2eK9gcJQ6uqVvJL63dnOM3')

elif opcao == "Pagode" and opcao_cantor == "Tiaguinho":
    st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/1vppDmG3i5sXf3DJzrK4T1')

elif opcao == "Pagode" and opcao_cantor == "Ferrugem":
    st.link_button (label="Spotify", url = 'https://open.spotify.com/intl-pt/artist/5ZfBThYiIIhL7jHMG8gDB2')

elif opcao == "Samba" and opcao_cantor == "Alcione":
   st.link_button (label="Spotify", url = 'https://www.youtube.com/watch?v=WrCuw1U0lq8')

elif opcao == "Samba" and opcao_cantor == "Zeca Pagodinho":
     st.link_button (label="Spotify", url = 'https://www.youtube.com/watch?v=Nm5N4iFLU0g')

elif opcao == "Rock" and opcao_cantor == "Freddie Mercury":
    st.link_button (label="Spotify", url = "https://www.youtube.com/watch?v=7gpVj_fzv4o")

elif opcao == "Rock" and opcao_cantor == "Ozzy Osbourne":
    st.link_button (label="Spotify", url = 'https://www.youtube.com/watch?v=G3LvhdFEOqs')
