from kivy.uix.screenmanager import (
    NoTransition,
    ScreenManager,
    SlideTransition,
    RiseInTransition,
    FallOutTransition,
    CardTransition,
    SwapTransition,
    FadeTransition,
    WipeTransition
)

TRANSITIONS_LIST = {
    'N': NoTransition,
    'S': SlideTransition,
    'R': RiseInTransition,
    'F': FallOutTransition,
    'C': CardTransition,
    'W': WipeTransition,
    'Sw': SwapTransition,
    'Fa': FadeTransition,
}

BACK_DIRECTION = {
    'left': 'right',
    'right': 'left',
    'lr': 'rl',
    'rl': 'lr'
}


class NavigationManager(ScreenManager):
    pages = []
    anim_trans = []

    def push(self, page, direction='left'):
        self.pages.append(self.current)
        try:
            self.transition.direction = 'left'
        except:
            self.transition.direction = 'lr'
        self.anim_trans.append([self.transition, self.transition.direction])
        self.current = page

    def _pop(self):
        if len(self.pages) > 0:
            back_page = self.pages[-1]
            del self.pages[-1]
            self.current = back_page
            return True
        else: quit()

    def pop(self):
        if self.anim_trans:
            conf = self.anim_trans[-1]
            self.transition = conf[0]
            try:
                self.transition.direction = BACK_DIRECTION.get(conf[1], 'right')
            except: pass
            del self.anim_trans[-1]
        return self._pop()

    def goto(self, page, transition='S', **props):
        _screen = self.get_screen(page)
        for prop in props:
            setattr(_screen, prop, props.get(prop))
        _transition = TRANSITIONS_LIST.get(transition, SlideTransition)
        self.transition = _transition()
        self.push(page)
        self.transition = SlideTransition()
