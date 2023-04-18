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
            if self.center:
                self.imgRect.center = x, y
            else:
                self.imgRect.left, self.imgRect.top = x, y

            self.hoverd = self.imgRect.collidepoint(*pygame.mouse.get_pos()) and pygame.mask.from_surface(img).get_at((pygame.mouse.get_pos()[0] - self.imgRect.x, pygame.mouse.get_pos()[1] - self.imgRect.y))
            if hoverImage is not None:
                self.hoverImage = hoverImage
        else:
            self.width = width
            self.height = height
            self.buttonRect = pygame.Rect(x - width / 2, y - height / 2, width, height)
            self.buttonRect.center = (x, y)
            self.color = color
            self.hoverd = self.buttonRect.collidepoint(pygame.mouse.get_pos())
            self.font = font
            self.textColor = textColor
            self.buttonText = buttonText
            self.border = border

        self.alreadyPressed = self.hoverd and pygame.mouse.get_pressed()[0]

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button
            if not self.alreadyPressed:
                mouse_pos = pygame.mouse.get_pos()
                if self.isImg:
                    if is_img_mask_collide_with_mouse(self.img, self.imgRect):
                        if self.onclickFunction is not None:
                            self.onclickFunction()
                else:
                    if self.buttonRect.collidepoint(mouse_pos):
                        if self.onclickFunction is not None:
                            self.onclickFunction()

        elif event.type == pygame.MOUSEMOTION:  # on hover
            pos = pygame.mouse.get_pos()
            if self.isImg:
                if is_img_mask_collide_with_mouse(self.img, self.imgRect):
                    if not self.hoverd:
                        if self.onHoverFunction is not None:
                            self.onHoverFunction()
                    self.hoverd = True
                else:
                    self.hoverd = False
            else:
                if self.buttonRect.collidepoint(pos):
                    if not self.hoverd:
                        if self.onHoverFunction is not None:
                            self.onHoverFunction()
                    self.hoverd = True
                else:
                    self.hoverd = False

    def draw(self):
        if self.isImg:
            if self.hoverd:
                img = self.hoverImage
            else:
                img = self.img
            self.screen.blit(img, self.imgRect)
        else:
            pygame.draw.rect(self.screen, self.color, self.buttonRect, self.border)
            if self.font is not None:
                text_surface, rect = self.font.render(self.buttonText, self.textColor, None, size=self.width / 6)
                rect.center = self.buttonRect.center
                self.screen.blit(text_surface, rect)
