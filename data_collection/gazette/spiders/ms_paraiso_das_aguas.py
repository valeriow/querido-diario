import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class MgParaisoDasAguasSpider(DioenetSpider):
    TERRITORY_ID = "5006275"
    name = "mg_paraiso_das_aguas"
    start_date = datetime.date(2013, 9, 13)
    city_code = "paraiso-das-aguas"
