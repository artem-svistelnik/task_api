from dotenv import load_dotenv, find_dotenv
import  os
from dotenv import dotenv_values
load_dotenv(find_dotenv())
SECRET_KEY  =  os . getenv ( "EMAIL" )
DATABASE_PASSWORD  =  os . getenv ( "1" )
dot_env_values = dotenv_values()

