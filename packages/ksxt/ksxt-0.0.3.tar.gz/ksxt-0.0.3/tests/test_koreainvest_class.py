class TestKoreaInvest:
    @classmethod
    def setup_class(cls):
        """
        [class level texture] constructor
        """
        pass
        
    @classmethod
    def teardown_class(cls):
        """
        [class level texture] destructor
        """
        pass

    def test_fetch_ticker(self, koreainvest_exchange, sample_symbol_stock):
        res = koreainvest_exchange.fetch_ticker(sample_symbol_stock)
        assert res['rt_cd'] == '0'

    def test_fetch_historical_data(self, koreainvest_exchange, sample_symbol_stock):
        res = koreainvest_exchange.fetch_historical_data(sample_symbol_stock, time_frame='D')
        assert res['rt_cd'] == '0'

    def test_fetch_create_order(self, koreainvest_exchange, sample_symbol_stock, koreainvest_accnum):
        res = koreainvest_exchange.create_order(
            acc_num=koreainvest_accnum, 
            symbol=sample_symbol_stock,
            ticket_type='entry_long',
            price=0, 
            qty=10, 
            otype='market'
        )

        assert res['rt_cd'] == '0'