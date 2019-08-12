# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.config import Config
from api.wrappers.users import UserManagement
from api.wrappers.app_clients import AppClientsManagement

_config = Config()
user_manager = UserManagement(_config)
app_client_manager = AppClientsManagement(_config)