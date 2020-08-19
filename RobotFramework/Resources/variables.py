DEV_DB_HOST = "ca3w4w795x.database.windows.net"
DEV_DB_PASS = "45#hds857Tr3!"
DEV_DB_PORT = "1433"
DEV_DB_USER = "EDF.Administrator@ca3w4w795x"


HEADERS_JSON = {"Content-Type": "application/json"}

# SFPW API VARS
SFPW_API_SYNC_DEV = "https://acs-edfdev-sfpapi.azurewebsites.net/user/syncuser"

# SFPW_API_WORKER_SUCCESS= {"success": True}
SFPW_API_WORKER_FAIL= {"success": True}
SFPW_API_WORKER_SUCCESS= {"success": True, "runtimeExceptions": None, "hasRuntimeExceptions": False, "logicExceptions": None, "hasLogicExceptions": False, "intentionalDelay": None}

add_user_sql = "INSERT INTO [framework].[user] (Identification, CreatedOn, ModifiedOn, LicenseType, LicenseId, ExpirationDate, UserId, Status, IsLegacyUser) VALUES ('test.automation@protonmail.com', '2018-09-11 20:01:33.6384935', '2019-09-10 20:01:33.6384935', 1, '114478', '2021-09-13 20:01:33.6384935', 'c15d2c9c-7422-45d7-b7b3-7a1575bf5e29', 1, 1)"


# GES API VARS
GES_MEC_API_TEST = "https://acs-edftest-ges-app-main.azurewebsites.net/ges"

GES_API_REQEST_BODY = {
    'accountinfo_valid': '"mec.automation@protonmail.com"',
    'accountinfo_invalid': '"invalid.email.format"',
    'accountinfo_non_existing': '"mec.automation.not.existing@protonmail.com"',
    'productinfo_valid': '["124", "140"]',
    'productinfo_invalid': "invalid_string_request",
    'licenseinfo_valid': '"333-DPF-7RU"',
    'licenseinfo_invalid': '"00-0-000-0-00"',
    # Todo - Add scenario with non - associated lic  (note: to story add update specification)
    'associate_suspended_pcp': '{"PublicLicenseId": "333-DPF-7RU", "EmailAddress": "mec.automation@protonmail.com"}',
    'associate_valid_essp': '{"PublicLicenseId": "333-DPF-7S7", "EmailAddress": "mec.automation.1@protonmail.com"}',
    'associate_valid_essp_return': '{"PublicLicenseId": "333-DPF-7S7", "EmailAddress": "mec.automation@protonmail.com"}',
    'associate_invalid_license': '{"PublicLicenseId": "aaaa", "EmailAddress": "mec.automation@protonmail.com"}',
    'associate_invalid_email': '{"PublicLicenseId": "333-DPF-7UN", "EmailAddress": "invalid.email.com"}',
    'associate_email_non_existing': '{"PublicLicenseId": "333-DPF-7UN", "EmailAddress": "mec.automation.not.existing@protonmail.com"}'
}

EXPECTED_GES_API_RESP =  {
    'accountinfo_valid': 'myESET',
    'accountinfo_invalid': None,
    'accountinfo_non_existing': None,
    'productinfo_valid': [{'ProductCode':'124','AccountType':'myESET'}, {'ProductCode':'140','AccountType':'myESET'}],
    'productinfo_invalid': None,
    'licenseinfo_valid': {'Email': 'mec.automation@protonmail.com', 'AccountType': 'myESET', 'Verified': True},
    'licenseinfo_invalid': None,
    'associate_suspended_pcp': {"Token": None, "LicenseVerified": "NOTVERIFIED"},
    'associate_valid_essp': {"Token": None, "LicenseVerified": "NOTVERIFIED"},
    'associate_valid_essp_return': {"Token": None, "LicenseVerified": "NOTVERIFIED"},
    'associate_invalid_license': None,
    'associate_invalid_email': None,
    'associate_email_non_existing': None
}

# CS Vars
CS_PROD = 'https://edf.eset.systems/edf'
CS_DEV = 'https://edf.dev.eset.systems/edf'
CS_TEST = 'https://edf.test.eset.systems/edf'
HEADERS_TEXT_XML = {"Content-Type": "text/xml"}
CS_PAYLOAD_PATH = './SystemTests/payloads'