# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.app import create_app
from api.config import Config

_config = Config()
app = create_app(_config)