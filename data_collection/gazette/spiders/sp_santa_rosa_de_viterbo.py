import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class RsBarraDoRibeiroSpider(DioenetSpider):
    TERRITORY_ID = "3547601"
    name = "sp_santa_rosa_de_viterbo"
    start_date = datetime.date(2022, 7, 20)
    city_code = "santa-rosa-de-viterbo"
