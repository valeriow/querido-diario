import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PrMarumbiSpider(DioenetSpider):
    TERRITORY_ID = "4115507"
    name = "pr_marumbi"
    start_date = datetime.date(2019, 2, 22)
    city_code = "marumbi"
