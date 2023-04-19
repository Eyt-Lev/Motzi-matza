from src.services.visualization_service import VisualizationService


class Reasons:
    ranOutOfTime = ["You've passed 18 minuets!", "The Matzot became Hametz now!"]
    wheatCrashOver = ["The wheats to crash are over!", "You hadn't collected enough flour."]
    flourBoxesOver = ["The flour to mix is over!", "You hadn't collected enough dough."]


class EndScreen:
    @staticmethod
    def draw(reason):
        VisualizationService.draw_end_screen(reason)
