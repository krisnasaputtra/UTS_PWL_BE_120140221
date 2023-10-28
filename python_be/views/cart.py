from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from ..models import Cart

@view_config(route_name='carts', request_method='POST', renderer='json')
def create_product_cart(request):
    """ Create a new product cart record in the database. """
    db = request.dbsession
    data = request.json_body

    # Validate input data
    if not all(key in data for key in ('name', 'price', 'buy_amount')):
        return {'status': 404,'message': 'Missing required fields'}

    # Create a new Produk Cart object with the input values
    cart_product = Cart(name=data['name'], price=data['price'], buy_amount=data['buy_amount'], total_price=data['buy_amount'] * data['price'])

    # Add the new Cart to the database
    db.add(cart_product)
    db.flush()

    # Return the newly created cart product as JSON
    return {'status': 201,
            "message": "Cart Success Added",
            "data": cart_product.to_dict()}

@view_config(route_name='carts', request_method='GET', renderer='json')
def get_product_carts(request):
    """ Retrieve a list of product cart records from the database. """
    db = request.dbsession

    # Retrieve a list of product carts from the database
    carts_product = db.query(Cart).all()
    cart_product = [cart_product.to_dict() for cart_product in carts_product]

    # Return the list of product carts as JSON
    if carts_product is not None:
        return {'status': "200", 
            "message": "Success Get Product Cart",
            "data": cart_product}
    else:
        raise HTTPNotFound()

# @view_config(route_name='product', request_method='GET', renderer='json')
# def get_product(request):
#     """ Retrieve a product record from the database by ID. """
#     db = request.dbsession
#     product_id = request.matchdict['id']

#     # Retrieve the product from the database
#     product = db.query(Product).filter(Product.id == product_id).first()

#     # Return the product as JSON, or raise a 404 error if it doesn't exist
#     if product is not None:
#         return {'status': '200', 
#                 'message': "Success Get Product", 
#                 'data': product.to_dict() }
#     else:
#         raise HTTPNotFound()

# @view_config(route_name='product', request_method='PUT', renderer='json')
# def update_product(request):
#     """ Update an existing product record in the database. """
#     db = request.dbsession
#     product_id = request.matchdict['id']
#     data = request.json_body

#     # Retrieve the product from the database
#     product = db.query(Product).filter(Product.id == product_id).first()

#     # Update the Product with the input values
#     if product is not None:
#         if 'name' in data:
#             product.name = data['name']
#         if 'price' in data:
#             product.price = data['price']
#         if 'stock' in data:
#             product.stock = data['stock']

#         # Commit the changes to the database
#         db.flush()

#         # Return the updated movie as JSON
#         return {'status': 201,
#                 'message': "Success Update Product",
#                 'data': product.to_dict()}
#     else:
#         raise HTTPNotFound()

# @view_config(route_name='product', request_method='DELETE', renderer='json')
# def delete_product(request):
#     """ Delete a product record from the database by ID. """
#     db = request.dbsession
#     product_id = request.matchdict['id']

#     # Retrieve the product from the database
#     product = db.query(Product).filter(Product.id == product_id).first()

#     # Delete the product from the database
#     if product is not None:
#         db.delete(product)
#         db.flush()
#         # Return a success message as JSON
#         return {'message': 'Product deleted'}
#     else:
#         raise HTTPNotFound()