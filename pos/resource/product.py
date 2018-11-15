from flask import session
from flask_restful import Resource, reqparse, abort
from models import product


class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("auth", type=str, required=True, location="headers",
                        help="You are not authenticated")
    parser.add_argument("name", type=str)
    parser.add_argument("type", type=str)
    parser.add_argument("color", type=str)
    parser.add_argument("status", type=str)
    parser.add_argument("updated_at", type=str)

    @staticmethod
    def checkAuth(token):
        if token == session["outlet"][4]:
            return True
        return False

    def get(self, id):
        data = ProductResource.parser.parse_args()
        if ProductResource.checkAuth(data["auth"]):
            params = {"id": id}
            database = session["outlet"][2]
            res = product.Product.find_product_by_id(database, params)
            if res:
                return res.json(), 200

            abort(406, message="No values found")
        abort(401, message="Unauthorized access")

    def put(self, id):
        data = ProductResource.parser.parse_args()
        if ProductResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            prod = product.Product.find_product_by_id(database, {"id": id})
            userProd = product.Product(
                id, data["name"], data["type"], data["color"], data["status"], data["updated_at"])
            params = {**prod.getParams(), **userProd.getParams()}

            key = {"id": id}

            res = product.Product.update_from_database(database, key, params)
            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")

    def delete(self, id):

        data = ProductResource.parser.parse_args()
        print(data)
        if ProductResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            res = product.Product.delete_from_database(database, {"id": id})
            print(res)
            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")


class ProductsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("auth", type=str, required=True, location="headers",
                        help="You are not authenticated")
    parser.add_argument("name", type=str)
    parser.add_argument("type", type=str)
    parser.add_argument("color", type=str)
    parser.add_argument("status", type=str)
    parser.add_argument("updated_at", type=str)

    @staticmethod
    def checkAuth(token):
        if token == session["outlet"][4]:
            return True
        return False

    def get(self):
        data = ProductResource.parser.parse_args()
        if ProductsResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            rows = product.Product.get_all_rows(database)
            if rows:
                return rows
            abort(406, message="Bad Request")
        abort(401, message="Unauthorized access")

    def post(self):
        data = ProductResource.parser.parse_args()
        if ProductResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            userProd = product.Product(None,
                                       data["name"], data["type"], data["color"])

            params = userProd.getParams()

            res = product.Product.insert_into_database(database, params)

            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")
