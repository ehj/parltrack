#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    This file is part of parltrack

#    parltrack is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    parltrack is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with parltrack  If not, see <http://www.gnu.org/licenses/>.

# (C) 2011 by Stefan Marsiske, <stefan.marsiske@gmail.com>, Asciimoo

COMMITTEE_MAP={'AFET': "Foreign Affairs",
               'DROI': "Human Rights",
               'SEDE': "Security and Defence",
               'DEVE': "Development",
               'INTA': "International Trade",
               'BUDG': "Budgets",
               'CONT': "Budgetary Control",
               'CODE': "Conciliation Committee",
               'ECON': "Economic and Monetary Affairs",
               'EMPL': "Employment and Social Affairs",
               'ENVI': "Environment, Public Health and Food Safety",
               'ITRE': "Industry, Research and Energy",
               'IMCO': "Internal Market and Consumer Protection",
               'TRAN': "Transport and Tourism",
               'REGI': "Regional Development",
               'AGRI': "Agriculture and Rural Development",
               'PECH': "Fisheries",
               'CULT': "Culture and Education",
               'JURI': "Legal Affairs",
               'LIBE': "Civil Liberties, Justice and Home Affairs",
               'AFCO': "Constitutional Affairs",
               'FEMM': "Women's Rights and Gender Equality",
               'PETI': "Petitions",
               'CRIS': "Financial, Economic and Social Crisis",
               'SURE': "Policy Challenges Committee",
               'RETT': "Regional Policy, Transport and Tourism",
               'Foreign Affairs': 'AFET',
               "Regional Policy, Transport and Tourism": 'RETT',
               'Foreign Affairs': 'AFET',
               'Human Rights': 'DROI',
               'Security and Defence': 'SEDE',
               'Development': 'DEVE',
               'International Trade': 'INTA',
               'Budgets': 'BUDG',
               'Budgetary Control': 'CONT',
               'Economic and Monetary Affairs': 'ECON',
               'Employment and Social Affairs': 'EMPL',
               'Environment, Public Health and Food Safety': 'ENVI',
               'Industry, Research and Energy': 'ITRE',
               'Internal Market and Consumer Protection': 'IMCO',
               'Transport and Tourism': 'TRAN',
               'Regional Development': 'REGI',
               'Agriculture and Rural Development': 'AGRI',
               'Fisheries': 'PECH',
               'Culture and Education': 'CULT',
               'Legal Affairs': 'JURI',
               'Civil Liberties, Justice and Home Affairs': 'LIBE',
               'Constitutional Affairs': 'AFCO',
               "Women's Rights and Gender Equality": 'FEMM',
               u"Women’s Rights and Gender Equality": 'FEMM',
               'Petitions': 'PETI',
               'Financial, Economic and Social Crisis': 'CRIS',
               'Policy Challenges Committee': 'SURE',
               'Committee on Foreign Affairs': 'AFET',
               'Committee on Human Rights': 'DROI',
               'Committee on Security and Defence': 'SEDE',
               'Committee on Development': 'DEVE',
               'Committee on International Trade': 'INTA',
               'Committee on Budgets': 'BUDG',
               'Committee on Budgetary Control': 'CONT',
               'Committee on Economic and Monetary Affairs': 'ECON',
               'Committee on Employment and Social Affairs': 'EMPL',
               'Committee on Environment, Public Health and Food Safety': 'ENVI',
               'Committee on Industry, Research and Energy': 'ITRE',
               'Committee on Internal Market and Consumer Protection': 'IMCO',
               'Committee on the Internal Market and Consumer Protection': 'IMCO',
               'Committee on Transport and Tourism': 'TRAN',
               'Committee on Regional Development': 'REGI',
               'Committee on Agriculture and Rural Development': 'AGRI',
               'Committee on Fisheries': 'PECH',
               'Committee on Culture and Education': 'CULT',
               'Committee on Legal Affairs': 'JURI',
               'Committee on Civil Liberties, Justice and Home Affairs': 'LIBE',
               'Committee on Constitutional Affairs': 'AFCO',
               "Committee on Women's Rights and Gender Equality": 'FEMM',
               'Committee on Petitions': 'PETI',
               'Committee on Financial, Economic and Social Crisis': 'CRIS',
               'Committee on Policy Challenges Committee': 'SURE'}

