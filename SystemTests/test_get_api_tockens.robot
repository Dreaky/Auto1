*** Settings ***
Library  simpleRequests.py
Library  helpers.py
Library  ecpClient.py
Variables  variables.py

*** Variables ***
${cs_url}    ${CS_DEV}
${lic_key}    2RKW-X5H9-AVBX-3P82-6P78
${cs_url}    ${CS_TEST}
${seat_id}    5b3131fd-d50f-4ece-9f6f-3ba3ea9a7ce1

*** Test Cases ***
Get API Tokens
    Given A New Seat ID is obtained and stored to seat_id
      And Seat ${seat_id} is activated with associated license ${lic_key}
     When XML tree is loaded from ${CS_PAYLOAD_PATH}/getApiTokens.xml and stored to tokens_xml
      And A tag seatid value in ${tokens_xml} is set to ${seat_id}
      And ECP call to ${cs_url} with body ${tokens_xml} is successful
     Then Value of XML ${latestXmlTree} tag tenants should not be empty
     Then Value of XML ${latestXmlTree} tag status should be VALID

*** Keywords ***
A New Seat ID is obtained and stored to ${variable_name}
    XML tree is loaded from ${CS_PAYLOAD_PATH}/seatAssociationV2.xml and stored to seat_xml
    ECP call to ${cs_url} with body ${seat_xml} is successful
    Value of tag seatid from ${latestXmlTree} is stored into ${variable_name}

Seat ${seat_id} is activated with associated license ${lic_key}
     XML tree is loaded from ${CS_PAYLOAD_PATH}/activationStandalone.xml and stored to activation_xml
     A tag seatid value in ${activation_xml} is set to ${seat_id}
     A tag key value in ${activation_xml} is set to ${lic_key}
     ECP call to ${cs_url} with body ${activation_xml} is successful

Value of XML ${elementree} tag ${tag} should not be empty
Value of XML ${elementree} tag ${tag} should be ${expected_value}
    Value of tag ${tag} from ${elementree} is stored into actual_value
    should not be empty    ${actual_value}
    should be equal    ${actual_value}  ${expected_value}