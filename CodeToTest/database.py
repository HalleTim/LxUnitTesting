class Database:
    def connect(self):
        self.connection = True

    def disconnect(self):
        self.connection = False

    def execute(self, query):
        if not self.connection:
            raise ConnectionError("Keine Verbindung zur Datenbank.")
        return f"Ergebnis für {query}"