import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class RsBarraDoRibeiroSpider(DioenetSpider):
    TERRITORY_ID = "3547908"
    name = "sp_santo_antonio_da_alegria"
    start_date = datetime.date(2022, 11, 17)
    city_code = "santo-antonio-da-alegria"
