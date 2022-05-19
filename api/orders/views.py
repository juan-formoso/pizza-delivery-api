from flask_restx import Namespace, Resource

order_namespace=Namespace('orders', description="a namespace for orders")

@order_namespace.route('/')
class HelloOrder(Resource):
  def get(self):
    return {'message': 'Hello Orders'}
