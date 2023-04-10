import os
import json


if os.path.isfile(os.getcwd()+"/config.json"):
    configFile = open(os.getcwd()+"/config.json","r")
    configJSON = json.load(configFile)
    configFile.close()
else :
    exit("config.json not found !")

class appConfig:
    PRODUCTION = configJSON['production']
    AUTH_DOMAINS = configJSON['authDomains']
    DOMAIN     = configJSON['appDomain']
    
    MYSQL_DBNAME   = configJSON['mysql']['name'] or os.getenv("MYSQL_DBNAME")
    MYSQL_USERNAME = configJSON['mysql']['userName'] or os.getenv("MYSQL_USERNAME")
    MYSQL_PASS     = configJSON['mysql']['password'] or os.getenv("MYSQL_PASS")
    MYSQL_URL    = configJSON['mysql']['url'] or os.getenv("MYSQL_URL")
    
    COOKIE_NAME = "$fapi_sid"
    COOKIE_SECRET_KEY  = os.getenv("COOKIE_SECRET") or "&^atiIU!n&^)09`!@#$#;fdrbHxAosu^87"
    COOKIE_MAX_AGE     = 86400
    COOKIE_SAME_SITE   = "strict"
    COOKIE_DOMAIN      =  None 
    
    CONNECT_MAIL = os.getenv("CONNECT_MAIL") or configJSON['mail']['connectMail']
    MAIL_USERNAME = os.getenv("MAIL_USERNAME") or configJSON['mail']['userName']
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD") or configJSON['mail']['password']
    MAIL_FROM     = os.getenv("MAIL_FROM") or configJSON['mail']['from']
    MAIL_SERVER   = os.getenv("MAIL_SERVER") or configJSON['mail']['url']
    MAIL_PORT     = os.getenv("MAIL_PORT") or configJSON['mail']['portNUmber']
    
    LIST_ENDPOINTS = configJSON['listAPI']