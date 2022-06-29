from console_game import Console_Game
from score import Score
from hand import Hand

def main():
    hand = Hand()
    hand.roll_hand()
    score = Score()
    view = Console_Game(score)
    view.draw_hand(hand.hand)
    view.draw_score_sheet()


if __name__ == "__main__":
    main()
