#!/usr/bin/env python
# coding: utf-8

# ### Creating dictionaries US states and Countries

# translate States to Two-Letter codes
us_states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


# ### Country Codes

# python dictionary for countries and codes in ISO format
# some minor manual repair was done to approximate worldometers site usage
iso3166 = {
	'AD': 'Andorra',
	'AE': 'United Arab Emirates',
	'AF': 'Afghanistan',
	'AG': 'Antigua and Barbuda',
	'AI': 'Anguilla',
	'AL': 'Albania',
	'AM': 'Armenia',
	'AN': 'Netherlands Antilles',
	'AO': 'Angola',
	'AQ': 'Antarctica',
	'AR': 'Argentina',
	'AT': 'Austria',
	'AU': 'Australia',
	'AW': 'Aruba',
	'AZ': 'Azerbaijan',
	'BA': 'Bosnia and Herzegovina',
	'BB': 'Barbados',
	'BD': 'Bangladesh',
	'BE': 'Belgium',
	'BF': 'Burkina Faso',
	'BG': 'Bulgaria',
	'BH': 'Bahrain',
	'BI': 'Burundi',
	'BJ': 'Benin',
	'BM': 'Bermuda',
	'BN': 'Brunei',
	'BO': 'Bolivia',
	'BR': 'Brazil',
	'BS': 'Bahama',
	'BT': 'Bhutan',
	'BW': 'Botswana',
	'BY': 'Belarus',
	'BZ': 'Belize',
	'CA': 'Canada',
	'CG': 'Congo',
	'CH': 'Switzerland',
	'CI': 'Ivory Coast',
	'CL': 'Chile',
	'CM': 'Cameroon',
	'CN': 'China',
	'CO': 'Colombia',
	'CR': 'Costa Rica',
	'CU': 'Cuba',
	'CY': 'Cyprus',
	'CZ': 'Czechia',
	'DE': 'Germany',
	'DJ': 'Djibouti',
	'DK': 'Denmark',
	'DM': 'Dominica',
	'DZ': 'Algeria',
	'EC': 'Ecuador',
	'EE': 'Estonia',
	'EG': 'Egypt',
	'EH': 'Western Sahara',
	'ER': 'Eritrea',
	'ES': 'Spain',
	'ET': 'Ethiopia',
	'FI': 'Finland',
	'FJ': 'Fiji',
	'FM': 'Micronesia',
	'FR': 'France',
	'GA': 'Gabon',
	'UK': 'uk',
	'GD': 'Grenada',
	'GE': 'Georgia',
	'GF': 'French Guiana',
	'GH': 'Ghana',
	'GI': 'Gibraltar',
	'GL': 'Greenland',
	'GM': 'Gambia',
	'GN': 'Guinea',
	'GP': 'Guadeloupe',
	'GQ': 'Equatorial Guinea',
	'GR': 'Greece',
	'GT': 'Guatemala',
	'GW': 'Guinea-Bissau',
	'GY': 'Guyana',
	'HK': 'Hong Kong',
	'HN': 'Honduras',
	'HR': 'Croatia',
	'HT': 'Haiti',
	'HU': 'Hungary',
	'ID': 'Indonesia',
	'IE': 'Ireland',
	'IL': 'Israel',
	'IN': 'India',
	'IQ': 'Iraq',
	'IR': 'Iran',
	'IS': 'Iceland',
	'IT': 'Italy',
	'JM': 'Jamaica',
	'JO': 'Jordan',
	'JP': 'Japan',
	'KE': 'Kenya',
	'KG': 'Kyrgyzstan',
	'KH': 'Cambodia',
	'KR': 'S.Korea',
	'KW': 'Kuwait',
	'KY': 'Cayman Islands',
	'KZ': 'Kazakhstan',
	'LA': 'Laos',
	'LB': 'Lebanon',
	'LC': 'Saint Lucia',
	'LI': 'Liechtenstein',
	'LK': 'Sri Lanka',
	'LR': 'Liberia',
	'LS': 'Lesotho',
	'LT': 'Lithuania',
	'LU': 'Luxembourg',
	'LV': 'Latvia',
	'LY': 'Libya',
	'MA': 'Morocco',
	'MC': 'Monaco',
	'MD': 'Moldova',
	'MG': 'Madagascar',
	'MH': 'Marshall Islands',
	'ML': 'Mali',
	'MN': 'Mongolia',
	'MM': 'Myanmar',
	'MO': 'Macau',
	'MQ': 'Martinique',
	'MR': 'Mauritania',
	'MS': 'Monserrat',
	'MT': 'Malta',
	'MU': 'Mauritius',
	'MV': 'Maldives',
	'MW': 'Malawi',
	'MX': 'Mexico',
	'MY': 'Malaysia',
	'MZ': 'Mozambique',
	'NA': 'Namibia',
	'NC': 'New Caledonia',
	'NE': 'Niger',
	'NF': 'Norfolk Island',
	'NG': 'Nigeria',
	'NI': 'Nicaragua',
	'NL': 'Netherlands',
	'NO': 'Norway',
	'NP': 'Nepal',
	'NR': 'Nauru',
	'NU': 'Niue',
	'NZ': 'New Zealand',
	'OM': 'Oman',
	'PA': 'Panama',
	'PE': 'Peru',
	'PF': 'French Polynesia',
	'PG': 'Papua New Guinea',
	'PH': 'Philippines',
	'PK': 'Pakistan',
	'PL': 'Poland',
	'PR': 'Puerto Rico',
	'PT': 'Portugal',
	'PW': 'Palau',
	'PY': 'Paraguay',
	'QA': 'Qatar',
	'RO': 'Romania',
	'RU': 'Russia',
	'RW': 'Rwanda',
	'SA': 'Saudi Arabia',
	'SB': 'Solomon Islands',
	'SC': 'Seychelles',
	'SD': 'Sudan',
	'SE': 'Sweden',
	'SG': 'Singapore',
	'SI': 'Slovenia',
	'SK': 'Slovakia',
	'SL': 'Sierra Leone',
	'SM': 'San Marino',
	'SN': 'Senegal',
	'SO': 'Somalia',
	'SR': 'Suriname',
	'SV': 'El Salvador',
	'SY': 'Syria',
	'SZ': 'Swaziland',
	'TD': 'Chad',
	'TG': 'Togo',
	'TH': 'Thailand',
	'TJ': 'Tajikistan',
	'TM': 'Turkmenistan',
	'TN': 'Tunisia',
	'TO': 'Tonga',
	'TP': 'East Timor',
	'TR': 'Turkey',
	'TT': 'Trinidad and Tobago',
	'TV': 'Tuvalu',
	'TW': 'Taiwan',
	'TZ': 'Tanzania',
	'UA': 'Ukraine',
	'UG': 'Uganda',
	'US': 'United States of America',
	'UY': 'Uruguay',
	'UZ': 'Uzbekistan',
	'VA': 'Vatican City',
	'VE': 'Venezuela',
	'VG': 'British Virgin Islands',
	'VN': 'Viet Nam',
	'VU': 'Vanuatu',
	'WS': 'Samoa',
	'YE': 'Yemen',
	'ZA': 'South Africa',
	'ZM': 'Zambia',
	'ZR': 'Zaire',
	'ZW': 'Zimbabwe'
}

