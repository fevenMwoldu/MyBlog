
import urllib.request,json
from .models import Quotes


# Getting the Quotes base url
quotes_url = None

def configure_request(app):
    global quotes_url
    quotes_url = app.config['QUOTE_API_BASE_URL']


def get_quotes():
    # make quotes api call to retrieve quotes

    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = quotes_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data=url.read()
        get_quotes_response=json.loads(get_quotes_data)

        # quotes_results=None

        # if get_quotes_response['quotes']:
        #     quotes_list = get_quotes_response['quotes']
        #     quotes_results = process_results(quotes_list)

    return get_quotes_response

def process_results(get_quotes_response):
    quotes_result=[]
    for quote in quotes_list:
        author = quote.get('author')
        id = quote.get('id')
        quote = quote.get('quote')
        permalink  = quote.get('permalink')

        quote_object = Quotes(author,id,quote,permalink)
        quotes_result.append(quote_object)

    return quotes_result








