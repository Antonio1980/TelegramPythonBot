from helper.utils import Utils


class APIBase:

    def __init__(self):
        self.token = "1071984975:AAH2rEuvVpcStNlqAPvxpNuUjeiKyOEY2fw"
        self.base_url = f"https://api.telegram.org/bot{self.token}/"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "accept": "*/*"
        }
        (self.past_timestamp, self.curr_timestamp, self.future_timestamp) = Utils.get_timestamps()
        (self.past_date, self.curr_date, self.future_date) = Utils.get_dates()
