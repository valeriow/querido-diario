import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class RjSumidouroSpider(DioenetSpider):
    TERRITORY_ID = "3305703"
    name = "rj_sumidouro"
    start_date = datetime.date(2021, 7, 26)
    city_code = "sumidouro"
