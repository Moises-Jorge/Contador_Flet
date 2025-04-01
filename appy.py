import flet as ft

def main(page: ft.Page) -> None:
    page.title = 'My first flet App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Funcoes que serao chamadas quando os botoes forem clicados
    def aumentar(e) -> None:
        caixa_txt.value = str(int(caixa_txt.value) + 1)
        page.update()
    
    
    def diminuir(e) -> None:
        caixa_txt.value = str(int(caixa_txt.value) - 1)
        page.update()
    
    
    # Criacao dos elementos ou widgets
    btn_up = ft.IconButton(
        ft.icons.ADD,
        on_click=aumentar
    )
    
    btn_down = ft.IconButton(
        ft.icons.REMOVE,
        on_click=diminuir
    )
    
    caixa_txt = ft.TextField(
        value=0,
        width=100,
        text_align=ft.TextAlign.CENTER
    )
    
    
    # Adicao dos elementos na pagina
    page.add(
        ft.Row(
            [btn_down, caixa_txt, btn_up],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    
ft.app(target=main)