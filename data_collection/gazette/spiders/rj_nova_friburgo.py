import datetime

from gazette.spiders.base.dioenet import DioenetSpider


class RjNovaFriburgoSpider(DioenetSpider):
    TERRITORY_ID = "3303401"
    name = "rj_nova_friburgo"
    start_date = datetime.date(2019, 10, 17)
    city_code = "nova-friburgo"
