import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PrSantaMonicaSpider(DioenetSpider):
    TERRITORY_ID = "4115507"
    name = "pr_santa_monica"
    start_date = datetime.date(2020, 4, 17)
    city_code = "santa-monica"
