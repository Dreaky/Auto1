responses = {
    0: {
        "SEVERITY_ENUMERATION": {
            1: "SEV_RETRY",
            2: "SEV_GIVEUP"
        }
    },
    1: {
        "SRC_CLIENT (error probably caused by the client)": {
            1: {
                "UNIT_HTTP (error on HTTP request level)": {
                    1: "INVALID REQUEST",
                    2: "ECP MESSAGE SIZE LIMIT EXCEEDED",
                    3: "UNSUPPORTED CONTENT TYPE",
                    4: "CANNOT PARSE MULTIPART HTTP MESSAGE",
                    5: "ECP NOT FOUND IN MULTIPART HTTP MESSAGE"
                }
            },
            2: {
                "UNIT_XML (error on XML level)": {
                    1: "INVALID STRUCTURE"
                }
            },
            3: {
                "UNIT_ECP (error on ECP level)": {
                    1: "INVALID ECP MESSAGE",
                    2: "UNKNOWN DOMAIN",
                    3: "UNKNOWN COMMAND",
                    4: "INVALID ECP COMMAND",
                    5: "INVALID CDATA IN COMMAND"
                }
            },
            4: {
                "UNIT_DATA (invalid or incomplete data received)": {
                    1: "MISSING IDENTIFICATION",
                    2: "MISSING RESOURCE",
                    3: "INVALID IDENTIFICATION"
                }
            }
        }
    },
    2: {
        "SRC_SERVER (error caused by the server)": {
            1: {
                "UNIT_CONFIG (server configuration error)": {
                    1: "SERVICE NOT CONFIGURED",
                    2: "VALIDATION SCHEMA NOT FOUND",
                    3: "DATABASE CONNECTION NOT CONFIGURED",
                    4: "INVALID VALIDATION SCHEMA",
                    5: "COMMAND NOT CONFIGURED"
                }
            },
            2: {
                "UNIT_DB (database problem)": {
                    1: "CANNOT CONNECT TO DB"
                }
            },
            3: "UNIT_INTERNAL (other kind of server error)",
            4: {
                "UNIT_QOS (QoS related error)": {
                    1: "QOS REJECT (request was rejected by QoS)"
                }
            }
        }
    },
    3: {
        "SRC_DB (error occurred during the use of database)": {
            1: "UNIT_STORED_PROCEDURE (stored procedure problem)",
            2: {
                "UNIT_RESULT_SET (database result usage problem)": {
                    1: "BAD NUMBER OF COLUMNS",
                }
            },
            3: "UNIT_INTERNAL (other kind of server error)"
        }
    },
    4: {
        "SRC_WS (error occurred during the use of web service)": {
            1: {
                "UNIT_NETWORK (network problem while calling EDF web service)": {
                    1: "CANNOT CONNECT TO WEB SERVICE"
                }
            },
            2: "UNIT_HTTP (EDF server returned HTTP response code other than 200)",
            3: {
                "UNIT_RESPONSE (cannot use/parse EDF web service response)": {
                    1: "INVALID RESPONSE",
                    2: "INVALID CDATA IN RESPONSE"
                }
            }
        }
    },
    5: {
        "SRC_EDF (error occurred on the EDF side, but may be caused by invalid client’s input data)": {
            1: "UNIT_WEBLOGIN_AUTHENTICATION",
            2: {
                "UNIT_WEBLOGIN_ASSOCIATION": {
                    1: "NONUNIQUE_COMPUTER_NAME"
                }
            },
            3: "UNIT_UPLOAD_CONFIGURATION_AUDIT",
            4: {
                "UNIT_GET_CONFIGURATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED"
                }
            },
            5: "UNIT_GET_ON_DEMAND_ACTIONS",
            6: "UNIT_UPDATE_ON_DEMAND_ACTIONS_STATE",
            7: "UNIT_REPORT_SUSPICION",
            8: "UNIT_SEND_NETWORK_SNAPSHOT_INTERFACE",
            9: "UNIT_SEND_NETWORK_SNAPSHOT_WIFI",
            10: "UNIT_SEND_NETWORK_SNAPSHOT_TRACEROUTE",
            11: "UNIT_SEND_DESKTOP_SNAPSHOT",
            12: "UNIT_SEND_WEBCAM_SNAPSHOT",
            13: "UNIT_UPDATE_PRODUCT_DATA",
            14: {
                "UNIT_GET_ATTACHMENT": {
                    1: "ATTACHMENT_NOT_FOUND"
                }
            },
            15: "UNIT_WEBLOGIN_DISSOCIATION",
            16: "UNIT_SEND_VARIABLE_DATA",
            17: "UNIT_ AUTHENTICATION",
            18: {
                "UNIT_ASSOCIATION": {
                    1: "NONUNIQUE_SEAT_NAME",
                    2: "ACCOUNT_MISMATCH",
                    3: "AUTHENTICATION_TYPE_MISMATCH",
                    4: "UNCONFIRMED_SEAT",
                    5: "INVALID_CREDENTIALS",
                    6: "TOKEN_NOT_FOUND",
                    7: "TOKEN_NOT_AUTHORIZED",
                    8: "INVALID_LICENSE",
                    9: "INVALID_COMPUTER_NAME",
                    10: "INVALID_LANGUAGE_CODE",
                    999: "SEAT_LOCKED"
                }
            },
            19: {
                "UNIT_CONFIRM_ASSOCIATION": {
                    1: "NONUNIQUE_SEAT_NAME",
                    2: "INVALID_COMPUTER_NAME"
                }
            },
            20: {
                "UNIT_CREATE_ACCOUNT": {
                    1: "NONUNIQUE_USERNAME",
                    2: "INVALID_USERNAME"
                }
            },
            21: {
                "UNIT_ACTIVATION": {
                    1: "INVALID_LICENSEKEY",
                    2: "EXPIRED_LICENSE",
                    3: "INVALID_LICENSE",
                    4: "INVALID_CREDENTIALS",
                    5: "TOKEN_NOT_FOUND",
                    6: "TOKEN_NOT_AUTHORIZED",
                    7: "SEAT_IS_ALREADY_ACTIVATED",
                    8: "SEAT_NOT_ASSOCIATED",
                    9: "ACCOUNT_NOT_FOUND",
                    10: "INVALID_ACCOUNT_ASSOCIATION",
                    11: "EMAIL_ALREADY_REGISTERED",
                    12: "CANCELLED_LICENSE",
                    13: "RENEWAL_LICENSEKEY_USED",
                    14: "INVALID_USERNAME_PASSWORD",
                    15: "LICENSEKEY_COUNTRY_MISMATCH",
                    16: "INVALID_ASSOC_TYPE_COMBINATION",
                    17: "TRIAL_CROSS_COUNTRY_MISMATCH",
                    18: "EMPTY_PRODUCT_LIST",
                    19: "TOKEN_EXPIRED",
                    20: "EMAIL_CONFIRMATION_FAILED",
                    21: "TOKEN_OVERUSED",
                    22: "FAILED_TO_CREATE_LICENSE",
                    23: "CRC_REGION_BATCH_COUNTRY_CONFLICT",
                    24: "CRC_REGION_REG_COUNTRY_CONFLICT",
                    25: "CCC_REG_COUNTRY_BATCH_COUNTRY_CONFLICT",
                    26: "GC_GEOIP_COUNTRY_BATCH_COUNTRY_CONFLICT",
                    27: "LL_APP_LANGUAGE_BATCH_LANGUAGE_CONFLICT",
                    28: "INVALID_DEAL",
                    29: "DEAL_NOT_ACTIVE",
                    30: "INVALID_DEVICE_ID_FOR_DEAL",
                    31: "ACTIVATION_NOT_ALLOWED",
                    32: "LSA_SEAT_QUANTITY_EXCEEDED",
                    33: "LICENSE_TOKEN_NOT_FOUND",
                    34: "CREDENTIALS_NOT_FOUND",
                    35: "RESYNC_FAILED",
                    36: "SEAT_NOT_ACTIVATED",
                    37: "UNIT_NOT_AVAILABLE",
                    38: "PWM_LICENSE_OWNER_VERIFICATION_FAILED",
                    39: "PWM_LICENSE_SEAT_LICENSE_MISMATCH",
                    40: "FREE_PRODUCT_CODE_AND_DEALCODE_ARE_REQUIRED",
                    41: "DEXTER_COMMUNICATION_FAILED",
                    42: "INCORRECT_INPUT_DATA",
                    43: "INCORRECT_PURCHASE_DATA",
                    44: "PROMOCODE_DOESNT_EXIST",
                    45: "PROMOCODE_NOT_SET_TO_CUSTOMER",
                    46: "PROMOCODE_ALREADY_USED",
                    47: "PROMOCODE_NOT_VALID_FOR_PRODUCT",
                    48: "PROMOCODE_REACHED_MAX_USERS",
                    49: "NO_CUSTOMER_CARD_FOUND",
                    50: "CAMPAIGN_NOT_VALID",
                    51: "CAMPAIGN_FOR_DEAL_NOT_VALID",
                    52: "CAMPAIGN_FOR_COUNTRY_NOT_VALID",
                    53: "USE_OF_OWN_PROMOCODE",
                    54: "POOL_EMPTY",
                    55: "ALL_LICENSES_EXPIRED",
                    56: "POOL_NOT_FOUND",
                    57: "LICENSE_NOT_FOUND_IN_POOL",
                    58: "PROMOCODE_NOT_VALID_FOR_COUNTRY",
                    59: "PROMOCODE_COUNTRY_PRODUCT_MISMATCH",
                    60: "PROMOCODE_NOT_VALID",
                    999: "SEAT_LOCKED"
                }
            },
            22: "UNIT_REPORT_EVENT",
            23: "UNIT_REPORT_STATUS",
            24: {
                "UNIT_DISSOCIATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "INVALID_INPUT_DATA",
                    4: "INVALID_CREDENTIALS",
                    5: "SEAT_ACCOUNT_MISMATCH",
                    999: "SEAT_LOCKED"
                }
            },
            25: "UNIT_SEND_GPS_SNAPSHOT",
            26: {
                "UNIT_GET_LICENSE_FILE": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "LICENSE_NOT_FOUND",
                    4: "LICENSE_FILE_NOT_FOUND"
                }
            },
            27: {
                "UNIT_UPDATE_SEAT_DATA": {
                    1: "LICENSE_MISSING",
                    2: "SEAT_NOT_FOUND",
                    3: "INVALID_COMPUTER_NAME",
                    4: "INVALID_LICENSE",
                    5: "INVALID_LANGUAGE_CODE"
                }
            },
            28: {
                "UNIT_EDF_GET_DEPLOYMENT_TOKEN": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "TOKEN_NOT_FOUND"
                }
            },
            29: {
                "UNIT_EDF_LINK_SEAT_POOLS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "ALREADY_DONE",
                    4: "LICENSE_IS_NOT_REGISTERED",
                    5: "LICENSE_NOT_FOUND",
                    6: "INVALID_CREDENTIALS",
                    7: "LICENSE_IS_NOT_MANAGEABLE",
                    8: "MISSING_ACCOUNT_RIGHTS",
                    9: "ACCOUNT_SUSPENDED",
                    999: "SEAT_LOCKED"
                }
            },
            30: {
                "UNIT_EDF_UNLINK_SEAT_POOLS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "ALREADY_DONE"
                }
            },
            31: {
                "UNIT_EDF_GET_LINKED_POOLS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED"
                }
            },
            32: {
                "UNIT_GET_LEGACY_LICENSE_FILE": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "LICENSE_NOT_FOUND",
                    4: "LICENSE_FILE_NOT_FOUND"
                }
            },
            33: "UNIT_GET_ENVIRONMENT_INFO",
            34: {
                "UNIT_SET_UPDATE_MIRROR": {
                    1: "UPDATE_EXPORT_MATRIX_FAILED"
                }
            },
            35: {
                "UNIT_REPORT_HARDWARE_CHANGE": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "SEAT_NOT_ASSOCIATED"
                }
            },
            36: {
                "UNIT_REPORT_UNIT_UTILIZATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED"
                }
            },
            37: {
                "UNIT_GET_PROFILES": {
                    1: "SEAT_NOT_FOUND",
                    2: "ACCOUNT_NOT_FOUND",
                    3: "PROFILE_NOT_FOUND",
                    4: "VERSION_INFO_NOT_FOUND"
                }
            },
            38: {
                "UNIT_UPDATE_PROFILE": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                    3: "GROUP_ERROR",
                    4: "VERSION_INFO_NOT_FOUND",
                    5: "OUTDATED_PROFILE",
                    6: "VERSION_UPDATE_FAILED",
                    7: "INVALID_OPERATION",
                    8: "CANNOT_DELETE_PROFILE",
                    9: "PROFILE_ALREADY_EXIST",
                    999: "SEAT_LOCKED"
                }
            },
            39: {
                "UNIT_SET_ACTIVE_PROFILE": {
                    1: "PROFILE_NOT_FOUND",
                    2: "SEAT_NOT_FOUND",
                    3: "EMPTY_PLATFORM_ID"
                }
            },
            40: {
                "UNIT_GET_ACTIVE_PROFILE": {
                    1: "PROFILE_NOT_FOUND",
                    2: "SEAT_NOT_FOUND"
                }
            },
            41: {
                "UNIT_GET_REQUESTED_ITEMS": {
                    1: "PROFILE_NOT_FOUND",
                    2: "SEAT_NOT_FOUND",
                }
            },
            42: {
                "UNIT_SET_REQUESTED_ITEMS": {
                    1: "SAVE_REQUESTED_ITEM_ERROR",
                    2: "UPDATE_REQUESTED_ITEM_ERROR",
                    3: "NEW_REQUEST_UNSUPPORTED_TYPE",
                    4: "APP_NOT_FOUND",
                    5: "SEAT_NOT_FOUND",
                    6: "PROFILE_NOT_FOUND",
                }
            },
            43: {
                "UNIT_SEND_LOGS": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            44: "UNIT_PAR_SEND_GPS_SNAPSHOT",
            45: {
                "UNIT_GET_REPORT": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            46: "UNIT_GENERATE_REPORT",
            47: "UNIT_GET_APPLICATION",
            48: {
                "UNIT_UPDATE_APPLICATION": {
                    1: "PROFILE_NOT_FOUND",
                    2: "SEAT_NOT_FOUND",
                }
            },
            49: "UNIT_GET_APPLICATIONS_USAGE",
            50: {
                "UNIT_SET_APPLICATIONS_USAGE": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            51: {
                "UNIT_REFRESH_GPS_LOCATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            52: {
                "UNIT_GET_GPS_LOCATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            53: {
                "UNIT_GET_CUSTOMIZATION": {
                    1: "PACKAGE_NOT_FOUND",
                }
            },
            54: {
                "UNIT_REPORT_DEVICE_ISSUES": {
                    1: "PROFILE_NOT_FOUND",
                    2: "SEAT_NOT_FOUND",
                    3: "UPDATE_DEVICE_ERROR",
                }
            },
            55: {
                "UNIT_UPDATE_ACCOUNT_SETTINGS": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                    3: "PHONE_NUMBERS_UPDATE_FAILED",
                    4: "SETTINGS_UPDATE_FAILED",
                }
            },
            56: {
                "UNIT_GET_ACCOUNT_SETTINGS": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            57: "UNIT_REPORT_PARENTAL_VERSION",
            58: {
                "UNIT_GET_COUNTRIES": {
                    1: "SEAT_NOT_FOUND",
                    2: "INVALID_CULTURE_CODE",
                    3: "SEAT_ASSOCIATED_WITH_INVALID_LANGUAGE",
                }
            },
            59: {
                "UNIT_GET_DEVICE_ISSUES": {
                    1: "SEAT_NOT_FOUND",
                    2: "PROFILE_NOT_FOUND",
                }
            },
            60: {
                "UNIT_GET_API_CREDENTIALS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "SEAT_LICENSE_NOT_FOUND",
                    4: "ESA_LICENSE_CREATE_FAILED",
                }
            },
            61: {
                "UNIT_DEACTIVATION": {
                    1: "SEAT_NOT_FOUND_IN_TABLESTORAGE",
                    2: "SEAT_NOT_FOUND",
                    3: "LICENSE_NOT_FOUND",
                }
            },
            62: "UNIT_REPORT_PARENTAL_EVENT",
            63: "UNIT_SIGN_APPLE_CSR",
            64: {
                "UNIT_GET_UNIT_UTILIZATION": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_NOT_ACTIVATED"
                }
            },
            65: {
                "UNT_GET_TOKEN_RELATED_DATA": {
                    1: "CANNOT CONNECT TO LI SERVICE",
                    2: "INVALID RESPONSE FROM LI SERVICE",
                    3: "UNKNOWN TOKEN FROM LI SERVICE",
                    4: "INVALID/EXPIRE INSTALLER FROM LI SERVICE"
                }
            },
            66: "UNT_IPM_GET_CONFIGURATION",
            67: {"UNT_IPM_GET_MESSAGE": {
                1: "INVALID_LICENSE_PARAMS"
            }
            },
            68: "UNT_IPM_GET_ATTACHMENT",
            69: {
                "UNIT_DOWNLOAD_APPLICATION_POLICY": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "APPSETTING_NOT_FOUND",
                    4: "APPSETTING_UPDATE_FAIL",
                    5: "ACCOUNT_MISMATCH",
                    6: "BLOB_DOWNLOAD_FAIL"
                }
            },
            70: {
                "UNIT_UPLOAD_APPLICATION_SETTINGS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED",
                    3: "APPSETTING_NOT_FOUND",
                    4: "APPSETTING_UPDATE_FAIL",
                    5: "ACCOUNT_MISMATCH",
                    6: "BLOB_UPLOAD_FAIL"
                }
            },
            71: "UNIT_GET_LICENSE_DETAILS",
            72: "UNIT_CONVERT_UP_TO_LK",
            73: "UNIT_GET_APPLICATION_ACTIVATION_MATRIX",
            74: "UNIT_GET_SEAT_DATA",
            75: {
                "UNIT_GET_PROMO_CODES": {
                    1: "SEAT_NOT_FOUND",
                    2: "LICENSE_NOT_FOUND",
                    3: "DX_COMMUNICATION_ERROR",
                    4: "PROMOCODE_ALREADY_USED"
                }
            },
            76: {
                "UNIT_GET_LICENSES": {
                    1: "INVALID_CREDENTIALS",
                    2: "EMPTY_PRODUCT_LIST",
                    3: "INVALID_APPLICATION"
                }
            },
            77: "UNIT_GET_ENCRYPTION_SERIAL_NUMBER",
            78: "UNIT_GET_API_TOKENS",
            79: "UNIT_CHECK_API_TOKEN",
            80: {
                "UNIT_SEND_SETTINGS_UNLOCK_CODE": {
                    1: "WRONG_CREDENTIALS",
                    2: "WRONG_EMAIL_ADDRESS",
                    3: "SEAT_NOT_FOUND",
                    4: "LICENSE_NOT_FOUND",
                    5: "INVALID_UNLOCK_CODE"
                }
            },
            81: {
                "ANTITHEFT_ASSOCIATION": {
                    1: "NONUNIQUE_COMPUTER_NAME",
                    2: "INVALID_CREDENTIALS",
                    3: "SEAT_NOT_FOUND",
                    4: "SEAT_NOT_CONFIRMED",
                    5: "LOGIN_NOT_FOUND"
                }
            },
            82: {
                "UNIT_SET_PROMO_CODE": {
                    1: "SEAT_NOT_FOUND",
                    2: "LICENSE_NOT_FOUND",
                    3: "DX_COMMUNICATION_ERROR",
                    4: "PROMOCODE_ALREADY_USED"
                }
            },
            83: "UNIT_REQUEST_DEVICE_REAL_TIME_INFO",
            84: {
                "UNIT_GET_DEVICE_REAL_TIME_INFO": {
                    1: "NOT_FOUND"
                }
            },
            85: "UNIT_SET_DEVICE_REAL_TIME_INFO",
            86: {
                "UNIT_GET_LINKED_LOCATIONS": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED"
                }
            },
            87: {
                "UNIT_REGISTER_NETWORK_DEVICE": {
                    1: "SEAT_NOT_FOUND",
                    2: "FINGERPRINT_NOT_FOUND"
                }
            },
            88: {
                "UNIT_GET_NETWORK_FINGERPRINT": {
                    1: "MANDATORY_FIELDS_MISSING"
                }
            },
            89: {
                "UNIT_DNS_EDF_REQUEST": {
                    1: "MESSAGE_ALREADY_PROCESSED"
                }
            },
            90: {
                "UNIT_GET_ASSOCIATED_ACCOUNT": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_DELETED"
                }
            },
            91: {
                "UNIT_REPORT_SEAT_TOKEN": {
                    1: "SEAT_NOT_FOUND"
                }
            },
            92: {
                "UNIT_IDENTIFY_HARDWARE": {
                    1: "SERVICE_DISABLED"
                }
            },
            93: {
                "UNIT_REPORT_HARDWARE_IDENTITY_CRISIS": {
                    1: "SERVICE_DISABLED"
                }
            },
            94: {
                "UNIT_REPORT_HARDWARE_IDENTITY_COLLISION": {
                    1: "SERVICE_DISABLED"
                }
            },
            95: {
                "UNIT_DISCONNECT_SEAT_TOKEN": {
                    1: "SEAT_NOT_FOUND"
                }
            },
            96: {
                "UNIT_EDTD_GET_PERMISSIONS": {
                    1: "LIB_NOT_FOUND"
                }
            },
            97: {
                "UNIT_MANAGE_LICENSE": {
                    1: "SEAT_NOT_FOUND",
                    2: "SEAT_NOT_MANAGED",
                    3: "ALREADY_MANAGED",
                    4: "NOT_SUITABLE_FOR_ACCOUNT",
                    5: "LICENSE_CANCELLED",
                    6: "LICENSE_NOT_REGISTERED",
                    7: "LICENSE_EXPIRED",
                    8: "LICENSE_NOT_FOUND",
                    9: "OWNER_UNVERIFIABLE"
                }
            },
            98: "UNIT_PWM_GET_MIGRATION_STATUS"
        }
    },
    6: {
        "SRC_3RD (error occurred on the 3rd party side, but may be caused by invalid client’s input data)": {
            1: {
                "UNIT_ESA_ACTIVATION": {
                    1: "VERSION_NOT_SUPPORTED",
                    2: "LICENSE_INVALID",
                    3: "LICENSE_ALREADY_ACTIVATED"
                }
            }
        }
    }
}