"""# Run a test server.
#Its only job is to start the module nothing else"""

from analyse import app
from flask_cors import CORS
CORS(app)
app.run(host='127.0.0.1', port=8080, debug=True)
