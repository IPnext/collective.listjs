from zope.interface import Interface, implements
from zope import schema

from Products.Five import BrowserView
from Products.ATContentTypes.interface import IATTopic

class IListJsEnabledFolderView(Interface):
    """A List.js enabled folder view
    """
    # Item list as iterable Products.CMFPlone.PloneBatch.Batch object
    contents = schema.Object(Interface)
    
class ListJsEnabledFolderView(BrowserView):
    """An Plone implementation of a List.js folder View,
    with AJAX niceness.
    """
    
    implements(IListJsEnabledFolderView)

    def query(self, start, limit, contentFilter):
        """ Make catalog query for the folder listing.
    
        @param start: First index to query
    
        @param limit: maximum number of items in the batch
    
        @param contentFilter: portal_catalog filtering dictionary with index -> value pairs.
    
        @return: Products.CMFPlone.PloneBatch.Batch object
        """
    
        # Batch size
        b_size = limit
    
        # Batch start index, zero based
        b_start = start
    
        # We use different query method, depending on
        # whether we do listing for topic or folder
        if IATTopic.providedBy(self.context):
            # ATTopic like content
            # Call Products.ATContentTypes.content.topic.ATTopic.queryCatalog() method
            # This method handles b_start internally and
            # grabs it from HTTPRequest object
            return self.context.queryCatalog(contentFilter, batch=True, b_size=b_size)
        else:
            # Folder or Large Folder like content
            # Call CMFPlone(/skins/plone_scripts/getFolderContents Python script
            # This method handles b_start parametr internally and grabs it from the request object
            return self.context.getFolderContents(contentFilter, batch=True, b_size=b_size)
        
    def __call__(self):
        """ Render the content item listing.
        """

        # How many items is one one page
        limit = 100

        # What kind of query we perform?
        filter = {}

        # Read the first index of the selected batch parameter as HTTP GET request query parameter
        start = self.request.get("b_start", 0)

        # Perform portal_catalog query
        self.contents = self.query(start, limit, filter)

        # Return the rendered template (productcardsummaryview.pt), with content listing information filled in
        return self.index()