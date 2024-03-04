from flask import Flask
from flask_login import LoginManager
import views
from user import get_user
from forms import SearchForm

lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)

def create_app():
    app = Flask(__name__)
    
    @app.context_processor
    def base():
        form = SearchForm()
        return dict(form=form)
           
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page, methods=["GET", "POST"])
    app.add_url_rule("/login", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    app.add_url_rule("/records", view_func=views.records_page, methods=['GET', 'POST'])
    app.add_url_rule("/records/<int:record_key>", view_func=views.record_page)
    app.add_url_rule("/records/<int:record_key>/edit", view_func=views.record_edit_page, methods=["GET", "POST"])
    app.add_url_rule("/new-record", view_func=views.record_add_page, methods=['GET', 'POST'])
    # SQL search
    app.add_url_rule("/data_for_search", view_func=views.sql_search, methods=['GET', 'POST'])
    app.add_url_rule("/search_result/<word_h>", view_func=views.search_result, methods=['GET', 'POST'])
    # Basic search
    app.add_url_rule("/basic_search", view_func=views.basic_search, methods=['POST'])
    app.add_url_rule("/basic_search/", view_func=views.home_page, methods=['GET', 'POST'])
    app.add_url_rule("/basic_search/<word_s>", view_func=views.basic_search_result, methods=['POST', 'GET'])
    #---------------------------------------------------------------------------------------   
           
    
    lm.init_app(app)
    lm.login_view = "login_page"
       
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