# time zones list
tz_dict = {0:'Etc/GMT',
 1:'Etc/GMT+1',
 10:'Etc/GMT+10',
 11:'Etc/GMT+11',
 12:'Etc/GMT+12',
 2:'Etc/GMT+2',
 3:'Etc/GMT+3',
 4:'Etc/GMT+4',
 5:'Etc/GMT+5',
 6:'Etc/GMT+6',
 7:'Etc/GMT+7',
 8:'Etc/GMT+8',
 9:'Etc/GMT+9',
 -1:'Etc/GMT-1',
 -10:'Etc/GMT-10',
 -11:'Etc/GMT-11',
 -12:'Etc/GMT-12',
 -13:'Etc/GMT-13',
 -14:'Etc/GMT-14',
 -2:'Etc/GMT-2',
 -3:'Etc/GMT-3',
 -4:'Etc/GMT-4',
 -5:'Etc/GMT-5',
 -6:'Etc/GMT-6',
 -7:'Etc/GMT-7',
 -8:'Etc/GMT-8',
 -9:'Etc/GMT-9'}


# ### States

# In[147]:


# Repair dictionaries to match lower case and hyphens used on worldometers.com
def repair_dict(dictionary):
    # Flip keys and values and make new keys all lower case
    dict_temp = {}
    for k,v in dictionary.items():
        dict_temp[k.lower()]= v 

    #replace spaces with a dash
    dictionary = {k.replace(' ', '-'): v 
        for k, v in dict_temp.items()}
    return dictionary


# In[148]:


all_states = repair_dict(us_states)


# ### Countries

# In[149]:


def reverse_dict(dictionary):
    # reverse keys and values
    return dict(map(reversed, dictionary.items()))


# In[150]:


iso3166r = reverse_dict(iso3166)


# In[151]:


all_countries = repair_dict(iso3166r)


# ### Select states and countries of interest

# In[152]:


def custom_list(some_string):
    #Takes as input upper or lower codes for states or countries
    #print("\n")
    slist = some_string.split()
    slist = [item.upper() for item in slist]
    return slist


# In[ ]:





# In[ ]:





# In[ ]:




