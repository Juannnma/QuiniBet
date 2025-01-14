from app.models.raffle import Raffle
from marshmallow import fields, Schema, post_load, ValidationError

class RaffleSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.String(required=True)
    time = fields.String(required=True)
    prize = fields.String(required=True)
    card_win = fields.String(load_only=True, allow_none=True)
    winners = fields.String(load_only=True, allow_none=True)

    @post_load
    def make_raffle(self, data, **kwargs):
        card_win = data.get('card_win')
        winners = data.get('winners')

        # Realizar la validación si los campos son proporcionados
        if card_win is not None and winners is not None:
            if card_win.strip() == "":
                raise ValidationError('Field "card_win" may not be empty.')

            if winners.strip() == "":
                raise ValidationError('Field "winners" may not be empty.')

        return Raffle(**data)
