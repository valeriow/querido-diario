import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PrSaoPedroDoIguacuSpider(DioenetSpider):
    TERRITORY_ID = "4125753"
    name = "pr_sao_pedro_do_iguacu"
    start_date = datetime.date(2021, 5, 31)
    city_code = "sao-pedro-do-iguacu"
