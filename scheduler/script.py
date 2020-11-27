# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

import schedule
from doc.google_sheet import GoogleSheet
from constants import constants
from models.maddyness import Maddyness


def run():
    """
    Main function to run the program, gets companies name and url and add them to the Google Sheet
    """
    maddyness = Maddyness("https://www.maddyness.com/?s=MaddyMoney")
    sheet = GoogleSheet()
    article = maddyness.get_random_article()
    companies = article.get_companies()
    for company in companies:
        company.get_infos()
        print(company)
        sheet.add_company(company, f'Entreprises!A{constants.CURRENT_LINE}:B')
        constants.CURRENT_LINE += 1


class Script:
    """
    Class used to schedule the run of this program
    """
    def __init__(self, current_line):
        self.current_line = current_line

    def schedule(self, day, hour):
        """
        Schedule the run of the script based on provided parameters
        :param day: int
            Day to run the script, between 1 and 7
        :param hour: int
            Hour to run the script, between 0 and 23
        """
        command = f'schedule.every().{constants.WEEK_DAYS[day].lower()}.at("{hour}:00").do(run)'
        eval(command)
        print(f'Script will run every {constants.WEEK_DAYS[day]} at {hour}:00')
        print('Script running...')
        while True:
            schedule.run_pending()
