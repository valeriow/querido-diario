import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class AmPedraBrancaDoAmapariSpider(DioenetSpider):
    TERRITORY_ID = "1600154"
    name = "am_pedra_branca_do_amapari"
    start_date = datetime.date(2020, 3, 9)
    city_code = "pedra-branca-do-amapari"
