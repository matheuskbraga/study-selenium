from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# ==========================================
# 1. NAVEGAÇÃO E HISTÓRICO
# ==========================================

# Acessa uma URL
driver.get("https://www.google.com")

# Recarrega a página atual (F5)
driver.refresh()

# Volta para a página anterior no histórico
driver.back()

# Avança para a próxima página no histórico
driver.forward()

# ==========================================
# 2. GERENCIAMENTO DE JANELAS E TELAS
# ==========================================

# Maximiza a janela para ocupar a tela com bordas normais
driver.maximize_window()

# Coloca o navegador em modo tela cheia total (equivalente a F11)
driver.fullscreen_window()

# Minimiza a janela do navegador
driver.minimize_window()

# Define dimensões específicas para a janela (largura, altura)
driver.set_window_size(1280, 720)

# ==========================================
# 3. METADADOS E INFORMAÇÕES DA PÁGINA
# ==========================================

# Retorna a URL atual exibida na barra de endereços (propriedade, sem parênteses)
url = driver.current_url

# Retorna o título da aba atual da página (propriedade, sem parênteses)
titulo = driver.title

# Retorna o código-fonte HTML completo da página renderizada
html_fonte = driver.page_source

# ==========================================
# 4. CAPTURAS DE TELA (SCREENSHOTS)
# ==========================================

# Tira um print e salva diretamente em um arquivo de imagem
driver.get_screenshot_as_file("screens.png")
# Alternativa equivalente mais concisa:
# driver.save_screenshot("screens.png")

# Tira print apenas de um elemento específico (ex: uma tabela ou card)
# elemento = driver.find_element(By.ID, "tabela-dados")
# elemento.screenshot("elemento.png")

# ==========================================
# 5. GERENCIAMENTO DE ABAS E JANELAS
# ==========================================

# Identificador exclusivo da aba/janela atual em foco
aba_atual = driver.current_window_handle

# Lista com os identificadores de todas as abas abertas
todas_abas = driver.window_handles

# Alterna o controle do Selenium para outra aba
# driver.switch_to.window(todas_abas[-1])

# Abre uma nova aba em branco e já move o foco para ela
driver.switch_to.new_window("tab")

# Abre uma nova janela independente e move o foco para ela
# driver.switch_to.new_window("window")

# ==========================================
# 6. ENCERRAMENTO E LIMPEZA
# ==========================================

# Fecha apenas a aba ou janela que está em foco no momento
driver.close()

# Encerra todas as abas, fecha o navegador e encerra o processo do chromedriver no sistema operacional
driver.quit()

# ==========================================
# 7. INTERAÇÃO COM CAMPOS DE TEXTO E INPUTS
# ==========================================

# Localiza o elemento de entrada (input ou textarea)
campo_busca = driver.find_element(By.NAME, "q")

# Digita texto no campo
campo_busca.send_keys("Selenium Python")

# Envia teclas especiais (Enter, Tab, Espaço, Backspace, etc.)
campo_busca.send_keys(Keys.RETURN)

# Limpa o texto contido no campo de entrada
campo_busca.clear()

# ==========================================
# 8. LEITURA DE DADOS DOS ELEMENTOS
# ==========================================

# Lê o texto visível renderizado entre as tags (ex: <span>Texto</span>)
texto_visivel = campo_busca.text

# Lê o valor atual digitado em um input (campos <input> guardam o texto no atributo 'value')
valor_digitado = campo_busca.get_attribute("value")

# Lê qualquer outro atributo HTML da tag (ex: href, class, placeholder, id, name)
placeholder_texto = campo_busca.get_attribute("placeholder")

# Lê propriedades calculadas do DOM (útil para campos dinâmicos onde get_attribute pode falhar)
propriedade_valor = campo_busca.get_property("value")

# Lê propriedades de estilo CSS aplicadas ao elemento
cor_do_texto = campo_busca.value_of_css_property("color")

# ==========================================
# 9. CLIQUES E SUBMISSÃO
# ==========================================

# Clica em um botão, link ou qualquer elemento clicável
botao_enviar = driver.find_element(By.ID, "btn-submit")
botao_enviar.click()

# Envia um formulário diretamente a partir de um input interno (dispensa clicar no botão submit)
campo_busca.submit()

# ==========================================
# 10. VERIFICAÇÃO DE ESTADO DO CAMPO
# ==========================================

# Retorna True se o elemento está visível na tela
esta_visivel = campo_busca.is_displayed()

# Retorna True se o campo está habilitado para edição (não possui disabled)
esta_habilitado = campo_busca.is_enabled()

# Retorna True se um checkbox ou radio button está marcado
esta_marcado = campo_busca.is_selected()