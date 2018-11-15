from flask import session
from flask_restful import Resource, reqparse, abort
from models import purchase_inventory


class PurchaseInventoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("auth", type=str, required=True, location="headers",
                        help="You are not authenticated")

    parser.add_argument("purchase_date", type=str)
    parser.add_argument("product_id", type=int)
    parser.add_argument("supplier_id", type=int)
    parser.add_argument("quantity", type=float)
    parser.add_argument("cost", type=float)
    parser.add_argument("status", type=str)
    parser.add_argument("updated_at", type=str)

    @staticmethod
    def checkAuth(token):
        if token == session["outlet"][4]:
            return True
        return False

    def get(self, id):
        data = PurchaseInventoryResource.parser.parse_args()
        if PurchaseInventoryResource.checkAuth(data["auth"]):
            params = {"id": id}
            database = session["outlet"][2]
            res = purchase_inventory.Purchase_inventory.find_purchase_inventory_by_id(
                database, params)
            if res:
                return res.json()
            abort(406, message="No values found")
        abort(401, message="Unauthorized access")

    def put(self, id):
        data = PurchaseInventoryResource.parser.parse_args()
        if PurchaseInventoryResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            pur = purchase_inventory.Purchase_inventory.find_purchase_inventory_by_id(
                database, {"id": id})
            userPur = purchase_inventory.Purchase_inventory(
                id, data["purchase_date"], data["product_id"], data["supplier_id"],
                data["quantity"], data["cost"], data["status"], data["updated_at"])
            params = {**pur.getParams(), **userPur.getParams()}

            key = {"id": id}

            res = purchase_inventory.Purchase_inventory.update_from_database(
                database, key, params)
            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")

    def delete(self, id):
        data = PurchaseInventoryResource.parser.parse_args()
        if PurchaseInventoryResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            res = purchase_inventory.Purchase_inventory.delete_from_database(database,
                                                                             {"id": id})
            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")


class PurchaseInventoriesResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("auth", type=str, required=True, location="headers",
                        help="You are not authenticated")
    parser.add_argument("purchase_date", type=str)
    parser.add_argument("product_id", type=int)
    parser.add_argument("supplier_id", type=int)
    parser.add_argument("quantity", type=float)
    parser.add_argument("cost", type=float)
    parser.add_argument("status", type=str)
    parser.add_argument("updated_at", type=str)

    @staticmethod
    def checkAuth(token):
        if token == session["outlet"][4]:
            return True
        return False

    def get(self):
        data = PurchaseInventoriesResource.parser.parse_args()
        if PurchaseInventoriesResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            rows = purchase_inventory.Purchase_inventory.get_all_rows(database)
            if rows:
                return rows
            abort(406, message="Bad Request")
        abort(401, message="Unauthorized access")

    def post(self):
        data = PurchaseInventoriesResource.parser.parse_args()
        if PurchaseInventoriesResource.checkAuth(data["auth"]):
            database = session["outlet"][2]
            purchase = purchase_inventory.Purchase_inventory(None, data["purchase_date"], data["product_id"], data["supplier_id"],
                                                             data["quantity"], data["cost"])

            params = purchase.getParams()
            res = purchase_inventory.Purchase_inventory.insert_into_database(
                database, params)

            if res:
                return {"message": "Accepted"}, 202
            abort(406, message="Insufficient values")
        abort(401, message="Unauthorized access")
