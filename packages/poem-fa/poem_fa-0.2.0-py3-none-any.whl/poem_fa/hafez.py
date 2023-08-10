import sqlite3
import pathlib
from poem_fa import utils
HAFEZ_CAT_ID = 24
MIN_ID = 2130
MAX_ID = 2624
class Hafez:
    def __init__(self) -> None:
        db_path = pathlib.Path(__file__).parent.absolute() / 'hafez.db'
        self.db = sqlite3.connect(db_path)

        self.cursor = self.db.cursor()
        self.ghazal = None

    def get_random_ghazal(self):

        query = f'select id from poem where cat_id = {HAFEZ_CAT_ID} and id between {MIN_ID} and {MAX_ID} order by Random() limit 1'
        self.cursor.execute(query)
        self.ghazal = self.cursor.fetchone()[0]
        return self.ghazal - MIN_ID + 1

    def get_ghazal(self,ghazal_id):
        ghazal_id = ghazal_id + MIN_ID - 1
        query = "select vorder, position , text from verse  where poem_id = ? order by vorder"
        self.cursor.execute(query, (ghazal_id,))
        return self.cursor.fetchall()

    def fal(self):
        ghazal_id = self.get_random_ghazal()
        ghazal_data = self.get_ghazal(ghazal_id)

        self.print_poem(ghazal=ghazal_data)
        return ghazal_data


    def print_poem(self, ghazal):
        for i, verse in enumerate(ghazal):
            if i % 2 == 0:
                continue
            print(utils.adopt_text(ghazal[i][-1]), end='\t')
            print(utils.adopt_text(ghazal[i-1][-1]), end='\n')


        