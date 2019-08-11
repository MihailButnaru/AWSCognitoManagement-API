# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.config import Config
from api.adapters.aws_adapter import AWSConnection
from api.core.users import CognitoUserManagement
from api.core.app_clients import AppClientsManagement

_config = Config()
aws_conn = AWSConnection().client
user_manager = CognitoUserManagement(_config, aws_conn)
app_client_manager = AppClientsManagement(_config, aws_conn)