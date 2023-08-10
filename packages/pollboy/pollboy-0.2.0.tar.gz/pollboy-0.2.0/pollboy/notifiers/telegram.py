from pollboy.logger import get_logger
from pollboy.config import Config
import requests

log = get_logger(__name__)

def strip_unsupported_html(text):
    repl_map = {
        '<p>': '',
        '<br>': '',
        '<br/>': '',
        '<br />': '',
        '</p>': '\n',
        '<ul>': '',
        '<ol>': '',
        '<li>': ' - ',
        '</li>': '',
        '</ul>': '',
        '</ol>': '',
    }
    for token in repl_map:
        text = text.replace(token, repl_map[token])
    return text

def send_text_only(feed_item, settings):
    url = 'https://api.telegram.org/bot%s/sendMessage' % (settings['token'])
    return requests.post(url, data={
        'chat_id': settings['chat_id'],
        'text': strip_unsupported_html(feed_item.description),
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    })

def send_photo_message(feed_item, settings):
    url = 'https://api.telegram.org/bot%s/sendPhoto' % (settings['token'])
    photo_url = feed_item.get('tg-image')
    log.debug('getting image from ' + photo_url)
    return requests.post(url, data={
        'chat_id': settings['chat_id'],
        'photo': photo_url,
        'caption': strip_unsupported_html(feed_item.description),
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    })

def notify(feed_item, settings):
    response = None
    if 'tg-image' in feed_item:
        log.debug(f'Sending telegram photo message')
        response = send_photo_message(feed_item, settings)
    else:
        log.debug(f'Sending telegram text message')
        response = send_text_only(feed_item, settings)

    log.debug(f'Received status code {response.status_code}')
    if response.status_code > 300 or response.status_code < 200:
        log.error(response.json())