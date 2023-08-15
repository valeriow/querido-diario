import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class MgSacramentoSpider(DioenetSpider):
    TERRITORY_ID = "3156908"
    name = "mg_sacramento"
    start_date = datetime.date(2019, 2, 26)
    city_code = "sacramento"
