# Copyright 2019 Mihail Butnaru
import os

class Config():
    """
    Configuration parameters
    """
    ###### ==============================>[ AWS CONFIGURATION ]<===============================
    @property
    def AWS_SERVICE(self):
        """ Specify the name of the AWS service."""
        return os.getenv('AWS_SERVICE', 'cognito-idp')

    @property
    def AWS_ACCESS_KEY_ID(self):
        """ Specify the AWS access key ID."""
        return os.getenv('AWS_ACCESS_KEY_ID', 'AKIAVWZ6W7BHFSEUIGLH')

    @property
    def AWS_SECRET_ACCESS_KEY(self):
        """ Specify the AWS secret key."""
        return os.getenv('AWS_SECRET_ACCESS_KEY', 'PDz/jyHubMGnctygScFK1y799bRFuhFLhQsG3soA')

    @property
    def AWS_REGION_NAME(self):
        """ Specify the region of the service."""
        return os.getenv('AWS_REGION_NAME', 'us-east-1')

    @property
    def AWS_USER_POOL_ID(self):
        """ Specify the AWS pool id. """
        return os.getenv('AWS_USER_POOL_ID', 'us-east-1_OEZizBpCk')

    
    ###### ==============================>[ SWAGGER CONFIGURATION ]<===============================

    @property
    def SWAGGER_UI_DOC_EXPANSION(self):
        """ """
        return os.getenv('SWAGGER_UI_DOC_EXPANSION', 'list')

    @property
    def RESTPLUS_MASK_SWAGGER(self):
        """ """
        return os.getenv('RESTPLUS_MASK_SWAGGER', False)

    @property
    def RESTPLUS_VALIDATE(self):
        """ """
        return os.getenv('RESTPLUS_VALIDATE', True)

    @property
    def RESTPLUS_ERROR_404_HELP(self):
        """ """
        return os.getenv('RESTPLUS_ERROR_404_ERROR', False)