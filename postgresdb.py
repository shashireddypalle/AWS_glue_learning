import psycopg2

class PostgresObject():
    def _init_(self):
        self._user = '<username>'
        self._pw = '<password>'
        self._host = '<host link>'
        self._port = '<port number>'
        self._database = '<database name>'
        self._connection = psycopg2.connect(user=self._user, password=self._pw, host=self._host, port=self._port,
                                            database=self._database)
        # print('You have connected to Postgresql')

    def is_connect(self):
        return bool(self._connection)

    def _connect(self):
        try:
            self._connection = psycopg2.connect(user=self._user, password=self._pw, host=self._host, port=self._port,
                                                database=self._database)
        except Exception as e:
            error = str(e)
            raise Exception('Connection error :{0}'.format(error))
        return self._connection

    def connect(self):
        if self.is_connect():
            return self._connection

        return self._connect()

    def disconnect(self):
        if self.is_connect():
            self._connection.close()
            self._connection = None

def get_db():
    if 'db' not in g:
        g.db = PostgresObject()
        g.db.conn = g.db.connect()
        # click.echo('Database connection is opened.')
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.disconnect()
    #print('You have been disconnected from Postgresql')

def init_db():
    db = get_db()