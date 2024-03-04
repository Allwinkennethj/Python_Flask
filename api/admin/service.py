from common.response import success_response,failure_response
from common.connection import add_admin_db,get_password,delete_user_db,edit_user_db,get_user_db
from common.utils.hashing import check_passoword,hash_password
from api.admin.model import Admin_details

def check_user_pass(username=None,password=None):
    if username is not None:
        if password is not None:
            if check_user(username=username,):
                if check_password(password=password):
                    return True
                else:
                    return failure_response("password check", 500)
            else:
                return failure_response("username check", 500)
        else:
            return failure_response("password_empty", 500)
    else:
        return failure_response("user_name empty", 500)

def check_user(username=None):
    if username is None:
        return False
    return True

def check_password(password=None):
    if password is None:
        return False
    return True


def add_user_service(username=None,password=None,name=None):
    password=hash_password(password)
    response=add_admin_db(username=username,password=password,name=name)
    if response == "Success":
        return True
    else:
        return response


def check_if_correct(username=None,password=None):
    try:
        db_password=get_password(username=username,tablename=Admin_details).encode("utf8")
        password=password.encode("utf8")
        if check_passoword(password,db_password):
            return True
        else:
            return False
    except Exception as e:
        return str(e)

#
# def delete_user_service(username=None):
#     try:
#         if delete_user_db(username=username,tablename="Admin_details")=="Success":
#             return True
#         else:
#             return False
#     except Exception as e:
#         return str(e)
#
# def edit_user_service(username=None,name=None):
#     try:
#         if edit_user_db(username=username,name=name,tablename="Admin_details")=="Success":
#             return True
#         else:
#             return False
#     except Exception as e:
#         return str(e)
#
# def get_user_service(username=None,password=None):
#     try:
#         check_result=check_if_correct(username=username,password=password)
#         if check_result is True:
#             user=get_user_db(username=username,tablename="Admin_details")
#             res = {
#                 'id': user[0],
#                 'name': user[1],
#                 'username': user[2],
#                 'created_by': user[3]
#             }
#             return res
#         else:
#             return check_result
#     except Exception as e:
#         return str(e)