STAGEMAP = {'Preparatory phase in Parliament': '01. Preparatory phase in EP',
            'Awaiting Parliament 1st reading / single reading / budget 1st stage': '02. EP 1st reading',
            'Awaiting Council 1st reading position / budgetary conciliation convocation': '03. EC 1st reading position',
            'Awaiting reconsultation': '04. Awaiting reconsultation',
            'Awaiting Parliament decision after Council rejection of joint text': '05. EP decision after EC rejection of joint text',
            'Awaiting Council decision, blocked at 1st reading': '06. EC decision, blocked at 1st reading',
            'Awaiting Parliament 2nd reading': '07. EP 2nd reading',
            'Awaiting Council decision, 2nd reading': '08. EC decision, 2nd reading',
            'Awaiting Parliament and Council decision, 3rd reading': '09. EP and EC decision, 3rd reading',
            'Conciliation ongoing': '10. Conciliation ongoing',
            'Political agreement on final act': '11. Political agreement on final act',
            'Awaiting signature': '12. Awaiting signature',
            'Awaiting final decision': '13. Awaiting final decision',}

STAGES = ['Preparatory phase in Parliament',
          'Awaiting Parliament 1st reading / single reading / budget 1st stage',
          'Awaiting reconsultation',
          'Awaiting Council decision, blocked at 1st reading',
          'Awaiting Council 1st reading position / budgetary conciliation convocation',
          'Budgetary conciliation committee convened',
          'Awaiting announcement of budgetary joint text',
          'Awaiting budgetary conciliation report',
          'Awaiting Parliament decision on budgetary joint text',
          'Awaiting Council decision on budgetary joint text',
          'Awaiting Parliament decision after Council rejection of joint text',
          'Awaiting Parliament 2nd reading',
          'Awaiting Council decision, 2nd reading',
          'Conciliation ongoing',
          'Conciliation ended',
          'Awaiting Parliament and Council decision, 3rd reading',
          'Political agreement on final act',
          'Awaiting signature',
          'Awaiting final decision',
          'Procedure completed, awaiting publication in Official Journal']

ALL_STAGES= [ "Preparatory phase in Parliament",
              "Awaiting Parliament 1st reading / single reading / budget 1st stage",
              "Awaiting reconsultation",
              "Awaiting Council decision, blocked at 1st reading",
              "Awaiting Council 1st reading position / budgetary conciliation convocation",
              "Budgetary conciliation committee convened",
              "Awaiting announcement of budgetary joint text",
              "Awaiting budgetary conciliation report",
              "Awaiting Parliament decision on budgetary joint text",
              "Awaiting Council decision on budgetary joint text",
              "Awaiting Parliament decision after Council rejection of joint text",
              "Awaiting Parliament 2nd reading",
              "Awaiting Council decision, 2nd reading",
              "Conciliation ongoing",
              "Conciliation ended",
              "Awaiting Parliament and Council decision, 3rd reading",
              "Political agreement on final act",
              "Awaiting signature",
              "Awaiting final decision",
              "Procedure completed, awaiting publication in Official Journal",
              "Procedure completed",
              "Procedure rejected",
              "Procedure lapsed or withdrawn"]

buildings={ u"Altiero Spinelli": 'ASP',
            u"Willy Brandt": 'WIB',
            u"Paul-Henri Spaak": 'PHS',
            u"Atrium": "ATR",
            u"Louise Weiss": 'LOW',
            u"Winston Churchill": 'WIC',
            u'Salvador de Madariaga': "SDM",
            u"Bât. Altiero Spinelli": 'ASP',
            u"Bât. Willy Brandt": 'WIB',
            u"Bât. Paul-Henri Spaak": 'PHS',
            u"Bât. Atrium": "ATR",
            u"Bât. Louise Weiss": 'LOW',
            u"Bât. Winston Churchill": 'WIC',
            u'B\xe2t. Salvador de Madariaga': "SDM",
            }

