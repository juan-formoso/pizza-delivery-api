from flask_restx import Namespace, Resource

order_namespace=Namespace('orders', description="a namespace for orders")

@order_namespace.route('/orders')
class OrderGetCreate(Resource):
  def get(self):
    """
      Get all orders
    """
    pass

  def post(self):
    """
      Create an order
    """
    pass

@order_namespace.route('/order/<int:order_id>')
class OrderGetUpdateDelete(Resource):
  def get(self, order_id):
    """
      Retrieve an order by id
    """
    pass

  def put(self, order_id):
    """
      Update an order by id
    """
    pass

  def delete(self, order_id):
    """
      Delete an order by id
    """
    pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
  def get(self, user_id, order_id):
    """
      Retrieve a specific order by user id
    """
    pass

@order_namespace.route('/user/<int:user_id>/orders')
class GetAllOrdersByUser(Resource):
  def get(self, user_id):
    """
      Retrieve all orders by user id
    """
    pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
  def patch(self, order_id):
    """
      Update an order status
    """
    pass
