import re
from urllib.parse import urlencode

import scrapy
from dateutil.rrule import DAILY, rrule

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class DioenetSpider(BaseGazetteSpider):
    def start_requests(self):
        base_url = f"https://plenussistemas.dioenet.com.br/list/{self.city_code}"

        for date in rrule(freq=DAILY, dtstart=self.start_date, until=self.end_date):
            url_params = {"d": date.strftime("%d/%m/%Y")}
            yield scrapy.Request(
                f"{base_url}?{urlencode(url_params)}",
                cb_kwargs={"gazette_date": date.date()},
            )

    def parse(self, response, gazette_date):
        REGEXP_EDITION_NUMBER = r"Edi..o\s.*\s(\d+)"

        if (
            response.css("h3>span.label-default::text").get()
            == "Sem registros encontrados..."
        ):
            self.logger.warning(f"No records found on date: {gazette_date}.")
        else:
            is_extra_edition = False
            gazettes_list = response.css("ul.lista-diarios>li")
            for gazette in gazettes_list:
                badges_list = gazette.css("span.badge::text")
                if len(badges_list) == 2:
                    is_extra_edition = True
                title = badges_list[0].get()
                gazette_url = gazette.css(".btn-group a").attrib["href"]
                match = re.search(REGEXP_EDITION_NUMBER.lower(), title.lower())
                if match:
                    gazette_number = match.group(1)
                    yield Gazette(
                        date=gazette_date,
                        edition_number=gazette_number,
                        is_extra_edition=is_extra_edition,
                        file_urls=[gazette_url],
                        power="executive",
                    )