ipexevents={u'CSL 1R Agreement': {'body': 'CSL', 'oeil': ['Council meeting'], },
            u'CSL Common Position': {'body': 'CSL', 'oeil': ['Council position'], },
            u'CSL Final Adoption': {'body': 'CSL',},
            u'CSL Final Agreement': {'body': 'CSL',},
            u'CSL Non Acceptance': {'body': 'CSL',},
            u'Date': {'body': 'EP', 'oeil': ['Initial legislative document', 'Commission/Council: initial legislative document', 'Legislative proposal published', 'Initial legislative proposal published', 'Modified legislative proposal published'], },
            u'Deadline Amendments': {'body': 'EP',},
            u'EP 1R Committee': {'body': 'EP', 'oeil': ['EP: decision of the committee responsible, 1st reading/single reading'], },
            u'EP 1R Plenary': {'body': 'EP', 'oeil': ['EP: position, 1st reading or single reading'], },
            u'EP 2R Committee': {'body': 'EP', 'oeil': ['EP: decision of the committee responsible, 2nd reading'], },
            u'EP 2R Plenary': {'body': 'EP', 'oeil': ['EP: position, 2nd reading'], },
            u'EP 3R Plenary': {'body': 'EP', 'oeil': ['EP: legislative resolution, 3rd reading'], },
            u'EP Conciliation Committee': {'body': 'EP', 'oeil': ['Results of conciliation'], },
            u'EP officialisation': {'body': 'EP', 'oeil': ['Commission/Council: initial legislative document'], },
            u'End Date': {'body': 'EP', 'oeil': ['Final legislative act'], },
            u'Foreseen CSL Activities': {'body': 'CSL',},
            u'Prev Adopt in Cte': {'body': 'EP',},
            u'Prev DG PRES': {'body': 'EC'},
            }

COUNTRIES = {'BE': 'Belgium',
             'BG': 'Bulgaria',
             'CZ': 'Czech Republic',
             'DK': 'Denmark',
             'DE': 'Germany',
             'EE': 'Estonia',
             'IE': 'Ireland',
             'EL': 'Greece',
             'ES': 'Spain',
             'FR': 'France',
             'IT': 'Italy',
             'CY': 'Cyprus',
             'LV': 'Latvia',
             'LT': 'Lithuania',
             'LU': 'Luxembourg',
             'HU': 'Hungary',
             'MT': 'Malta',
             'NL': 'Netherlands',
             'AT': 'Austria',
             'PL': 'Poland',
             'PT': 'Portugal',
             'RO': 'Romania',
             'SI': 'Slovenia',
             'SK': 'Slovakia',
             'FI': 'Finland',
             'SE': 'Sweden',
             'UK': 'United Kingdom',
             }

SEIRTNUOC = {'Belgium': 'BE',
             'Bulgaria': 'BG',
             'Czech Republic':'CZ',
             'Denmark': 'DK',
             'Germany': 'DE',
             'Estonia': 'EE',
             'Ireland': 'IE',
             'Greece': 'EL',
             'Spain': 'ES',
             'France': 'FR',
             'Italy': 'IT',
             'Cyprus': 'CY',
             'Latvia': 'LV',
             'Lithuania': 'LT',
             'Luxembourg': 'LU',
             'Hungary': 'HU',
             'Malta': 'MT',
             'Netherlands': 'NL',
             'Austria': 'AT',
             'Poland': 'PL',
             'Portugal': 'PT',
             'Romania': 'RO',
             'Slovenia': 'SI',
             'Slovakia': 'SK',
             'Finland': 'FI',
             'Sweden': 'SE',
             'United Kingdom':'GB',
             }

GROUPS=[
   'Communist and Allies Group',
   'European Conservative Group',
   'European Conservatives and Reformists',
   'European Democratic Group',
   'Europe of freedom and democracy Group',
   'Europe of Nations Group (Coordination Group)',
   'Forza Europa Group',
   'Confederal Group of the European United Left',
   'Confederal Group of the European United Left/Nordic Green Left',
   'Confederal Group of the European United Left - Nordic Green Left',
   'Christian-Democratic Group',
   "Christian-Democratic Group (Group of the European People's Party)",
   "Group of the European People's Party ",
   'Group for a Europe of Democracies and Diversities',
   'Group for the European United Left',
   'Group for the Technical Coordination and Defence of Indipendent Groups and Members',
   'Group of Independents for a Europe of Nations',
   'Group of the Alliance of Liberals and Democrats for Europe',
   'Group of the European Democratic Alliance',
   'Group of the European Liberal, Democrat and Reform Party',
   'Group of the European Radical Alliance',
   'Group of the European Right',
   'Group of the Greens/European Free Alliance',
   'Group of the Party of European Socialists',
   'Group of the Progressive Alliance of Socialists and Democrats in the European Parliament',
   'European Democratic Union Group',
   'Group of European Progressive Democrats',
   "Group of the European People's Party (Christian Democrats) and European Democrats",
   "Group of the European People's Party (Christian Democrats)",
   'Group Union for Europe',
   'Identity, Tradition and Sovereignty Group',
   'Independence/Democracy Group',
   'Left Unity',
   'Liberal and Democratic Group',
   'Liberal and Democratic Reformist Group',
   'Non-attached',
   'Non-attached Members',
   "Rainbow Group: Federation of the Green Alternative European Links, Agelev-Ecolo, the Danish People's Movement against Membership of the European Community and the European Free Alliance in the European Parliament",
   'Rainbow Group in the European Parliament',
   'Socialist Group',
   'Socialist Group in the European Parliament',
   'Technical Coordination and Defence of Independent Groups and Members',
   'Technical Group of Independent Members - mixed group',
   'Technical Group of the European Right',
   'The Green Group in the European Parliament',
   'Union for Europe of the Nations Group', ]

