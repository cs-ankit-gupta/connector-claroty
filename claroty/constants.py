""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

ASSET_TYPE = {
    "Endpoint": "eEndpoint",
    "Engineering Station": "eEngineeringStation",
    "Networking": "eNetworking",
    "OT": "eOT",
    "PLC": "ePLC"
}

CRITICALITY_EXACT = {"High": "eHigh", "Medium": "eMedium", "Low": "eLow"}

STATUS_CATEGORY = {
    "Resolved": "1",
    "Unresolved": "0",
    "Security": "1",
    "Integrity": "0"
}
FORMAT = {
    "Asset List": "asset_list",
    "Insight Assets": "insight_assets",
    "Resource IDs": "rids"
}
SEVERITY = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Critical": 4
}
ALERT_SEVERITY = {
    "Low": 0,
    "Medium": 1,
    "High": 2,
    "Critical": 3
}

EVENT_STATUS = {
    "OT Alert": "eOtAlert",
    "OT Operation": "eOtOperation",
    "Alert": "eAlert",
    "Not Risky Change": "eNotRisky"
}
TYPE_DICT = {
    "0 - eNewAsset": "0",
    "1 - eAssetConflict": "1",
    "2 - eBaselineDeviation": "2",
    "3 - eThreat": "3",
    "4 - eAssetInformationChange": "4",
    "5 - eProtocolSpecific": "5",
    "6 - eBaselineDown": "6",
    "8 - eBaselineVolumeDeviationHigh": "8",
    "9 - eBaselineVolumeDeviationLow": "9",
    "10 - eFTPData": "10",
    "11 - eBaselineRule": "11",
    "12 - eHighArpActivity": "12",
    "13 - eKnownThreatEvent": "13",
    "14 - eFalseMac": "14",
    "15 - eSuspiciousFileTransfer": "15",
    "16 - ePolicyViolation": "16",
    "17 - ePolicyRuleMatch": "17",
    "18 - eHostScan": "18",
    "19 - ePortScan": "19",
    "20 - eDenialOfService": "20"
}
