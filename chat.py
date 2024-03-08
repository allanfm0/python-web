import flet as ft


def main(page):
    text = ft.Text("HashZap")

    chat = ft.Column()

    def enviar_menssgem_tunel(message):
        print(message)
        text_message = ft.Text(message)
        chat.controls.append(text_message)
        page.update()

    page.pubsub.subscribe(enviar_menssgem_tunel)

    def to_send(send):
        print("Enviar mensagem")
        page.pubsub.send_all(f"{user_name.value}: {message.value}")

        message.value = ""

        page.update()

    message = ft.TextField(label="Digite sua mensagem...", on_submit=to_send)
    send_button = ft.ElevatedButton("Send", on_click=to_send)
    line_send = ft.Row([message, send_button])

    def enter_chat(enter):
        popup.open = False
        page.remove(start_button)
        page.remove(text)

        page.add(chat)
        page.pubsub.send_all(f"{user_name.value} entrou no chat...")

        page.add(line_send)
        page.update()

    title_popup = ft.Text("Bem vindo ao HashZap")
    user_name = ft.TextField(label="Escreva o seu nome no chat!")
    enter_button = ft.ElevatedButton("Entrar no chat", on_click=enter_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=title_popup,
        content=user_name,
        actions=[enter_button]
    )

    def open_popup(click):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Start Chat!", on_click=open_popup)

    page.add(text)
    page.add(start_button)


ft.app(target=main, view=ft.WEB_BROWSER)
