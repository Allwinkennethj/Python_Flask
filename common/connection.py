from config import db
from api.admin.model import Admin_details
from api.user.model import User_details
import traceback
from api.user.UserSchema import UserSchema
def add_user_db(username=None,name=None,password=None):
    try:
        user=User_details(
            username=username,
            name=name,
            password=password,
        )
        db.session.add(user)
        user=db.session.query(User_details).filter_by(username=username).first()
        user.created_by=username
        db.session.commit()
        return "Success"
    except Exception as e:
        print(traceback.print_exception(e))
        return str(e)

def add_admin_db(username=None,name=None,password=None):
    try:
        user=Admin_details(
            username=username,
            name=name,
            password=password,
        )
        db.session.add(user)
        user=db.session.query(Admin_details).filter_by(username=username).first()
        user.created_by=username
        db.session.commit()
        return "Success"
    except Exception as e:
        print(traceback.print_exception(e))
        return str(e)

def get_password(username=None,tablename=User_details):
    try:
        password=db.session.query(tablename).filter_by(username=username).first().password
        return password
    except Exception as e:
        return str(e)


def delete_user_db(username=None,tablename=User_details):
    try:
        db.session.query(tablename).filter_by(username=username).delete()
        db.session.commit()
        return "Success"
    except Exception as e:
        return str(e)

def edit_user_db(username=None,name=None,tablename=User_details):
    try:
        user=db.session.query(tablename).filter_by(username=username).first()
        user.name=name
        db.session.commit()
        return "Success"
    except Exception as e:
        return str(e)

def get_user_db(username=None,tablename=User_details):
    try:
        user=db.session.query(tablename.id,tablename.name,tablename.username,tablename.created_by).filter_by(username=username).first()
        return user
    except Exception as e:
        return str(e)

def getall_con(page=None,per_page=None):
    try:
        users=User_details.query.paginate(
            page=page,
            per_page=per_page
        )

        result=UserSchema().dump(users,many=True)

        return result
    except Exception as e:
        return None