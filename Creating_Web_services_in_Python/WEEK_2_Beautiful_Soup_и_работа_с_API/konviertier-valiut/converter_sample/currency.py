from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to,date,requests):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={
        'date_req': date})  # Использовать переданный requests
    soup = BeautifulSoup(response.content ,"lxml")
    list_of_all_codes = soup.findAll("valute")
    spec_list = []
    if( (cur_from == 'RUR') and (cur_to == 'RUR')):
        return amount
    if(cur_from == 'RUR'):
        for tags in list_of_all_codes:
            if (tags.charcode.text == cur_to):
                spec_list.append(Decimal(tags.value.text.replace(',','.')))
                spec_list.append(Decimal(tags.nominal.text.replace(',','.')))
        result = ((amount*spec_list[1])/spec_list[0])
    else:
        for tags in list_of_all_codes:
            if (tags.charcode.text == cur_from):
                spec_list.append(Decimal(tags.value.text.replace(',','.')))
                spec_list.append(Decimal(tags.nominal.text.replace(',','.')))
            if (tags.charcode.text == cur_to):
                spec_list.append(Decimal(tags.value.text.replace(',','.')))
                spec_list.append(Decimal(tags.nominal.text.replace(',','.')))
        result = (amount * spec_list[0]/spec_list[1])/(spec_list[2]/spec_list[3])
    return result.quantize(Decimal("1.0000"))  # не забыть про округление до 4х знаков после запятой


#result = convert( 1000, 'RUR', 'JPY',"02/03/2020",requests)
#print(result)
