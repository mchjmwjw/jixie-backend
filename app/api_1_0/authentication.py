from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(email, password):
#     if email == '':
#         g.current_user = AnonymousUser()
#         return True
