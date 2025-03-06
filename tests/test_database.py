class TestDatabase:

    def test_database_available_buns_count(self, database):
        db_buns_count = len(database.buns)
        assert len(database.available_buns()) == db_buns_count

    def test_database_available_ingredients_count(self, database):
        db_ingredients_count = len(database.ingredients)
        assert len(database.available_ingredients()) == db_ingredients_count
