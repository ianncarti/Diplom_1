class TestBun:

    def test_bun_get_bun_name(self, default_bun):
        assert default_bun.get_name() == 'булобчка'

    def test_bun_get_bun_price(self, default_bun):
        assert default_bun.get_price() == 10
