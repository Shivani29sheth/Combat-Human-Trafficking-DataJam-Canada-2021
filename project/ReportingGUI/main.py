from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from os.path import expanduser
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Path to user folder
home = expanduser("~")


# Screen manager and screen classes
class Manager(ScreenManager):
    reportData = {}


class FirstScreen(Screen):
    pass


class MinorScreen(Screen):
    pass


class PerpetratorScreen(Screen):
    pass


class Perpetrator2Screen(Screen):
    pass


class VictimScreen(Screen):
    pass


class SituationScreen(Screen):
    pass


class FinalScreen(Screen):
    pass

# Kivy framework starts here
root_widget = Builder.load_string('''
Manager:
    FirstScreen:
    MinorScreen:
    PerpetratorScreen:
    Perpetrator2Screen:
    VictimScreen:
    SituationScreen:
    FinalScreen:
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: q1
            #font_size: 50
            text: 'Do you feel as if one or more of your riders on this trip were victims of trafficking?\\nPLEASE NOTE, IF YOU SUSPECT THAT SOMEONE IS IN IMMEDIATE DANGER, CALL 911'
        Button:
            id: b1_y
            text: 'Yes'
            on_release:
                root.manager.current = 'minor'
        Button:
            id: b1_n
            text: 'No'
            on_release:
                app.stop()
<MinorScreen>:
    name: 'minor'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qm
            text: 'Do you think that the potential victim is under the age of 18?'
        Button:
            id: bm_y
            text: 'Yes'
            on_release:
                root.manager.reportData['isMinor'] = True  
                root.manager.current = 'perpetrator'
        Button:
            id: bm_n
            text: 'No'
            on_release: 
                root.manager.reportData['isMinor'] = False
                root.manager.current = 'perpetrator'
<PerpetratorScreen>:
    name: 'perpetrator'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qp
            text: 'Was/were the victim(s) traveling alone or with someone who was clearly "in charge?"'
        Button
            id: bp_y
            text: 'Yes'
            on_release: app.root.current = 'perpetrator2'
        Button
            id: bp_n
            text: 'No'
            on_release: app.root.current = 'victim'
        Button
            id: bp_bk
            text: 'Go back'
            on_release: app.root.current = 'minor'
<Perpetrator2Screen>:
    name: 'perpetrator2'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qp2
            text: 'Provide information about the person in charge'
        Label:
            text: 'Were they instructing the victim to lie?'
        CheckBox
            id: cp2_1
        Label:
            text: 'Did they exhibit controlling behaviour such as not letting the victim speak for themselves?'
        CheckBox
            id: cp2_2
        Label:
            text: 'Were they verbally abusive?'
        CheckBox
            id: cp2_3
        Button
            id: bp2_cn
            text: 'Confirm'
            on_release:
                root.manager.reportData['Perpetrator'] = [] 
                if cp2_1.state: root.manager.reportData['Perpetrator'].append('instructing victim to lie')
                if cp2_2.state: root.manager.reportData['Perpetrator'].append('controlling')
                if cp2_3.state: root.manager.reportData['Perpetrator'].append('abusive')
                app.root.current = 'victim'
        Button
            id: bp2_bk
            text: 'Go back'
            on_release: app.root.current = 'perpetrator'
<VictimScreen>:
    name: 'victim'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qv
            text: 'Provide information about the suspected victim'
        Label:
            text: 'Were they carrying bruises or cuts from physical abuse in various stages?'
        CheckBox
            id: cv_1
        Label:
            text: 'Were they in distress, fearful, disoriented or lost?'
        CheckBox
            id: cv_2
        Label:
            text: 'Did they look malnourished and/or tired?'
        CheckBox
            id: cv_3
        Label:
            text: 'Were they underdressed for the weather, seemed to have few and/or shabby possessions?'
        CheckBox
            id: cv_4
        Label:
            text: 'Were they nervous and possibly unable to make eye contact?'
        CheckBox
            id: cv_5
        Button
            id: bv_cn
            text: 'Confirm'
            on_release: 
                root.manager.reportData['Victim'] = []
                if cv_1.state:root.manager.reportData['Victim'].append('physically abused')
                if cv_2.state:root.manager.reportData['Victim'].append('emotional distress')
                if cv_3.state:root.manager.reportData['Victim'].append('malnourished and/or tired')
                if cv_4.state:root.manager.reportData['Victim'].append('looks impoverished')
                if cv_5.state:root.manager.reportData['Victim'].append('no eye contact')
                app.root.current = 'situation'
        Button
            id: bv_bk
            text: 'Go back'
            on_release: app.root.current = 'perpetrator'
<SituationScreen>:
    name: 'situation'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qs
            text: 'Check all that apply'
        Label:
            text: 'One or more of the riders were insistent on paying cash'
        CheckBox
            id: cs_1
        Label:
            text: 'The drop off location was at a side entrance or hidden entrance'
        CheckBox
            id: cs_2
        Label:
            text: 'The drop off location is near a hotel, truck stop, or airport'
        CheckBox
            id: cs_3
        Label:
            text: 'Did you ask and were they unable to provide you with ID?'
        CheckBox
            id: cs_4    
        Button
            id: bs_cn
            text: 'Confirm'
            on_release:
                root.manager.reportData['Situation'] = []
                if cs_1.state:root.manager.reportData['Situation'].append('cash payment')
                if cs_2.state:root.manager.reportData['Situation'].append('hidden entrance')
                if cs_3.state:root.manager.reportData['Situation'].append('near transit hub')
                if cs_4.state:root.manager.reportData['Situation'].append('no ID') 
                app.root.current = 'final'
        Button
            id: bs_bk
            text: 'Go back'
            on_release: app.root.current = 'victim'
<FinalScreen>:
    name: 'final'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: qf_1
            text: 'Provide a description of those involved, including physical identifiers such as hair color, approximate age, tattoos, etc.'
        TextInput:
            id: description
        Label:
            id:qf_2
            text: 'Provide any names or nicknames overheard'
        TextInput:
            id: names
        Label:
            text: 'Any other details we should know about?'
        TextInput:
            id: misc
        Label:
            text: 'Provide a phone number or email address that we can contact you with'
        TextInput:
            id: contact
        Button
            id: bf_cn
            text: 'Confirm'
            on_release:
                if description.text: root.manager.reportData['Description'] = description.text
                if names.text: root.manager.reportData['Names'] = names.text
                if misc.text: root.manager.reportData['Miscellaneous'] = misc.text
                if contact.text: root.manager.reportData['Contact'] = contact.text
                app.save(root.manager.reportData) 
                app.stop()
        Button
            id: bf_bk
            text: 'Go back'
            on_release: app.root.current = 'situation'
''')


class Report(App):
    """The front end of TRACKS framework, built using Kivy framework"""
    rData = None

    def build(self):
        return root_widget

    # Save to XML
    def save(self,mydata):
        # list items maintain their structure in xml file
        my_item_func = lambda x: 'item'
        xmldat = dicttoxml(mydata, item_func=my_item_func)
        xmlfl= open(home + '/report.xml', 'w')
        print(xmldat)
        xmlfl.write(parseString(xmldat).toprettyxml())
        xmlfl.close()
        return


Report().run()

