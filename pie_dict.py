#!/usr/bin/env python
# coding: utf-8

def pie (df):
    df.type = df.type.replace(dict.fromkeys(['Banquet Facility', 'Bar/Tavern/Brewery','Caterer',
       'Casino','Restaurant - Buffet', 'Grocery Store','Nightclub',
       'Restaurant - Fast Food', 'Restaurant - Other',
        'Restaurant - Sit Down','Retailer','Specialty Food Retailer'], 'Resturant/Retail'))
    df.type = df.type.replace(dict.fromkeys(['Healthcare - Acute Care Hospital',
       'Healthcare - Alcohol/Drug Abuse Treatment (inpatient)',
       'Healthcare - Ambulatory Surgery Center','Healthcare - Assisted Living', 
       'Healthcare - Combined Care',
        'Healthcare - Alcohol/Drug Abuse Treatment (outpatient)',
       'Healthcare - Facility for Developmentally Disabled (inpatient)',
       'Healthcare - Facility for Developmentally Disabled (outpatient)',
       'Healthcare - Group Home', 'Healthcare - Hospice','Healthcare - Independent Living Facility',
       'Healthcare - Memory Care', 'Healthcare - Outpatient',
       'Healthcare - Psychiatric Hospital', 'Healthcare - Rehab Facility',
       'Healthcare - Skilled Nursing',
       'Healthcare - Long-term Acute Care'], 'Healthcare'))

    df.type = df.type.replace(dict.fromkeys([ 'Adult Sports Club/Team','Agriculture - Other',
       'Convenience/Corner Store',  
       'Home Maintenance Services','Hotel/Lodge/Resort', 'Indoor Entertainment/Rec',
       'Outdoor Entertainment/Rec', 'Overnight Camp',  
       'Personal Services', 'Religious Facility','Homeless Shelter',
       'Social Gathering','Travel'], 'Other'))

    df.type = df.type.replace(dict.fromkeys([
       'Jail', 'Law Enforcement - Other', 'Correctional, Other','Law Enforcement Administration',
       'State Prison'],'Jail/Prison'))

    df.type = df.type.replace(dict.fromkeys(['Child Care Center',
        'School Administration', 'School K-12', 'School/College Dorm','Trade School', 
       'Youth Sports/Activities'], 'Day Care/School'))

    df.type = df.type.replace(dict.fromkeys([
        'Office/Indoor Workspace', 'Distribution Center/Business', 
        'Farm/Dairy', 'Food Distribution', 'Materials Supplier', 
        'Food Warehouse','Non-Food Manufacturer/Warehouse',
        'Food Manufacturing/Packaging','Meat Processing/Packaging',
        'Construction Company/Contractor', 'Construction Site'],'Office/Mfg/Dist/Construction'))
    
   
    return df
