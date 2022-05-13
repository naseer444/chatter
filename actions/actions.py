# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet, FollowupAction


from .firebaseRetrieval import funcLake
from .firebaseRetrieval import funcValley
from .firebaseRetrieval import funcNationalParks
from .firebaseRetrieval import funcMosques
from .firebaseRetrieval import funcHill
from .firebaseRetrieval import funcWaterfall
from .firebaseRetrieval import funcMountain



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message("Here are the Lakes I found in Pakistan:\n\n\n")
        dispatcher.utter_message(funcLake())


class ActionValley(Action):
    
    def name(self) -> Text:
        return "action_valley"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are the Valleys I found in Pakistan:\n\n\n")
        dispatcher.utter_message(funcValley())   
        
        
class ActionNationalParks(Action):
    
    def name(self) -> Text:
        return "action_NationalParks"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are the National Parks of Pakistan:\n\n\n")
        dispatcher.utter_message(funcNationalParks()) 


class ActionMosques(Action):
    
    def name(self) -> Text:
        return "action_Mosques"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are the Mosques of Pakistan:\n\n\n")
        dispatcher.utter_message(funcMosques()) 
        
        
        

class ActionHill(Action):
    
    def name(self) -> Text:
        return "action_hill"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are the Hill Stations of Pakistan:\n\n\n")
        dispatcher.utter_message(funcHill()) 
        

class ActionWaterfall(Action):
    
    def name(self) -> Text:
        return "action_waterfall"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are the Waterfalls of Pakistan:\n\n\n")
        dispatcher.utter_message(funcWaterfall()) 
        
        
        
class ActionMountain(Action):
    
    def name(self) -> Text:
        return "action_mountain"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Here are some Mountains of Pakistan:\n\n\n")
        dispatcher.utter_message(funcMountain()) 
        
        
        
        
        
        
        