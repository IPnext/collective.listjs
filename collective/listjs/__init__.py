from zope.i18nmessageid import MessageFactory

_ = subscriberdataMessageFactory = MessageFactory('collective.listjs')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
