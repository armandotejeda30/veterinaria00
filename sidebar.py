
# Modulos
import flet
from flet import *
from functools import partial
import time

# Clase sidebar
class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()
    
    # highlight hover over the icons
    def HighLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = "white10"
            e.control.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color='white'
            e.control.content.controls[1].color='white'
            e.control.content.update()
    
    def UserData(self, initials:str, name:str, description:str):
        # user info
        return Container(
            content=Row(
                controls=[
                    Container(
                        width = 42,
                        height = 42,
                        bgcolor = "blue",
                        alignment = alignment.center,
                        border_radius = 60,
                        content = Text(value = initials, size = 20, weight = "bold", ),

                    ),
                    Column(
                        spacing = 1,
                        alignment = 'center',
                        controls=[
                            Text(
                                value = name,
                                size = 11,
                                weight = "bold",
                                # details for the animation (later)

                                opacity = 1, # full opacity 0 - 1
                                animate_opacity = 200 #speed of animation
                            ),
                            Text(
                                value = description,
                                size = 9,
                                weight = "w400",
                                color="white54",
                                # details for the animation (later)

                                opacity = 1, # full opacity 0 - 1
                                animate_opacity = 200 #speed of animation
                            ),
                        ]
                    )
                ]
            )
        )
        #pass
    
    # main sidebar with row and icons
    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width = 180,
            height = 45,
            border_radius = 20,
            on_hover = lambda e: self.HighLight(e),
            content = Row(
                controls = [
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white',
                        style = ButtonStyle(
                            shape = {
                                "": RoundedRectangleBorder(radius = 7),
                            },
                            overlay_color = {"": "transparent"},
                        ),
                    ),
                    Text(
                        value = text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    ),

                ]
            ),

        )

    
    def build(self):
        return Container(
            # define the dimensions and characterisitics of the retunred
            width = 200,
            height = 580,
            padding = padding.only(top=10),
            alignment = alignment.center,
            content = Column(
                controls = [
                    # sidebar icons
                    self.UserData("AD", 'Admin', 'Software Engineer'),
                    
                    # divider
                    Divider(height = 50, color="transparent"),
                    
                    self.ContainedIcon(icons.HOME, "Home"),
                    self.ContainedIcon(icons.CALENDAR_MONTH, "Calendar"),
                    self.ContainedIcon(icons.PAYMENT, "Pay"),
                    self.ContainedIcon(icons.GIF_BOX, "Services"),
                    self.ContainedIcon(icons.CHAT, "Support"),

                    Divider(height=100, color="transparent") ,
                    self.ContainedIcon(icons.EXIT_TO_APP, "Log out"),
                ]
            ),
             

            #content=None
        )

# main function
def main(page: Page):
    # size window
    page.window_height = 700
    page. window_width = 300
    #titulo
    page.title = 'SideBar'

    # Alineaciones
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    # add class to page
    page.add(
        Container(
            width=200,
            height=580,
            bgcolor='black',
            border_radius= 10,
            # animate the sidebar
            animate = animation.Animation(500, "decelerate"),
            # aling inner contents
            alignment=alignment.center,
            padding = 10,
            content = ModernNavBar()
        )
    )

    page.update()

# run
if __name__ == "__main__":
    flet.app(target=main)

