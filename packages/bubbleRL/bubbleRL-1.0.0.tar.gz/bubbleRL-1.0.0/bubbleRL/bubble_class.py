import json
import string
import requests
from urllib.parse import quote


class Bubble:
    """This class allow you to make all request methods to an any bubble.io application on a simpple way"""
    
    def __init__(self, url: string, api_key: string):
        self.__url        = url
        self.__api_key    = api_key
        self.__header     = {"content-type": "application/json","Authorization": "Bearer " + self.__api_key}
        self.__object     = ""
        self.__table      = ""
        self.__newData    = ""
        self.__newObjects = []
        self.__replacedObject    = ""
        self.__updatedObject     = ""
        self.__deletedObject     = ""
    
    #Métodos get de las variables

    @property
    def object(self):
        return self.__object
    
    @property
    def table(self):
        return self.__table

    @property
    def newData(self):
        return self.__newData

    @property
    def newObjects(self):
        return self.__newObjects
    
    @property
    def replacedObject(self):
        return self.__replacedObject
    
    @property
    def updatedObject(self):
        return self.__updatedObject
    
    @property
    def updatedObject(self):
        return self.__updatedObject
    
    @property
    def deletedObject(self):
        return self.__deletedObject
    
    #Métodos set de las variables

    @object.setter
    def object(self, object):
        self.__object = object

    @table.setter
    def table(self, table):
        self.__table = table

    @newData.setter
    def newData(self, newData):
        self.__newData = newData

    @newObjects.setter
    def newObjects(self, newObjects):
        self.__newObjects = newObjects

    @replacedObject.setter
    def replacedObject(self, replacedObject):
        self.__replacedObject = replacedObject

    @updatedObject.setter
    def updatedObject(self, updatedObject):
        self.__updatedObject = updatedObject

    @deletedObject.setter
    def deletedObject(self, deletedObject):
        self.__deletedObject = deletedObject

    #Métodos de la clase

    def getObjet(self, table:string, _id:string):
        """Get an specific object from an specific table of the data base"""
        try:
            r = requests.get(self.__url + "/" + table + "/" + _id, headers=self.__header).json()
            try:
                self.object = r["response"]
            except: 
                self.object = r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def getTable(self, table:string, constrains):
        """Get a full table from the date base"""
        responseRequest = []
        if len(constrains) > 0:
            try:
                responseConsulta = requests.get(self.__url + "/" + table + "?cursor=0" + "&constraints=" + quote(json.dumps(constrains),"UTF-8"),
                headers=self.__header).json()
                try:
                    resto = int(responseConsulta["response"]["remaining"])
                    count = int(responseConsulta["response"]["count"])
                    for item in responseConsulta["response"]["results"]:
                        responseRequest.append(item)
                    while resto > (count-100):
                        responseRepetida = requests.get(self.__url + "/" + table + "?cursor="+ str(count) + "&constraints=" +                    
                        quote(json.dumps(constrains),"UTF-8"), headers=self.__header).json()
                        for item in responseRepetida["response"]["results"]:
                            responseRequest.append(item)
                        count = count + 100
                    self.table = responseRequest
                except:
                    self.table = responseRequest
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        else:
            try:
                responseConsulta = requests.get(self.__url + "/" + table + "?cursor=0", headers=self.__header).json()
                try:
                    resto = int(responseConsulta["response"]["remaining"])
                    count = int(responseConsulta["response"]["count"])
                    for item in responseConsulta["response"]["results"]:
                        responseRequest.append(item)
                    while resto > (count-100):
                        responseRepetida = requests.get(self.__url + "/" + table + "?cursor="+ str(count), headers=self.__header).json()
                        for item in responseRepetida["response"]["results"]:
                            responseRequest.append(item)
                        count = count + 100
                    self.table = responseRequest
                except:
                    self.table = responseRequest
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

    def newObject(self, table:string, properties:dict):
        """Create an object on a specific table"""
        if isinstance(properties, dict):
            try:
                r = requests.post(self.__url + "/" + table, data=json.dumps(properties), headers=self.__header).json()
                try:
                    self.newData = r["id"]
                except:
                    self.newData = r
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        else:
            return "The properties should be a json"

    def newObjects(self, table:string, properties):
        """Create multiples objects on a specific table"""
        p = []
        for p in properties:
            if isinstance(p, dict):
                try:
                    r = requests.post(self.__url + "/" + table, data=json.dumps(p), headers=self.__header).json()
                    try:
                        p.append(r["id"])
                    except:
                        p.append(r)
                except requests.exceptions.RequestException as e:
                    raise SystemExit(e)
            
            else:
                return "The proporties should be a json"
        self.newObjects = p

    def replaceObject(self, table:string, uid:string, properties:dict):
        """Update all the properties from an object, if dont sent some propertie, this will be updated to an empty propertie """
        if isinstance(properties, dict):
            try:
                r = requests.put(self.__url + "/" + table + "/" + uid, data=json.dumps(properties), headers=self.__header)
                try:
                    self.replacedObject = r.status_code
                except:
                    self.replacedObject = r
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        else:
            return "The properties should be a json"

    def updateObject(self, table:string, uid:string, properties:dict):
        """Update an specific propertie from an object, this will not overwrite any propiertie that wasn't given"""
        if isinstance(properties, dict):
            try:
                r = requests.patch(self.__url + "/" + table + "/" + uid, data=json.dumps(properties), headers=self.__header)
                try:
                    self.updatedObject = r.status_code
                except:
                    self.updatedObject = r
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
        else:
            return "The properties should be a json"

    def deleteObject(self, table:string, uid:string):
        """Delete an specifict object from a table"""
        try:
            r = requests.delete(self.__url + "/" + table + "/" + uid, headers=self.__header)
            try:
                self.deletedObject = r["statusCode"]
            except:
                self.deletedObject = r.status_code
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        