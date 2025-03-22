from sqlalchemy import create_engine

class requests:
    def __init__(self, db_connection_link):
        self.db = create_engine(db_connection_link)

    def edit(self, sql):
        self.connection = self.db.connect()
        self.transaction = self.connection.begin()
        self.connection.execute(sql)
        self.transaction.commit()
        self.connection.close()

    def select(self, sql):
        self.connection = self.db.connect()
        self.transaction = self.connection.begin()
        return self.connection.execute(sql)
        self.transaction.commit()
        self.connection.close()


