# Publish-Subscribe architecture
# Bus keeps track of event publishers and listeners
class Bus:
    eventAction = {}
    allowedEvents = {'onIntrusion':False, 'onEmergency':False, 'onAuthorizedEntry':False, 'onClick':[]}

    def publish(self, event):
        if event in self.eventAction:
            for i in self.eventAction[event]:
                i()

    def subscribe(self, event, action):
        if event in self.eventAction:
            self.eventAction[event].append(action)
        else:
            if event in self.allowedEvents:
                self.eventAction[event] = [action]
                self.allowedEvents[event] = True
                eventNotifier.subscribe(event, self)


class HouseSecurity(Bus):
    def __init__(self):
        pass

# Event handler methods
class Actions:
    def action1(self):
        print('Intruder detected in the premises')

    def action2(self):
        print('Emergency situation detected')

    def action3(self):
        print('Notifying authorities')


#****************************************************************************
# OS or hardware functionality
# Simulates the triggering of events
#****************************************************************************


class SystemEventNotifier:
    eventListeners = {'onIntrusion':[], 'onEmergency':[], 'onAuthorizedEntry':[], 'onClick':[]}

    def subscribe(self, event, controller):
        if event in self.eventListeners:
            self.eventListeners[event].append(controller)

    def triggerEvent(self, event):
        for i in self.eventListeners[event]:
            i.publish(event)


eventNotifier = SystemEventNotifier()

#************************************************************************


# test the code
def main():
    h = HouseSecurity()
    h.subscribe('onIntrusion', Actions.action1)
    h.subscribe('onIntrusion', Actions.action3)

    h1 = HouseSecurity()
    h1.subscribe('onEmergency', Actions.action2)
    h1.subscribe('onEmergency', Actions.action3)

    h1.subscribe('onIntrusion', Actions.action1)
    h1.subscribe('onIntrusion', Actions.action3)

    eventNotifier.triggerEvent('onIntrusion')

#main()