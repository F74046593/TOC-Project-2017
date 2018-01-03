from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'u1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'u2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'u3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'mumi'

    def on_enter_state1(self, update):
        update.message.reply_text("one pass,one fail")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("two pass")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("I hope I can pass.")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_photo(open("img/mumi.jpg","rb"))
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

