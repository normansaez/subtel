import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuración de la API de GCP
PROJECT_ID = 'your-project-id'
CREDENTIALS_FILE = 'path-to-your-service-account-file.json'

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

service = build('cloudresourcemanager', 'v1', credentials=credentials)

# Definición de roles específicos
roles_dict = {
    "Administrador": "roles/owner",
    "Operador Instalador": "roles/editor",
    "Representante EES": "roles/viewer",
    "Analista Avanzado": "roles/bigquery.admin",
    "Validador SUBTEL": "roles/pubsub.editor",
    "Consulta SUBTEL": "roles/pubsub.viewer",
    "Consulta MINEDUC": "roles/datastore.viewer",
    "Operador Seguimiento de Tickets": "roles/support.editor",
    "Operador M2M": "roles/iot.admin"
}

def get_iam_policy(project_id):
    request = service.projects().getIamPolicy(resource=project_id, body={})
    response = request.execute()
    return response

def set_iam_policy(project_id, policy):
    request = service.projects().setIamPolicy(resource=project_id, body={'policy': policy})
    response = request.execute()
    return response

def list_roles():
    policy = get_iam_policy(PROJECT_ID)
    roles = []
    for binding in policy.get('bindings', []):
        roles.append({'role': binding['role'], 'members': binding['members']})
    return roles

def add_role(user_email, role):
    policy = get_iam_policy(PROJECT_ID)
    binding_exists = False
    for binding in policy['bindings']:
        if binding['role'] == role:
            if f'user:{user_email}' not in binding['members']:
                binding['members'].append(f'user:{user_email}')
            binding_exists = True
            break
    if not binding_exists:
        policy['bindings'].append({'role': role, 'members': [f'user:{user_email}']})
    return set_iam_policy(PROJECT_ID, policy)

def remove_role(user_email, role):
    policy = get_iam_policy(PROJECT_ID)
    for binding in policy['bindings']:
        if binding['role'] == role:
            binding['members'] = [member for member in binding['members'] if member != f'user:{user_email}']
            break
    return set_iam_policy(PROJECT_ID, policy)

# Interfaz de Streamlit
st.title('Gestión de Roles en GCP')

# Listar roles
st.header('Roles Actuales')
roles = list_roles()
for role in roles:
    st.write(f"Role: {role['role']}")
    for member in role['members']:
        st.write(f"  - {member}")

# Asignar nuevo rol
st.header('Asignar Nuevo Rol')
user_email = st.text_input('Correo Electrónico del Usuario')
role_name = st.selectbox('Rol a Asignar', list(roles_dict.keys()))

if st.button('Asignar Rol'):
    if user_email and role_name:
        role = roles_dict[role_name]
        result = add_role(user_email, role)
        st.write('Rol asignado correctamente.')
    else:
        st.write('Por favor, introduce el correo electrónico del usuario y selecciona un rol.')

# Eliminar rol
st.header('Eliminar Rol')
user_email_remove = st.text_input('Correo Electrónico del Usuario para Eliminar Rol')
role_name_remove = st.selectbox('Rol a Eliminar', list(roles_dict.keys()), key='remove_role')

if st.button('Eliminar Rol'):
    if user_email_remove and role_name_remove:
        role = roles_dict[role_name_remove]
        result = remove_role(user_email_remove, role)
        st.write('Rol eliminado correctamente.')
    else:
        st.write('Por favor, introduce el correo electrónico del usuario y selecciona un rol.')

