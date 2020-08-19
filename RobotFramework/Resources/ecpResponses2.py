responses = [
    {
        "SEVERITY_ENUMERATION": [
            "SEV_RETRY",
            "SEV_GIVEUP"
        ]
    },
    {
        "SRC_CLIENT (error probably caused by the client)": [
            {
                "UNIT_HTTP (error on HTTP request level)": [
                    "INVALID REQUEST",
                    "ECP MESSAGE SIZE LIMIT EXCEEDED",
                    "UNSUPPORTED CONTENT TYPE",
                    "CANNOT PARSE MULTIPART HTTP MESSAGE",
                    "ECP NOT FOUND IN MULTIPART HTTP MESSAGE"
                ]
            },
            {
                "UNIT_XML (error on XML level)": [
                    "INVALID STRUCTURE"
                ]
            },
            {
                "UNIT_ECP (error on ECP level)": [
                    "INVALID ECP MESSAGE",
                    "UNKNOWN DOMAIN",
                    "UNKNOWN COMMAND",
                    "INVALID ECP COMMAND",
                    "INVALID CDATA IN COMMAND"
                ]
            },
            {
                "UNIT_DATA (invalid or incomplete data received)": [
                    "MISSING IDENTIFICATION",
                    "MISSING RESOURCE",
                    "INVALID IDENTIFICATION"
                ]
            }
        ]
    },

    {
        "SRC_SERVER (error caused by the server)": [
            {
                "UNIT_CONFIG (server configuration error)": [
                    "SERVICE NOT CONFIGURED",
                    "VALIDATION SCHEMA NOT FOUND",
                    "DATABASE CONNECTION NOT CONFIGURED",
                    "INVALID VALIDATION SCHEMA",
                    "COMMAND NOT CONFIGURED"
                ]
            },
            {
                "UNIT_DB (database problem)": [
                    "CANNOT CONNECT TO DB"
                ]
            },
            "UNIT_INTERNAL (other kind of server error)",
            {
                "UNIT_QOS (QoS related error)": [
                    "QOS REJECT (request was rejected by QoS)"
                ]
            }
        ]
    },
    {
        "SRC_DB (error occurred during the use of database)": [
            "UNIT_STORED_PROCEDURE (stored procedure problem)",
            {
                "UNIT_RESULT_SET (database result usage problem)": [
                    "BAD NUMBER OF COLUMNS",
                ]
            },
            "UNIT_INTERNAL (other kind of server error)"
        ]
    },
    {
        "SRC_WS (error occurred during the use of web service)": [
            {
                "UNIT_NETWORK (network problem while calling EDF web service)": [
                    "CANNOT CONNECT TO WEB SERVICE"
                ]
            },
            "UNIT_HTTP (EDF server returned HTTP response code other than 200)",
            {
                "UNIT_RESPONSE (cannot use/parse EDF web service response)": [
                    "INVALID RESPONSE",
                    "INVALID CDATA IN RESPONSE"
                ]
            }
        ]
    },
    {
        "SRC_EDF (error occurred on the EDF side, but may be caused by invalid client’s input data)": [
            "UNIT_WEBLOGIN_AUTHENTICATION",
            {
                "UNIT_WEBLOGIN_ASSOCIATION": [
                    "NONUNIQUE_COMPUTER_NAME"
                ]
            },
            "UNIT_UPLOAD_CONFIGURATION_AUDIT",
            {
                "UNIT_GET_CONFIGURATION": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED"
                ]
            },
            "UNIT_GET_ON_DEMAND_ACTIONS",
            "UNIT_UPDATE_ON_DEMAND_ACTIONS_STATE",
            "UNIT_REPORT_SUSPICION",
            "UNIT_SEND_NETWORK_SNAPSHOT_INTERFACE",
            "UNIT_SEND_NETWORK_SNAPSHOT_WIFI",
            "UNIT_SEND_NETWORK_SNAPSHOT_TRACEROUTE",
            "UNIT_SEND_DESKTOP_SNAPSHOT",
            "UNIT_SEND_WEBCAM_SNAPSHOT",
            "UNIT_UPDATE_PRODUCT_DATA",
            {
                "UNIT_GET_ATTACHMENT": [
                    "ATTACHMENT_NOT_FOUND"
                ]
            },
            "UNIT_WEBLOGIN_DISSOCIATION",
            "UNIT_SEND_VARIABLE_DATA",
            "UNIT_ AUTHENTICATION",
            {
                "UNIT_ASSOCIATION": [
                    "NONUNIQUE_SEAT_NAME",
                    "ACCOUNT_MISMATCH",
                    "AUTHENTICATION_TYPE_MISMATCH",
                    "UNCONFIRMED_SEAT",
                    "INVALID_CREDENTIALS",
                    "TOKEN_NOT_FOUND",
                    "TOKEN_NOT_AUTHORIZED",
                    "INVALID_LICENSE",
                    "INVALID_COMPUTER_NAME",
                    "INVALID_LANGUAGE_CODE",
                    "SEAT_LOCKED"
                ]
            },
            {
                "UNIT_CONFIRM_ASSOCIATION": [
                    "NONUNIQUE_SEAT_NAME",
                    "INVALID_COMPUTER_NAME"
                ]
            },
            {
                "UNIT_CREATE_ACCOUNT": [
                    "NONUNIQUE_USERNAME",
                    "INVALID_USERNAME"
                ]
            },
            {
                "UNIT_ACTIVATION": [
                    "INVALID_LICENSEKEY",
                    "EXPIRED_LICENSE",
                    "INVALID_LICENSE",
                    "INVALID_CREDENTIALS",
                    "TOKEN_NOT_FOUND",
                    "TOKEN_NOT_AUTHORIZED",
                    "SEAT_IS_ALREADY_ACTIVATED",
                    "SEAT_NOT_ASSOCIATED",
                    "ACCOUNT_NOT_FOUND",
                    "INVALID_ACCOUNT_ASSOCIATION",
                    "EMAIL_ALREADY_REGISTERED",
                    "CANCELLED_LICENSE",
                    "RENEWAL_LICENSEKEY_USED",
                    "INVALID_USERNAME_PASSWORD",
                    "LICENSEKEY_COUNTRY_MISMATCH",
                    "INVALID_ASSOC_TYPE_COMBINATION",
                    "TRIAL_CROSS_COUNTRY_MISMATCH",
                    "EMPTY_PRODUCT_LIST",
                    "TOKEN_EXPIRED",
                    "EMAIL_CONFIRMATION_FAILED",
                    "TOKEN_OVERUSED",
                    "FAILED_TO_CREATE_LICENSE",
                    "CRC_REGION_BATCH_COUNTRY_CONFLICT",
                    "CRC_REGION_REG_COUNTRY_CONFLICT",
                    "CCC_REG_COUNTRY_BATCH_COUNTRY_CONFLICT",
                    "GC_GEOIP_COUNTRY_BATCH_COUNTRY_CONFLICT",
                    "LL_APP_LANGUAGE_BATCH_LANGUAGE_CONFLICT",
                    "INVALID_DEAL",
                    "DEAL_NOT_ACTIVE",
                    "INVALID_DEVICE_ID_FOR_DEAL",
                    "ACTIVATION_NOT_ALLOWED",
                    "LSA_SEAT_QUANTITY_EXCEEDED",
                    "LICENSE_TOKEN_NOT_FOUND",
                    "CREDENTIALS_NOT_FOUND",
                    "RESYNC_FAILED",
                    "SEAT_NOT_ACTIVATED",
                    "UNIT_NOT_AVAILABLE",
                    "PWM_LICENSE_OWNER_VERIFICATION_FAILED",
                    "PWM_LICENSE_SEAT_LICENSE_MISMATCH",
                    "FREE_PRODUCT_CODE_AND_DEALCODE_ARE_REQUIRED",
                    "DEXTER_COMMUNICATION_FAILED",
                    "INCORRECT_INPUT_DATA",
                    "INCORRECT_PURCHASE_DATA",
                    "PROMOCODE_DOESNT_EXIST",
                    "PROMOCODE_NOT_SET_TO_CUSTOMER",
                    "PROMOCODE_ALREADY_USED",
                    "PROMOCODE_NOT_VALID_FOR_PRODUCT",
                    "PROMOCODE_REACHED_MAX_USERS",
                    "NO_CUSTOMER_CARD_FOUND",
                    "CAMPAIGN_NOT_VALID",
                    "CAMPAIGN_FOR_DEAL_NOT_VALID",
                    "CAMPAIGN_FOR_COUNTRY_NOT_VALID",
                    "USE_OF_OWN_PROMOCODE",
                    "POOL_EMPTY",
                    "ALL_LICENSES_EXPIRED",
                    "POOL_NOT_FOUND",
                    "LICENSE_NOT_FOUND_IN_POOL",
                    "PROMOCODE_NOT_VALID_FOR_COUNTRY",
                    "PROMOCODE_COUNTRY_PRODUCT_MISMATCH",
                    "PROMOCODE_NOT_VALID",
                    "SEAT_LOCKED"
                ]
            },
            "UNIT_REPORT_EVENT",
            "UNIT_REPORT_STATUS",
            {
                "UNIT_DISSOCIATION": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "INVALID_INPUT_DATA",
                    "INVALID_CREDENTIALS",
                    "SEAT_ACCOUNT_MISMATCH",
                    "SEAT_LOCKED"
                ]
            },
            "UNIT_SEND_GPS_SNAPSHOT",
            {
                "UNIT_GET_LICENSE_FILE": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "LICENSE_NOT_FOUND",
                    "LICENSE_FILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_UPDATE_SEAT_DATA": [
                    "LICENSE_MISSING",
                    "SEAT_NOT_FOUND",
                    "INVALID_COMPUTER_NAME",
                    "INVALID_LICENSE",
                    "INVALID_LANGUAGE_CODE"
                ]
            },
            {
                "UNIT_EDF_GET_DEPLOYMENT_TOKEN": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "TOKEN_NOT_FOUND"
                ]
            },
            {
                "UNIT_EDF_LINK_SEAT_POOLS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "ALREADY_DONE",
                    "LICENSE_IS_NOT_REGISTERED",
                    "LICENSE_NOT_FOUND",
                    "INVALID_CREDENTIALS",
                    "LICENSE_IS_NOT_MANAGEABLE",
                    "MISSING_ACCOUNT_RIGHTS",
                    "ACCOUNT_SUSPENDED",
                    "SEAT_LOCKED"
                ]
            },
            {
                "UNIT_EDF_UNLINK_SEAT_POOLS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "ALREADY_DONE"
                ]
            },
            {
                "UNIT_EDF_GET_LINKED_POOLS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED"
                ]
            },
            {
                "UNIT_GET_LEGACY_LICENSE_FILE": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "LICENSE_NOT_FOUND",
                    "LICENSE_FILE_NOT_FOUND"
                ]
            },
            "UNIT_GET_ENVIRONMENT_INFO",
            {
                "UNIT_SET_UPDATE_MIRROR": [
                    "UPDATE_EXPORT_MATRIX_FAILED"
                ]
            },
            {
                "UNIT_REPORT_HARDWARE_CHANGE": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "SEAT_NOT_ASSOCIATED"
                ]
            },
            {
                "UNIT_REPORT_UNIT_UTILIZATION": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED"
                ]
            },
            {
                "UNIT_GET_PROFILES": [
                    "SEAT_NOT_FOUND",
                    "ACCOUNT_NOT_FOUND",
                    "PROFILE_NOT_FOUND",
                    "VERSION_INFO_NOT_FOUND"
                ]
            },
            {
                "UNIT_UPDATE_PROFILE": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND",
                    "GROUP_ERROR",
                    "VERSION_INFO_NOT_FOUND",
                    "OUTDATED_PROFILE",
                    "VERSION_UPDATE_FAILED",
                    "INVALID_OPERATION",
                    "CANNOT_DELETE_PROFILE",
                    "PROFILE_ALREADY_EXIST",
                    "SEAT_LOCKED"
                ]
            },
            {
                "UNIT_SET_ACTIVE_PROFILE": [
                    "PROFILE_NOT_FOUND",
                    "SEAT_NOT_FOUND",
                    "EMPTY_PLATFORM_ID"
                ]
            },
            {
                "UNIT_GET_ACTIVE_PROFILE": [
                    "PROFILE_NOT_FOUND",
                    "SEAT_NOT_FOUND"
                ]
            },
            {
                "UNIT_GET_REQUESTED_ITEMS": [
                    "PROFILE_NOT_FOUND",
                    "SEAT_NOT_FOUND"
                ]
            },
            {
                "UNIT_SET_REQUESTED_ITEMS": [
                    "SAVE_REQUESTED_ITEM_ERROR",
                    "UPDATE_REQUESTED_ITEM_ERROR",
                    "NEW_REQUEST_UNSUPPORTED_TYPE",
                    "APP_NOT_FOUND",
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_SEND_LOGS": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            "UNIT_PAR_SEND_GPS_SNAPSHOT",
            {
                "UNIT_GET_REPORT": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            "UNIT_GENERATE_REPORT",
            "UNIT_GET_APPLICATION",
            {
                "UNIT_UPDATE_APPLICATION": [
                    "PROFILE_NOT_FOUND",
                    "SEAT_NOT_FOUND"
                ]
            },
            "UNIT_GET_APPLICATIONS_USAGE",
            {
                "UNIT_SET_APPLICATIONS_USAGE": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_REFRESH_GPS_LOCATION": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_GET_GPS_LOCATION": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_GET_CUSTOMIZATION": [
                    "PACKAGE_NOT_FOUND"
                ]
            },
            {
                "UNIT_REPORT_DEVICE_ISSUES": [
                    "PROFILE_NOT_FOUND",
                    "SEAT_NOT_FOUND",
                    "UPDATE_DEVICE_ERROR"
                ]
            },
            {
                "UNIT_UPDATE_ACCOUNT_SETTINGS": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND",
                    "PHONE_NUMBERS_UPDATE_FAILED",
                    "SETTINGS_UPDATE_FAILED"
                ]
            },
            {
                "UNIT_GET_ACCOUNT_SETTINGS": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            "UNIT_REPORT_PARENTAL_VERSION",
            {
                "UNIT_GET_COUNTRIES": [
                    "SEAT_NOT_FOUND",
                    "INVALID_CULTURE_CODE",
                    "SEAT_ASSOCIATED_WITH_INVALID_LANGUAGE"
                ]
            },
            {
                "UNIT_GET_DEVICE_ISSUES": [
                    "SEAT_NOT_FOUND",
                    "PROFILE_NOT_FOUND"
                ]
            },
            {
                "UNIT_GET_API_CREDENTIALS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "SEAT_LICENSE_NOT_FOUND",
                    "ESA_LICENSE_CREATE_FAILED"
                ]
            },
            {
                "UNIT_DEACTIVATION": [
                    "SEAT_NOT_FOUND_IN_TABLESTORAGE",
                    "SEAT_NOT_FOUND",
                    "LICENSE_NOT_FOUND"
                ]
            },
            "UNIT_REPORT_PARENTAL_EVENT",
            "UNIT_SIGN_APPLE_CSR",
            {
                "UNIT_GET_UNIT_UTILIZATION": [
                    "SEAT_NOT_FOUND",
                    "SEAT_NOT_ACTIVATED"
                ]
            },
            {
                "UNT_GET_TOKEN_RELATED_DATA": [
                    "CANNOT CONNECT TO LI SERVICE",
                    "INVALID RESPONSE FROM LI SERVICE",
                    "UNKNOWN TOKEN FROM LI SERVICE",
                    "INVALID/EXPIRE INSTALLER FROM LI SERVICE"
                ]
            },
            "UNT_IPM_GET_CONFIGURATION",
            {
                "UNT_IPM_GET_MESSAGE": [
                    "INVALID_LICENSE_PARAMS"
                ]
            },
            "UNT_IPM_GET_ATTACHMENT",
            {
                "UNIT_DOWNLOAD_APPLICATION_POLICY": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "APPSETTING_NOT_FOUND",
                    "APPSETTING_UPDATE_FAIL",
                    "ACCOUNT_MISMATCH",
                    "BLOB_DOWNLOAD_FAIL"
                ]
            },
            {
                "UNIT_UPLOAD_APPLICATION_SETTINGS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED",
                    "APPSETTING_NOT_FOUND",
                    "APPSETTING_UPDATE_FAIL",
                    "ACCOUNT_MISMATCH",
                    "BLOB_UPLOAD_FAIL"
                ]
            },
            "UNIT_GET_LICENSE_DETAILS",
            "UNIT_CONVERT_UP_TO_LK",
            "UNIT_GET_APPLICATION_ACTIVATION_MATRIX",
            "UNIT_GET_SEAT_DATA",
            {
                "UNIT_GET_PROMO_CODES": [
                    "SEAT_NOT_FOUND",
                    "LICENSE_NOT_FOUND",
                    "DX_COMMUNICATION_ERROR",
                    "PROMOCODE_ALREADY_USED"
                ]
            },
            {
                "UNIT_GET_LICENSES": [
                    "INVALID_CREDENTIALS",
                    "EMPTY_PRODUCT_LIST",
                    "INVALID_APPLICATION"
                ]
            },
            "UNIT_GET_ENCRYPTION_SERIAL_NUMBER",
            "UNIT_GET_API_TOKENS",
            "UNIT_CHECK_API_TOKEN",
            {
                "UNIT_SEND_SETTINGS_UNLOCK_CODE": [
                    "WRONG_CREDENTIALS",
                    "WRONG_EMAIL_ADDRESS",
                    "SEAT_NOT_FOUND",
                    "LICENSE_NOT_FOUND",
                    "INVALID_UNLOCK_CODE"
                ]
            },
            {
                "ANTITHEFT_ASSOCIATION": [
                    "NONUNIQUE_COMPUTER_NAME",
                    "INVALID_CREDENTIALS",
                    "SEAT_NOT_FOUND",
                    "SEAT_NOT_CONFIRMED",
                    "LOGIN_NOT_FOUND"
                ]
            },
            {
                "UNIT_SET_PROMO_CODE": [
                    "SEAT_NOT_FOUND",
                    "LICENSE_NOT_FOUND",
                    "DX_COMMUNICATION_ERROR",
                    "PROMOCODE_ALREADY_USED"
                ]
            },
            "UNIT_REQUEST_DEVICE_REAL_TIME_INFO",
            {
                "UNIT_GET_DEVICE_REAL_TIME_INFO": [
                    "NOT_FOUND"
                ]
            },
            "UNIT_SET_DEVICE_REAL_TIME_INFO",
            {
                "UNIT_GET_LINKED_LOCATIONS": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED"
                ]
            },
            {
                "UNIT_REGISTER_NETWORK_DEVICE": [
                    "SEAT_NOT_FOUND",
                    "FINGERPRINT_NOT_FOUND"
                ]
            },
            {
                "UNIT_GET_NETWORK_FINGERPRINT": [
                    "MANDATORY_FIELDS_MISSING"
                ]
            },
            {
                "UNIT_DNS_EDF_REQUEST": [
                    "MESSAGE_ALREADY_PROCESSED"
                ]
            },
            {
                "UNIT_GET_ASSOCIATED_ACCOUNT": [
                    "SEAT_NOT_FOUND",
                    "SEAT_DELETED"
                ]
            },
            {
                "UNIT_REPORT_SEAT_TOKEN": [
                    "SEAT_NOT_FOUND"
                ]
            },
            {
                "UNIT_IDENTIFY_HARDWARE": [
                    "SERVICE_DISABLED"
                ]
            },
            {
                "UNIT_REPORT_HARDWARE_IDENTITY_CRISIS": [
                    "SERVICE_DISABLED"
                ]
            },
            {
                "UNIT_REPORT_HARDWARE_IDENTITY_COLLISION": [
                    "SERVICE_DISABLED"
                ]
            },
            {
                "UNIT_DISCONNECT_SEAT_TOKEN": [
                    "SEAT_NOT_FOUND"
                ]
            },
            {
                "UNIT_EDTD_GET_PERMISSIONS": [
                    "LIB_NOT_FOUND"
                ]
            },
            {
                "UNIT_MANAGE_LICENSE": [
                    "LICENSE_NOT_FOUND",
                    "LICENSE_ALREADY_MANAGED",
                    "LICENSE_NOT_SUITABLE",
                    "LICENSE_IS_CANCELLED",
                    "LICENSE_NOT_REGISTERED",
                    "LICENSE_EXPIRED"
                ]
            },
            "UNIT_PWM_GET_MIGRATION_STATUS"
        ]
    },

    {
        "SRC_3RD (error occurred on the 3rd party side, but may be caused by invalid client’s input data)": [
            {
                "UNIT_ESA_ACTIVATION": [
                    "VERSION_NOT_SUPPORTED",
                    "LICENSE_INVALID",
                    "LICENSE_ALREADY_ACTIVATED"
                ]
            }
        ]
    }
]
