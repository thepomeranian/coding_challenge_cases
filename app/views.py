from app import api
from Cases import *

api.add_resource(Cases, '/cases')
