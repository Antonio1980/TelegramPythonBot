import json
import requests
from helper import logger
from json import JSONDecodeError
from tg_api.base_api import APIBase
from tg_api.api_constants import *
from helper.log_decorator import automation_logger


class TelegramAPI(APIBase):
    def __init__(self):
        super(TelegramAPI, self).__init__()

    @automation_logger(logger)
    def get_me(self):
        uri = self.base_url + "getMe"
        try:
            logger.logger.info(F"API URL is GET- {uri}")
            _response = requests.get(url=uri, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.logger.error(F"{e.__class__.__name__} get_me failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_updates(self):
        uri = self.base_url + "getUpdates"
        try:
            logger.logger.info(F"API URL is GET- {uri}")
            _response = requests.get(url=uri, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.logger.error(F"{e.__class__.__name__} get_updates failed with error: {e}")
            raise e

    @automation_logger(logger)
    def send_message(self, chat_id: int, message: str) -> tuple:
        uri = self.base_url + "sendMessage"
        payload = json.dumps({"chat_id": chat_id, "text": message})
        logger.logger.info(REQUEST_BODY.format(payload))
        try:
            logger.logger.info(F"API URL is POST- {uri}")
            _response = requests.post(url=uri, data=payload, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.logger.error(F"{e.__class__.__name__} send_message failed with error: {e}")
            raise e

    @automation_logger(logger)
    def send_location(self, chat_id: int, latitude: float, longitude: float) -> tuple:
        uri = self.base_url + "sendLocation"
        payload = json.dumps({"chat_id": chat_id, "latitude": latitude, "longitude": longitude})
        try:
            logger.logger.info(F"API URL is POST- {uri}")
            _response = requests.post(url=uri, data=payload, headers=self.headers)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as e:
                logger.logger.error(f"Failed to parse response json: {e}")
                if _response.text is not None:
                    body = _response.text
                else:
                    body = _response.reason
            logger.logger.info(RESPONSE_TEXT.format(body))
            return body, _response
        except Exception as e:
            logger.logger.error(F"{e.__class__.__name__} send_location failed with error: {e}")
            raise e
