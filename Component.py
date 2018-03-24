#Component based architectural style

import PublishSubscribe

# persistent storage
class DataStorage:
    password = "password"

    def getPassword(self):
        return self.password

# Parent component object
class Component(PublishSubscribe.Bus):
    def show(self):
        pass

class Button(Component):
    text = ''

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return '************\n* ' + self.text + ' *\n************'

    def show(self):
        print(self)


class TextInput(Component):
    label = ''
    value = ''
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label+' : '+self.value

    def show(self):
        val = self.label + ': '
        self.value = input(val)

class Label(Component):
    value = ''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def show(self):
        print(self)

    def setVal(self, val):
        self.value = val







# Sample view made with the above components using publish-subscribe code
class HomeSecurityView:
    txt=None
    btn=None
    storage = DataStorage()
    def main(self):
        self.lbl = Label('Iconic Home Security')
        self.lbl.show()

        self.statusScreen = Label('You have 30 seconds to enter your password')
        self.statusScreen.show()

        self.statusScreen.subscribe('onIntrusion', self.notifyAuthorities)
        self.statusScreen.subscribe('onAuthorizedEntry', self.notifySuccessfulEntry)

        self.txt = TextInput('Password')
        self.txt.show()

        self.btn = Button('Click me')
        self.btn.show()
        self.btn.subscribe('onClick', self.checkPassword)

        # Trigger clicking event of the button
        PublishSubscribe.eventNotifier.triggerEvent('onClick')


    def checkPassword(self):
        if self.txt.value == self.storage.getPassword():
            self.btn.publish('onAuthorizedEntry')

        else:
            self.btn.publish('onIntrusion')

    def notifyAuthorities(self):
        self.statusScreen.setVal('Intruder detected! Authorities have been notified')
        self.statusScreen.show()

    def notifySuccessfulEntry(self):
        self.statusScreen.setVal('Welcome to Tamirat\'s residence!')
        self.statusScreen.show()



x = HomeSecurityView()
x.main()