group_map={ "Confederal Group of the European United Left - Nordic Green Left": 'GUE/NGL',
            "Confederal Group of the European United Left-Nordic Green Left": 'GUE/NGL',
            'Confederal Group of the European United Left / Nordic Green Left': 'GUE/NGL',
            'Confederal Group of the European United Left/Nordic Green Left': 'GUE/NGL',
            "European Conservatives and Reformists": 'ECR',
            'European Conservatives and Reformists Group': 'ECR',
            "Europe of freedom and democracy Group": 'EFD',
            'Europe of Freedom and Democracy Group': 'EFD',
            "Group of the Alliance of Liberals and Democrats for Europe": 'ALDE',
            "Group of the Greens/European Free Alliance": "Verts/ALE",
            "Group of the Progressive Alliance of Socialists and Democrats in the European Parliament": "S&D",
            'Group for a Europe of Democracies and Diversities': 'EDD',
            'Group of the European Liberal Democrat and Reform Party': 'ELDR',
            'Group of the European Liberal, Democrat and Reform Party': 'ELDR',
            'Group indépendence/Démocratie': ['ID','INDDEM', 'IND/DEM'],
            'Independence/Democracy Group': ['ID', 'INDDEM', 'IND/DEM'],
            'Non-attached Members': ['NA','NI'],
            'Non-attached': ['NA','NI'],
            'Identity, Tradition and Sovereignty Group': 'ITS',
            "Group of the European People's Party (Christian Democrats) and European Democrats": 'PPE-DE',
            "Group of the European People's Party (Christian Democrats)": 'PPE',
            "Group of the European People's Party (Christian-Democratic Group)": "PPE",
            'Group of the Party of European Socialists': 'PSE',
            'Socialist Group in the European Parliament': 'PSE',
            'Technical Group of Independent Members': 'TDI',
            'Group indépendence/Démocratie': 'UEN',
            'Union for a Europe of Nations Group': 'UEN',
            'Union for Europe of the Nations Group': 'UEN',
            'Group of the Greens / European Free Alliance': 'Verts/ALE',
            'Greens/EFA': 'Verts/ALE',
            }
groupids=[]
for item in group_map.values():
    if type(item)==list:
        groupids.extend(item)
    else:
        groupids.append(item)

