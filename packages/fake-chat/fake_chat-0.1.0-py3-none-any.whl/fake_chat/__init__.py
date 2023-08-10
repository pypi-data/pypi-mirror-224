from .__fake__ import fake as faketool

get_credentials = faketool.get_credentials
login = faketool.login_get_token
generate_share_token = faketool.generate_share_token
generate_pool_token = faketool.generate_pool_token

__all__ = ['faketool', 'get_credentials', 'login', 'generate_share_token', 'generate_pool_token']
