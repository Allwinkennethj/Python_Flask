from factory import create_app
from config import db,jwt
from api.user.model import User_details
from api.admin.model import Admin_details

app=create_app()

db.init_app(app)
jwt.init_app(app)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()
    app.run(debug=True,host='0.0.0.0')