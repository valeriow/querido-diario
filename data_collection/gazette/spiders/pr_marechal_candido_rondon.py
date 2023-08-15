# Ver.. edição extra: https://plenussistemas.dioenet.com.br/list/marechal-candido-rondon?secao=&d=11%2F08%2F2023&pesquisa=

import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class PrMarechalCandidoRondonSpider(DioenetSpider):
    TERRITORY_ID = "4114609"
    name = "pr_marechal_candido_rondon"
    start_date = datetime.date(2012, 6, 19)
    city_code = "marechal-candido-rondon"
