from itemadapter import ItemAdapter

class ScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        keys = ['chapters', 'comments', 'bookmarks']
        for key in keys:
            value = adapter.get(key)
            if(value[0] is None):
                adapter[key] = ["0"]
        string = adapter.get('words')
        adapter['words'] = int(string[0].replace(',', ''))
        return item

import mysql.connector

class SaveToMySQLPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '8cd6ef76', 
            database = 'fics'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS fics(
            id int NOT NULL auto_increment,
            name text,
            author text,
            date text,
            url VARCHAR(255),
            language text,
            words int,
            chapters text,
            comments text,
            kudos text,
            bookmarks text,
            hits text,
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):

        self.cur.execute(""" insert into fics (
            name,
            author,
            date,
            url,
            language,
            words,
            chapters,
            comments,
            kudos,
            bookmarks,
            hits
            ) values (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
                )""", (
            item["name"][0],
            item["author"][0],
            item["date"][0],
            item["url"][0],
            item["language"][0],
            item["words"],
            item["chapters"][0],
            item["comments"][0],
            item["kudos"][0],
            item["bookmarks"][0],
            item["hits"][0],
        ))

        self.conn.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
