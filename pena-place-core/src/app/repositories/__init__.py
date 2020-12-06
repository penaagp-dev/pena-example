from src.pkg.mariadb import get_cursor, get_connection
from src.app import app

__cursor__ = get_cursor()
__conn__ = get_connection()