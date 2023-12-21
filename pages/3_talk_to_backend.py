import streamlit as st
import requests

backend_url = "http://veritas_server-backend-1:8000"

endpoint = "/"

r = requests.get(backend_url+endpoint)

st.write(r.json())


