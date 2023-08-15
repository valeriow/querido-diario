import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class MsCassilandiaSpider(DioenetSpider):
    TERRITORY_ID = "5002902"
    name = "ms_cassilandia"
    start_date = datetime.date(2013, 3, 28)
    city_code = "cassilandia"
