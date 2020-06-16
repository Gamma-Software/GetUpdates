from get_account_api.log import log
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer


class OnedriveInterface:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.api_base_url = 'https://api.onedrive.com/v1.0/'
        self.scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
        self.client = onedrivesdk.get_default_client(
            client_id=self.client_id,
            scopes=self.scopes)

    def authenticate(self):
        log("Onedrive: Authenticate")
        auth_url = self.client.auth_provider.get_auth_url(self.redirect_uri)
        # Block thread until we have the code
        code = GetAuthCodeServer.get_auth_code(auth_url, self.redirect_uri)
        # Finally, authenticate!
        self.client.auth_provider.authenticate(code, self.redirect_uri, self.client_secret)

    def upload_file(self, name, path_to_file):
        log("Onedrive: Upload: " + name)
        return self.client.item(drive='me', id='root').children[name].upload(path_to_file)

    def download_file(self, name, path_to_file):
        log("Onedrive: Download: " + name)
        root_folder = self.client.item(drive='me', id='root').children.get()
        id_of_file = root_folder[0].id

        self.client.item(drive='me', id=id_of_file).download(path_to_file)
