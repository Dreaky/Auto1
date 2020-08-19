import hashlib
import json

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword, library
from robot.api import logger
import DatabaseLibrary
import datetime

@library(scope="GLOBAL", version="0.1")
class helpers():

    def __init__(self):
        self.db = DatabaseLibrary.DatabaseLibrary()
        pass

    @keyword("An md5 hash of ${input_string} is stored into variable ${variable_name}")
    def calculate_md5(self, input_string, variable_name="default_hash_var"):
        logger.debug(f"Calcluating md5 from: {input_string}")
        hash = hashlib.md5(input_string.encode("utf-8")).hexdigest()
        BuiltIn().set_suite_variable(f"${variable_name}", hash)
        return hash

    @keyword("Safer pass headers for ${body} are stored into variable ${variable_name}")
    def prepare_saferpass_headers(self, body, variable_name):
        key = "F6D6CC53-2D2A-4181-A330-499A064B29A2"
        # TODO - QUOTES Around body???
        hash_input = f'{key}{body}'
        headers = {"Authorization": self.calculate_md5(input_string=hash_input).upper(),
                   "Content-Type": "application/json"
                   }
        BuiltIn().set_suite_variable(f"${variable_name}", headers)
        return headers

    @keyword("User ID is abstracted from ${queried_user} and stored to ${variable_name}")
    def abstract_uuid(self, queried_user, variable_name):
        # [0][6] is location of uuid in returned table from KW: User with name ${name} is queried and stored to variable ${var_name}
        uuid = str(queried_user[0][6])
        BuiltIn().set_suite_variable(f"${variable_name}", uuid)
        return uuid

    @keyword("Json with ${uuid} for body of request is stored into variable ${variable_name}")
    def prepare_saferpass_body(self, uuid, variable_name):
        body_json = {"id": str(uuid)}
        BuiltIn().set_suite_variable(f"${variable_name}", json.dumps(body_json))
        return json.dumps(body_json)

    @keyword("Update Date of queried user ${queried_var_name} should be updated to current date_time")
    def compare_spfw_dates(self, queried_var_name):
        update_date = queried_var_name[0][2]
        tolerance = datetime.timedelta(hours=3)
        delta_time = abs(update_date - datetime.datetime.now())
        logger.debug(f'Delta time is: {delta_time}')
        assert delta_time <= tolerance, f"Update Date: {update_date} is not updated within tolerance {tolerance}, actual delta_time: {delta_time}"

    @keyword("GES api headers for ${body} are stored into variable ${variable_name}")
    def ges_headers(self, body, variable_name):
        token = "fafc8bc0-2056-4b39-a3a1-ae1b12c12e66"
        hash_input = f"{token.upper()}{str(len(body))}"
        headers = {"Authorization": self.calculate_md5(input_string=hash_input),
                   "Content-Type": "application/json",
                   "Content-Length": str(len(body))
                   }
        BuiltIn().set_suite_variable(f"${variable_name}", headers)
        return headers