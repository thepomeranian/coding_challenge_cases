from app import api
from HelloWorld import *
from Cases import *

api.add_resource(HelloWorld, '/')
api.add_resource(Cases, '/cases')
