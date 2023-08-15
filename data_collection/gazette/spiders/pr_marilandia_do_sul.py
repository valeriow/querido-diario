import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PrMarilandiaDoSulSpider(DioenetSpider):
    TERRITORY_ID = "4114906"
    name = "pr_marilandia_do_sul"
    start_date = datetime.date(2019, 12, 17)
    city_code = "marilandia-do-sul"
