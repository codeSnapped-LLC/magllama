import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    auth_mode: str = os.getenv("AUTH_MODE", "jwt")  # Options: jwt, okta, ldap
    okta_client_id: str = os.getenv("OKTA_CLIENT_ID", "")
    okta_client_secret: str = os.getenv("OKTA_CLIENT_SECRET", "")
    okta_issuer: str = os.getenv("OKTA_ISSUER", "")
    ldap_server: str = os.getenv("LDAP_SERVER", "")
    ldap_user_dn: str = os.getenv("LDAP_USER_DN", "")
    ldap_password: str = os.getenv("LDAP_PASSWORD", "")
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_service_key: str = os.getenv("SUPABASE_SERVICE_KEY", "")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
