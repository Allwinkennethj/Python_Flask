from flask import Blueprint
from common.response import success_response,failure_response
from api.admin.service import (check_user_pass,add_user_service,
                              check_if_correct)
from flask import request,jsonify
import traceback
from flask_jwt_extended import create_access_token,create_refresh_token

admin=Blueprint("admin",__name__,url_prefix="/admin")

@admin.route("/login",methods=["POST"])
def login_user():
    try:
        payload=request.get_json()
        username=payload.get("username")
        password=payload.get("password")
        checking=check_if_correct(username=username,password=password)
        if checking is True:
            access_token=create_access_token(identity=username)
            refresh_token=create_refresh_token(identity=username)
            return jsonify(
                {
                    "message":"logged in",
                    "token":{
                        "access":access_token,
                        "refresh":refresh_token
                    }
                }
            ),200
        else:
            return checking

    except Exception as e:
        print(traceback.print_exception(e))
        return failure_response(str(e),500)




@admin.route("/addadmin",methods=["POST"])
def add_admin():
    try:
        payload=request.get_json()
        username=payload.get("username")
        password=payload.get("password")
        name=payload.get("name")
        checking=check_user_pass(username=username,password=password)
        if checking is True:
            if add_user_service(username=username,password=password,name=name) is True:
                return success_response("added successfully",200)
            else:
                return failure_response("not added successfully",500)
        else:
            return checking

    except Exception as e:
        return failure_response(str(e),500)
#
# @admin.route("/deleteadmin",methods=["DELETE"])
# def delete_admin():
#     try:
#         username=request.args.get("username")
#         password=request.args.get("password")
#         if check_if_correct(username=username,password=password):
#             if delete_user_service(username):
#                 return success_response("deleted successfully",200)
#             else:
#                 return failure_response("internal server",500)
#         else:
#             return failure_response("password incorrect",401)
#     except Exception as e:
#         return failure_response("error",500)
#
# @admin.route("/editadmin",methods=["POST"])
# def update_admin():
#     try:
#         payload=request.get_json()
#         username=payload.get("username")
#         password=payload.get("password")
#         name=payload.get("name")
#         if check_if_correct(username=username,password=password) is True:
#             if edit_user_service(username,name) is True:
#                 return success_response("edited successfully",200)
#             else:
#                 return failure_response("cannot edit",500)
#         else:
#             return failure_response("password wrong",401)
#     except Exception as e:
#         return failure_response("server error",500)
#
# @admin.route("/getadmin",methods=["GET"])
# def get_admin():
#     try:
#         payload=request.get_json()
#         username=payload.get("username")
#         password=payload.get("password")
#         if check_if_correct(username=username,password=password) is True:
#             user=get_user_service(username=username,password=password)
#             return success_response(message=user, status_code=200)
#         else:
#             return failure_response("password wrong",401)
#     except Exception as e:
#         print(traceback.print_exception(e))
#         return failure_response("view server error",500)
