import pygame

from src.tools import is_img_mask_collide_with_mouse


class Button:
    def __init__(
            self,
            screen, x, y, img=None, hoverImage=None,
            width=None, height=None, color=None,
            font=None, textColor=None, buttonText=None, border=0,
            onclickFunction=None, onHoverFunction=None, onePress=False,
            center=True
    ):
        self.x = x
        self.y = y
        self.screen = screen
        self.onePress = onePress
        self.onclickFunction = onclickFunction
        self.onHoverFunction = onHoverFunction
        self.isImg = img is not None

        if img is not None:
            self.img = img
            self.imgRect = img.get_rect()
            self.center = center
            self.originalImg = img
            if self.center:
                self.imgRect.center = x, y
            else:
                self.imgRect.left, self.imgRect.top = x, y
            if hoverImage is not None:
                self.hoverImage = hoverImage
        else:
            self.width = width
            self.height = height
            self.buttonRect = pygame.Rect(x - width / 2, y - height / 2, width, height)
            self.buttonRect.center = (x, y)
            self.color = color
            self.font = font
            self.textColor = textColor
            self.buttonText = buttonText
            self.border = border

        self.hovered = False
        self.alreadyPressed = False

    def handleEvent(self):
        pos = pygame.mouse.get_pos()
        if self.checkForClicks(pos):
            if self.onclickFunction is not None:
                self.onclickFunction()
        if self.checkForHover(pos):
            if self.onHoverFunction is not None:
                self.onHoverFunction()

    def checkForClicks(self, mousePos):
        if not self.alreadyPressed:
            if self.isImg:
                if is_img_mask_collide_with_mouse(self.img, self.imgRect) and pygame.mouse.get_pressed()[0]:
                    self.alreadyPressed = True
                    return True
            else:
                if self.buttonRect.collidepoint(mousePos) and pygame.mouse.get_pressed()[0]:
                    self.alreadyPressed = True
                    return True
        if pygame.mouse.get_pressed()[0] == 0:
            self.alreadyPressed = False

    def checkForHover(self, mousePos):
        if self.isImg:
            hoveredNow = is_img_mask_collide_with_mouse(self.img, self.imgRect)
            if hoveredNow:
                self.img = self.hoverImage
                if not self.hovered:
                    self.hovered = True
                    return True
            else:
                self.img = self.originalImg
                self.hovered = False

        elif not self.isImg:
            hoveredNow = self.buttonRect.collidepoint(mousePos)
            if hoveredNow:
                if not self.hovered:
                    self.hovered = True
                    return True
            else:
                self.hovered = False

    def draw(self):
        self.handleEvent()
        if self.isImg:
            self.screen.blit(self.img, self.imgRect)
        else:
            pygame.draw.rect(self.screen, self.color, self.buttonRect, self.border)
            if self.font is not None:
                text_surface, rect = self.font.render(self.buttonText, self.textColor, None, size=self.width / 6)
                rect.center = self.buttonRect.center
                self.screen.blit(text_surface, rect)
