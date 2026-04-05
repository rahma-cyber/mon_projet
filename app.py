import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Network Calculator")

st.write("Entrez le réseau et le masque CIDR pour obtenir les hôtes disponibles et autres informations.")


with st.form(key='network_form'):
    network_input = st.text_input("Adresse réseau (ex: 192.168.10.0)")
    cidr_input = st.number_input("Masque CIDR", min_value=0, max_value=32, value=26)
    submit_button = st.form_submit_button(label='Afficher les hôtes')

if submit_button:
    
    try:
        hosts_response = requests.get(f"{API_URL}/hosts")
        hosts_data = hosts_response.json()
        
        count_response = requests.get(f"{API_URL}/count_hosts", params={"network": network_input, "cidr": cidr_input})
        count_data = count_response.json()

        st.subheader("Informations du réseau")
        st.write(f"Réseau: {network_input}/{cidr_input}")
        st.write(f"Nombre d'hôtes utilisables: {count_data.get('usable_hosts', 'Erreur')}")
        
        
        st.subheader("Liste des hôtes disponibles")
        if 'hosts' in hosts_data:
            for host in hosts_data['hosts']:
                st.write(host)


        import ipaddress
        net = ipaddress.ip_network(f"{network_input}/{cidr_input}")
        st.write(f"Adresse réseau: {net.network_address}")
        st.write(f"Adresse broadcast: {net.broadcast_address}")
        st.write(f"Masque: {net.netmask}")
        st.write(f"Passerelle (premier hôte): {list(net.hosts())[0] if len(list(net.hosts()))>0 else 'N/A'}")

    except Exception as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")