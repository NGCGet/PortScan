# 🔍 Simple Python Port Scanner

Um scanner de portas TCP leve, simples e funcional desenvolvido em Python. O script permite verificar rapidamente se portas específicas em um determinado host (domínio ou IP) estão abertas.

---

## 🚀 Recursos

- **Varredura Personalizada:** Defina manualmente as portas que deseja analisar via linha de comando.
- **Portas Padrão:** Varredura automática das portas mais comuns (HTTP, HTTPS, SSH, FTP, MySQL, etc.) caso nenhuma porta seja especificada.
- **Gerenciamento Seguro de Recursos:** Utiliza o contexto `with` para garantir que as conexões de socket sejam encerradas adequadamente após cada teste.
- **Tratamento de Exceções:** Lida com falhas de resolução de DNS e erros de timeout sem interromper a execução abruptamente.

---

## 🛠️ Pré-requisitos

- **Python 3.6** ou superior instalado no seu sistema.
- Não requer a instalação de bibliotecas externas (utiliza apenas os módulos nativos `socket` e `sys`).

---

## 📥 Como Baixar e Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/NGCGet/PortScan.git](https://github.com/NGCGet/PortScan.git)
   cd PortScan
   python portscan.py google.com 22,80,443,8080
