from flask import Blueprint
from common.response import success_response,failure_response
from api.user.service import (check_user_pass,add_user_service,
                              check_if_correct,delete_user_service,
                              edit_user_service,get_user_service,getall_service)
from flask import request,jsonify
import traceback
from flask_jwt_extended import jwt_required,get_jwt

user=Blueprint("user",__name__,url_prefix="/user")

@user.route("/adduser",methods=["POST"])
@jwt_required()
def add_user():
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

@user.route("/deleteuser",methods=["DELETE"])
@jwt_required()
def delete_user():
    try:
        username=request.args.get("username")
        password=request.args.get("password")
        if check_if_correct(username=username,password=password):
            if delete_user_service(username):
                return success_response("deleted successfully",200)
            else:
                return failure_response("internal server",500)
        else:
            return failure_response("password incorrect",401)
    except Exception as e:
        return failure_response("error",500)

@user.route("/edit",methods=["POST"])
@jwt_required()
def update_user():
    try:
        payload=request.get_json()
        username=payload.get("username")
        password=payload.get("password")
        name=payload.get("name")
        if check_if_correct(username=username,password=password) is True:
            if edit_user_service(username,name) is True:
                return success_response("edited successfully",200)
            else:
                return failure_response("cannot edit",500)
        else:
            return failure_response("password wrong",401)
    except Exception as e:
        return failure_response("server error",500)


@user.route("/getuser",methods=["GET"])
@jwt_required()
def get_user():
    try:
        payload=request.get_json()
        username=payload.get("username")
        password=payload.get("password")
        if check_if_correct(username=username,password=password) is True:
            user=get_user_service(username=username,password=password)
            return success_response(message=user, status_code=200)
        else:
            return failure_response("password wrong",401)
    except Exception as e:
        print(traceback.print_exception(e))
        return failure_response("view server error",500)


@user.route("/getalluser",methods=["GET"])
@jwt_required()
def getalluser():
    try:
        claims=get_jwt()
        if claims.get('sub')=="admin":
            page=request.args.get("page",default=1,type=int)
            per_page=request.args.get("per_page",default=3,type=int)
            result=getall_service(page,per_page)
            return jsonify({
                "users":result,
            }),200
        else:
            return failure_response("Admin access needed",401)
    except Exception as e:
        return failure_response("error",400)