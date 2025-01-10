
import logging

from app import create_app

app = create_app()

if __name__ == '__main__':
    logging.debug("demarrage de l'application.....")
    app.run(debug=False, host="0.0.0.0")