import flet as ft
from datetime import date, timedelta


quartos = {
    "Simples": {"preco": 100, "disponiveis": 5},
    "Duplo": {"preco": 180, "disponiveis": 3},
    "Luxo": {"preco": 300, "disponiveis": 2},
}


disponibilidade = {
    (date.today() + timedelta(days=i)).isoformat(): quartos.copy()
    for i in range(7)  # Próximos 7 dias
}


def main(page: ft.Page):
    page.title = "Reserva de Quartos"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.ALWAYS

    resultado = ft.Text("")
    lista_quartos = ft.Dropdown(
        label="Tipo de Quarto",
        options=[ft.dropdown.Option(q) for q in quartos],
    )
    calendario = ft.Dropdown(
        label="Data da Reserva",
        options=[ft.dropdown.Option(d) for d in disponibilidade],
    )

    def reservar(e):
        tipo = lista_quartos.value
        data = calendario.value

        if not tipo or not data:
            resultado.value = "Por favor, selecione o quarto e a data."
        elif disponibilidade[data][tipo]["disponiveis"] > 0:
            disponibilidade[data][tipo]["disponiveis"] -= 1
            preco = disponibilidade[data][tipo]["preco"]
            resultado.value = f"Reserva confirmada!\nQuarto: {tipo}\nData: {data}\nPreço: R$ {preco},00"
        else:
            resultado.value = f"Desculpe, não há mais quartos '{tipo}' disponíveis em {data}."
        
        page.update()

    reservar_btn = ft.ElevatedButton("Reservar", on_click=reservar)

    page.add(
        ft.Text("Simulador de Reserva de Quartos", size=30, weight=ft.FontWeight.BOLD),
        lista_quartos,
        calendario,
        reservar_btn,
        resultado
    )

ft.app(target=main)
