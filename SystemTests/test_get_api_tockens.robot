*** Settings ***
Library  simpleRequests.py
Library  helpers.py
Library  ecpClient.py
Variables  variables.py

*** Variables ***
${cs_url}    ${CS_TEST}
${seat_id}    5b3131fd-d50f-4ece-9f6f-3ba3ea9a7ce1

*** Test Cases ***
Get API Tokens
     Given XML tree is loaded from ${CS_PAYLOAD_PATH}/getApiTokens.xml and stored to tokens_xml
       And A tag seatid value in ${tokens_xml} is set to ${seat_id}
      When ECP call to ${cs_url} with body ${tokens_xml} is successful
      Then Value of XML ${latestXmlTree} tag status should be VALID

*** Keywords ***
Value of XML ${elementree} tag ${tag} should be ${expected_value}
    Value of tag ${tag} from ${elementree} is stored into actual_value
    should be equal    ${actual_value}  ${expected_value}