import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class MgSantanaDoGarambeuSpider(DioenetSpider):
    TERRITORY_ID = "3158706"
    name = "mg_santana_do_garambeu"
    start_date = datetime.date(2022, 9, 22)
    city_code = "santana-do-garambeu"
