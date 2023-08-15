import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class RsBarraDoRibeiroSpider(DioenetSpider):
    TERRITORY_ID = "4301909"
    name = "rs_barra_do_ribeiro"
    start_date = datetime.date(2022, 7, 28)
    city_code = "barra-do-ribeiro"
