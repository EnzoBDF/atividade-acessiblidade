from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
import json
import time
import os

# Lista dos sites
sites = {
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "fitgirl_repacks": "https://fitgirl-repacks.site",
    "portal_unisenai": "https://unisenaisc.com.br",
    "ufsc": "https://ufsc.br"
}

# Pasta onde os JSONs serão salvos
output_dir = "relatorios_acessibilidade"
os.makedirs(output_dir, exist_ok=True)

# Configuração do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

try:
    for nome, url in sites.items():
        print(f"\nAnalisando: {nome} -> {url}")
        driver.get(url)

        # Espera alguns segundos para a página carregar
        time.sleep(5)

        axe = Axe(driver)
        axe.inject()

        # Executa a análise
        results = axe.run()

        # Salva o resultado em JSON
        output_path = os.path.join(output_dir, f"{nome}_acess.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)

        print(f"Relatório salvo em: {output_path}")

finally:
    driver.quit()
    print("\nNavegador fechado.")