CELEXCODES={
    "1": { "Sector": "Treaties",
           "Document Types" : { "D": "Treaty of Amsterdam 1997",
                                "M": "Treaty on the European Union, Maastricht 1992 - EU Treaty - consolidated version 1997",
                                "E": "EEC Treaty 1957 - EEC Treaty - consolidated version 1992 - EEC Treaty - consolidated version 1997",
                                "K": "ECSC Treaty 1951",
                                "A": "EURATOM Treaty 1957",
                                "U": "Single European Act 1986",
                                "G": "Groenland Treaty 1985",
                                "R": "Treaty amending certain financial provisions 1975",
                                "F": "Treaty amending certain budgetary provisions 1970",
                                "F": "Merger Treaty 1965",
                                "B": "Accession Treaty 1972 (United Kingdom, Denmark, Ireland, Norway)",
                                "H": "Accession Treaty 1979 (Greece)",
                                "I": "Accession Treaty 1985 (Spain, Portugal)",
                                "N": "Accession Treaty 1994 (Austria, Sweden, Finland, Norway)",
                                "T": "Accession Treaty 2003 (Slovakia, Estonia, Poland, Hungary, Lithuania, Latvia, Slovenia, Cyprus, Czech Republic, Malta)",
                                }},
    "2": { "Sector": "External Agreements",
           "Document Types" : { "A":"Agreements with non-member States or international organisations",
                                "D":"Acts of bodies created by international agreements",
                                "P":"Acts of parliamentary bodies created by international agreements",
                                "X":"Other Acts ",},},
    "3": { "Sector": "Legislation",
           "Document Types" : { "E":"Common Foreign and Security Policy (CFSP) - common positions / joint actions / common strategies",
                                "F":"Justice and Home Affairs (JHA) - common positions / framework decisions",
                                "R":"Regulations",
                                "L":"Directives",
                                "D":"Decisions sui generis",
                                "S":"ECSC Decisions of general interest",
                                "M":"Non-opposition to a notified concentration",
                                "J":"Non-opposition to a notified joint venture",
                                "B":"Budget",
                                "K":"Recommendations ECSC",
                                "O":"Guidelines ECB",
                                "H":"Recommendations",
                                "A":"Avis",
                                "G":"Resolutions",
                                "C":"Declarations",
                                "Q":"Institutional arrangements, Rules of Procedure, Internal agreements",
                                "X":"Other documents",},},
    "4": { "Sector": "Internal Agreements",
           "Document Types" : { "D":"Decisions of the representatives of the governments of the Member States",
                                "X":"Other acts",},},
    "5": { "Sector": "Proposals + preparatory documents",
           "Document Types" : { "AG":"Council - common positions",
                                "KG":"Council - assent ECSC",
                                "IG":"Member States - Initiatives",
                                "XG":"Council - other acts",
                                "PC":"COM Documents - proposals for legislation",
                                "DC":"COM Documents - other documents",
                                "SC":"SEC Documents",
                                "XC":"Commission - other acts",
                                "AP":"EP - legislative resolution",
                                "BP":"EP - budget",
                                "IP":"EP - other resolutions",
                                "XP":"EP - other acts",
                                "AA":"Court of Auditors - opinions",
                                "TA":"Court of Auditors - reports",
                                "SA":"Court of Auditors - special reports",
                                "XA":"Court of Auditors - other acts",
                                "AB":"ECB - opinions",
                                "HB":"ECB - recommendations",
                                "XB":"ECB - other acts",
                                "AE":"ESC - opinions on consultation",
                                "IE":"ESC - other opinions",
                                "XE":"ESC - other acts",
                                "AR":"CR - opinions on consultation",
                                "IR":"CR - other opinions",
                                "XR":"CR - other acts",
                                "AK":"ECSC Com. - opinions",
                                "XK":"ECSC Com. - other acts",
                                "XX":"Other acts ", }, },
    "6": { "Sector": "Case Law",
           "Document Types" : { "A":"Court of First Instance Judgments",
                                "B":"Court of First Instance - Orders",
                                "D":"Court of First Instance - Third Party Proceedings",
                                "F":"Court of First Instance - Opinions",
                                "H":"Court of First Instance - Case report",
                                "C":"Court of Justice - Conclusions of the Avocate-General",
                                "J":"Court of Justice - Judgments",
                                "O":"Court of Justice - Orders",
                                "P":"Court of Justice - Case report",
                                "S":"Court of Justice - Seizure",
                                "T":"Court of Justice - Third Party Proceedings",
                                "V":"Court of Justice - Opinions",
                                "X":"Court of Justice - Rulings",},},
    "7": { "Sector": "National Implementation",
           "Document Types" : {"L":"National Implementation Measures - implementation of directives",},},
    "9": { "Sector": "European Parliamentary Questions",
           "Document Types" : { "E":"European European Parliament - Written Questions",
                                "H":"European European Parliament - Questions at Questiontime",
                                "O":"European European Parliament - Oral questions",},},
    "C": { "Sector": "OJC Documents", "Document Types" : {},},
    "E": { "Sector": "EFTA Documents",
           "Document Types" : { "A":"International Agreements",
                                "C":"Acts of the EFTA Surveillance Authority",
                                "G":"Acts of the EFTA Standing Committee",
                                "J":"Decisions, Orders, Consultative opinions of the EFTA Court",
                                "P":"Pending cases of the EFTA Court",
                                "X":"EFTA - Other Acts",},},
    }
