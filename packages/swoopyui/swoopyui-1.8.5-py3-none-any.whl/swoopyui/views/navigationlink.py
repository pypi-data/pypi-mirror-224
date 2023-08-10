from ..tools.on_action import on_view_action




class NavigationLink (object):
    """A view that controls a navigation presentation."""
    def __init__(self, title:str="Navigate", is_presented:bool = False, on_navigate=None) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.on_navigate = on_navigate
        self.__is_presented = is_presented
        self.__title = title

        self.__subviews = []
        self.__skinviews = []
    
    def get_dict_content (self):
        all_sub_views = []
        all_skin_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        
        for skv in self.__skinviews:
            all_skin_views.append(skv.get_dict_content())
        
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "NavigationLink",
            "title" : self.__title,
            "is_presented" : self.__is_presented,
            "sub_views" : all_sub_views,
            "skin_views" : all_skin_views
        }
    
    def respown (self, new_id=None, mother_view=None, parent=None):
        if new_id == None: return
        if mother_view == None: return
        if parent == None: return

        if self.__id == None:
            self.__id = new_id
            self.__last_view_id = new_id
        
        if self.__mother_view == None:
            self.__mother_view = mother_view
        
        if self.__parent_view == None:
            self.__parent_view = parent
    
    def add (self, *sub_view):
        """Add sub-views to the page the the user will be navigate to using this linker."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
    
    def add_skin_view (self, *skin_view):
        """Add a skin-view, its a sub-view that will be a part of the navigationLink look."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for skv in skin_view:
            skv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__skinviews.append(skv)
    
    def view_action (self, action_data):
        action_name = action_data['action_name']
        if action_name == "on_navigate":
            on_view_action(self.on_navigate, [self])
    
    def update (self):
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
        
        self.__parent_view.update()

    @property
    def id (self):
        return self.__id
    

    @property
    def title (self):
        return self.__title
    
    @title.setter
    def title (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__title = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    

    @property
    def is_presented (self):
        return self.__is_presented
    
    @is_presented.setter
    def is_presented (self, value:bool):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__is_presented = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id