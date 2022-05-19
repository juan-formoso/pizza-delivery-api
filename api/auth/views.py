from flask_restx import Namespace, Resource

auth_namespace=Namespace('auth', description="a namespace for authentication")

@auth_namespace.route('/')
class HelloAuth(Resource):
  def get(self):
    return {'message': 'Hello Auth'}
