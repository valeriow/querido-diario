import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PbMaltaSpider(DioenetSpider):
    TERRITORY_ID = "2508802"
    name = "pb_malta"
    start_date = datetime.date(2022, 11, 9)
    city_code = "malta"
