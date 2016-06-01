import logging
import os
import connexion
from connexion.resolver import RestyResolver

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app = connexion.App(__name__)
    heroku_app = os.environ.get("HEROKU_APP_NAME")
    app_host = (heroku_app +'.herokuapp.com') if heroku_app else "127.0.0.1:8080"
    app.add_api('api.yaml', arguments={'host': app_host}, resolver=RestyResolver('api'))
    app.run(server='tornado', port=int(os.environ.get("PORT", 8080)))
