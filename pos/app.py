from flask import Flask, session, request, jsonify
from flask_restful import Api
from database import Database
from interval_update import ThreadingExample
from resource import product, purchase_inventory

app = Flask(__name__)
app.secret_key = "asdasdasdas"
api = Api(app)
mainDB = Database("stores.db")


@app.route('/authenticate')
def authenticate():
    token = request.headers["auth_token"]

    outlet = mainDB.get_rows("outlets", {"auth_key": token})[0]

    if outlet:
        session["outlet"] = outlet
        return jsonify({"message": "Access Granted"}), 200
    return jsonify({"message": "Unauthorized Access"}), 201


api.add_resource(product.ProductResource, "/product/<int:id>")
api.add_resource(product.ProductsResource, "/products")
api.add_resource(purchase_inventory.PurchaseInventoryResource,
                 "/purchase_inventory/<int:id>")
api.add_resource(purchase_inventory.PurchaseInventoriesResource,
                 "/purchase_inventories")

if __name__ == '__main__':
    app.run(debug=True, port=3306)
