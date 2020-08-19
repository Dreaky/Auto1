from robot.api.deco import keyword, library
from robot.libraries import BuiltIn
import os
import logging
import requests
import xml.etree.ElementTree as ET
from robot.libraries import BuiltIn
from ecpResponses import responses

# This disables SSL warning for ignored cerificate verification
requests.packages.urllib3.disable_warnings()

@library(scope="GLOBAL", version="0.1")
class ecpClient:

    def __init__(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        self.rfBuiltIn = BuiltIn.BuiltIn()
        pass

    @keyword('ECP call to ${url} with body ${xml_tree} is successful')
    def ecp_call_success(self, url, xml_tree):
        rc_hex, ecp_xml_tree, rc_msg = self.ecp_call(url, xml_tree)
        resp_message = self.get_value_from_tree('message', ecp_xml_tree, variable_name='default_tag_value')
        assert rc_hex == '0', f'RC is: {rc_hex}, but should be 0!\nResponse message: {resp_message}\nErr_msg: {rc_msg}'
        return rc_hex, ecp_xml_tree, rc_msg

    @keyword('ECP call to ${url} with body ${xml_tree} is made')
    def ecp_call(self, url, xml_tree):
        ET.register_namespace('ecp', 'http://www.eset.com/2012/02/ecp')
        headers = {'content-type': 'text/xml'}
        xml_tree = xml_tree.getroot()
        request_string = ET.tostring(xml_tree)
        print(f"--- REQUEST: {request_string}")
        resp = requests.post(url, data=request_string, headers=headers, verify=False).content
        print(f"--- RESPONSE: {resp}")
        ecp_xml_tree = ET.fromstring(resp)
        rc_hex = self.get_value_from_tree('code', ecp_xml_tree, variable_name='default_tag_value')
        rc_parsed = self.parse_ecp_rc(rc_hex)
        rc_msg = self.construct_error_msg(rc_parsed)
        self.rfBuiltIn.set_suite_variable(f"$latestXmlTree", ecp_xml_tree)
        self.rfBuiltIn.set_suite_variable(f"$latestRcHex", rc_hex)
        return rc_hex, ecp_xml_tree, rc_msg

    @keyword('Value of response error ${rc_hex} should be ${expected_value}')
    def assert_rc_hex(self, rc_hex, expected_value):
        assert rc_hex == expected_value, f"Value of response error should be {expected_value}, but it is {rc_hex}!"

    @keyword('XML string is loaded from ${filepath} and stored to ${variable_name}')
    def xml_string_from_file(self, filepath, variable_name):
        with open(filepath, 'r') as file:
            xml_string = file.read().replace('\n', '')
        self.rfBuiltIn.set_suite_variable(f"${variable_name}", xml_string)
        return xml_string

    @keyword('XML tree is loaded from ${filepath} and stored to ${variable_name}')
    def xml_tree_from_file(self, filepath, variable_name):
        tree = ET.parse(filepath)
        self.rfBuiltIn.set_suite_variable(f"${variable_name}", tree)
        return tree

    @keyword('File content of ${filepath} is stored into ${variable_name}')
    def read_xml(self, filepath, variable_name):
        content = os.read(filepath)
        self.rfBuiltIn.set_suite_variable(f"${variable_name}", content)
        return content

    @keyword('Value of tag ${tag} from ${xml_tree} is stored into ${variable_name}')
    def get_value_from_tree(self, tag, xml_tree, variable_name):
        value = xml_tree.find(f".//{tag}").text
        self.rfBuiltIn.set_suite_variable(f"${variable_name}", value)
        return value

    @keyword('Value of tag ${tag} from ${xml_tree} should be ${expected_value}')
    def assert_value_from_tree(self, tag, xml_tree, expected_value):
        actual_value = xml_tree.find(f".//{tag}").text
        assert actual_value == expected_value, f"Tag: {tag} should have value: {expected_value}, but it is {actual_value}!"

    @keyword('A tag ${tag} value in ${xml_tree} is set to ${value}')
    def set_xml_value(self, tag, xml_tree, value):
        xml_tree = xml_tree.getroot()
        element = xml_tree.find(f".//{tag}")
        element.text = value
        print(f'Updated tree = {ET.tostring(xml_tree)}')
        return xml_tree


    @keyword('XML tree ${elementree} is converted to string and stored to ${variable name}')
    def xml_to_string(self, elementree, variable_name):
        xml_tree = elementree.getroot()
        xml_string = ET.tostring(xml_tree)
        self.rfBuiltIn.set_suite_variable(f"${variable_name}", xml_string)
        return xml_string


    def parse_ecp_rc(self, ecp_rc):
        """Format is: XSSUUEEE
        X represents error severity
        SS represents source of response error
        UU represents unit within a source
        EEE is detailed error code within a unit"""
        if len(ecp_rc) < 7:
            return ecp_rc
        severity = int(ecp_rc[0], 16)
        error_source = int(ecp_rc[1:3], 16)
        unit_within_source = int(ecp_rc[3:5], 16)
        detailed_error_code = int(ecp_rc[5:8], 16)
        return severity, error_source, unit_within_source, detailed_error_code

    def construct_error_msg(self, rc):
        msg = ""
        if rc == "0":
            msg += f'Request is successfull. Rc is: {rc},'
            logging.info(msg)
            return msg
        if len(rc) < 4:
            raise ValueError(f'Rc is shorther than expected Rc is: {rc}')

        severity = rc[0]
        error_source = rc[1]
        unit_within_source = rc[2]
        detailed_error_code = rc[3]
        try:
            sev_key = str(*responses[0])
            severity_msg = responses[0][sev_key][severity]
            msg += f'{severity_msg}: '

            error_source_key = str(*responses[error_source])
            msg += f'{error_source_key}: '
            unit_dict_location = responses[error_source][error_source_key][unit_within_source]

            if detailed_error_code == 0:
                if len(unit_dict_location) == 1:
                    unit_within_key = str(*unit_dict_location)
                    msg += f'{unit_within_key}: '
                else:
                    unit_within_key = unit_dict_location
                    msg += f'{unit_within_key}: '
                msg += f'No detailed error message.'
            else:
                unit_within_key = str(*unit_dict_location)
                detailed_error_msg = responses[error_source][error_source_key][unit_within_source][unit_within_key][
                    detailed_error_code]
                msg += f'{unit_within_key}: {detailed_error_msg}'
            msg = msg.replace(u'\xa0', u' ')
        except Exception as e:
            msg = f'Unable to parse RC Code, please check if responses dict or documentation are updated! e: {e}'
        return rc, msg
