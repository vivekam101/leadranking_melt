import json

# *
# * LEAD RANKING *
# *

def _map_lead_ranking_data(data):
    _mapping = {
        "_id": "Id",
        "LeadSource": "LeadSource__c",
        "Mobile": "MobilePhone",
        "ProgramType__Program": "ProgramType__c",
        "Telephone": "Phone",
        "donotemail": "DoNotEmail__c",
        "donotfax": "DoNotFax__c",
        "donotphone": "DoNotPhone__c",
        "po_prefered_start_date1": "PreferredStartDate__c"
        #        "LeadCategory":"LeadCategory__c",
        #        "LeadSubCategory":"LeadSubcategory__c"
    }
    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    _out["LeadCategory"] = data.get("LeadCategory__r", {}).get("Name")
    _out["LeadSubCategory"] = data.get("LeadSubcategory__r", {}).get("Name")

    return _out

LEAD_RANKING_API_CONFIG = {
    "data_map":_map_lead_ranking_data,
    "model_dump_file_path":"model_dumps/leadranking_rf.pkl",
    "true_status":1,
    "category_cols":{"LeadCategory":['affiliate', 'aggregate', 'email/social/alum', 'field', 'media',
      'other', 'partner', 'search', 'website'],\
            "LeadSubCategory": ['alumni referral', 'ambassador referral', 'application', 'banner',
      'classesusa', 'climb credit', 'conference', 'cpl', 'display',
      'district program', 'ec referral', 'house', 'nise', 'organic',
      'other', 'outdoor', 'ppc', 'purchased', 'radio', 'referral',
      'request', 'social', 'treasures 4 teachers', 'tv', 'web video',
      'webinar'],\
             "LeadSource":['affiliate', 'aggregate', 'district program', 'email/social/alum',
      'field', 'media', 'other', 'partner', 'search', 'website']},
}


# *
# * LEAD RANKING ENDS HERE *
# *

# *
# * MELT *
# *

def _map_melt_data(data):
    _mapping = {
        "_id": "Id",
        # "batch_code": "BatchCode__c",
        # "mentor": "Mentor__c",
        # "experience_level":"Experience__c",
        #        "LeadCategory":"LeadCategory__c",
        #        "LeadSubCategory":"LeadSubcategory__c"
    }
    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    _out["batch_code"] = data.get("Engagements__r", {}).get("records")[0].get("BatchCode__c")
    _out["mentor"] = data.get("Entrollments__r", {}).get("records")[0].get("Mentor__c")
    _out["experience_level"] = data.get("Engagements__r", {}).get("records")[0].get("Experience__c")
    # print(_out)
    return _out

MELT_API_CONFIG = {
    "data_map":_map_melt_data,
    "model_dump_file_path":"model_dumps/Melt.pkl",
    "true_status":1,
    "category_cols":{"experience_level":['beginner', 'expert', 'intermediate'],\
            "batch_code": ['1','2','3','4','5','6','7','8','9','10'],\
             "mentor":['byron barton', 'cathy mckay', 'crystal neumann', 'debbie beck',
      'other', 'tiffany hamlett']},
}


# *
# * MELT ENDS HERE *
# *

# *
# * LEAD CONVERSION *
# *

def _map_lead_conversion_rate(data):
    _mapping ={
            '_id':'Id',
            '_no_of_visits':'Visits__c',
            '_page_views':'Page_Views__c',
            '_submissions':'Submissions__c',
             'annual_revenue':'Annual_Revenue_in_USD__c',
             'annual_sales_volume':'Annual_Sales_Volume__c',
             '_no_of_rejects':'No_of_rejected_items__c',
             'lead_category':'LeadCategory__c',
             'lead_source':'Lead_Source__c'
    }
    _out = {}
    for _key in _mapping.keys():
        _out[_key] = data.get(_mapping[_key])

    return _out

LEAD_CONVERSION_API_CONFIG = {
    "data_map":_map_lead_conversion_rate,
    "model_dump_file_path":"model_dumps/decision_tree.pkl",
    "true_status":"Y",
    "category_cols":{"lead_category":['Affiliate', 'Aggregate', 'Field'],\
            "lead_source":['Data.com', 'ESamples', 'Other', 'SOPS', 'Trade Shows', 'Web']},
}

# *
# * LEAD CONVERSION ENDS HERE *
# *

