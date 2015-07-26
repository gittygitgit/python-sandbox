#!/usr/bin/python

import HTMLParser

class MyParse(HTMLParser.HTMLParser):
    def __init__(self):
        #super() does not work for this class
        HTMLParser.HTMLParser.__init__(self)
        self.tag_stack = []
        self.attr_stack = []

    def handle_endtag(self, tag):
        #take the tag off the stack if it matches the next close tag
        #if you are expecting unmatched tags, then this needs to be more robust
        if self.tag_stack[len(self.tag_stack)-1][0] == tag:
            self.tag_stack.pop()

    def handle_data(self, data):
        #'data' is the text between tags, not necessarily
        #matching tags
        #this gives you a link to the last tag
        tstack = self.tag_stack[len(self.tag_stack)-1]
        #do something with the text
           
    def handle_starttag(self, tag, attrs):
        #add tag to the stack
        self.tag_stack.append([tag, attrs])
        #if this tag is a link
        if tag =="a":
            #these next few lines find if there is a hyperlink in the tag
            tloc = map(lambda x: 1 if x[0]=='href' else 0,attrs)
            try:
                #did we find any hyperlinks
                attr_loc = tloc.index(1)
            except:
                pass
            # attr_loc only exists if we found a hyperlink
            if vars().has_key('attr_loc'):
                #append to the last item in the stack the location of the hyperlink
                #note, this does not increase the length of the stack
                #as we are putting it inside the last item on the stack
                self.tag_stack[len(self.tag_stack)-1].append(attr_loc)
               
                #now we can do what we need with the hyperlink
