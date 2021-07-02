from flask import Flask


# __name__ as reference to current file
app = Flask(__name__)

# now build the rest of the application now that app has been instantiated
# (configurations, additional packages, etc)

# build routes(paths)
from .import routes