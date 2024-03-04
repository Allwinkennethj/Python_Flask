from common.response import success_response,failure_response
from common.connection import add_user_db,get_password,delete_user_db,edit_user_db,get_user_db,getall_con
from common.utils.hashing import check_passoword,hash_password


def getall_service(page=None,per_page=None):
    try:
        result=getall_con(page,per_page)
        if result==None:
            return failure_response("Connection error empty",500)
        else:
            return result
    except Exception as e:
        return failure_response("Service error",400)
def check_user_pass(username=None,password=None):
    if username is not None:
        if password is not None:
            if check_user(username=username):
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
    response=add_user_db(username=username,password=password,name=name)
    if response == "Success":
        return True
    else:
        return response


def check_if_correct(username=None,password=None):
    try:
        db_password=get_password(username).encode("utf8")
        password=password.encode("utf8")
        if check_passoword(password,db_password):
            return True
    except Exception as e:
        return str(e)


def delete_user_service(username=None):
    try:
        if delete_user_db(username=username)=="Success":
            return True
        else:
            return False
    except Exception as e:
        return str(e)

def edit_user_service(username=None,name=None):
    try:
        if edit_user_db(username=username,name=name)=="Success":
            return True
        else:
            return False
    except Exception as e:
        return str(e)

def get_user_service(username=None,password=None):
    try:
        check_result=check_if_correct(username=username,password=password)
        if check_result is True:
            user=get_user_db(username=username)
            res = {
                'id': user[0],
                'name': user[1],
                'username': user[2],
                'created_by': user[3]
            }
            return res
        else:
            return check_result
    except Exception as e:
        return str(e)