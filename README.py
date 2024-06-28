#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `vlc` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `vlc` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/use the `vlc` on `Linux Ubuntu`._

# ## Descrição [1][2]
# 
# ### `vlc`
# 
# O `vlc`, ou VideoLAN Client, é um popular reprodutor de mídia de código aberto que é amplamente utilizado para reproduzir uma variedade de formatos de áudio e vídeo em várias plataformas, incluindo Windows, macOS, Linux, Android e iOS. O `vlc` é conhecido por sua capacidade de lidar com uma ampla gama de tipos de arquivo, tornando-o uma escolha versátil para assistir a vídeos e ouvir música. Além disso, ele oferece recursos avançados, como suporte a legendas, streaming de mídia, ajustes de áudio e vídeo em tempo real e a capacidade de reproduzir mídia de discos ópticos, dispositivos de armazenamento externo e streaming online. O VLC também é apreciado por sua interface de usuário simples e intuitiva, além de ser de código aberto, o que significa que sua comunidade de desenvolvedores pode contribuir para aprimorar e expandir suas funcionalidades. É uma escolha popular para aqueles que buscam uma solução de reprodução de mídia confiável e versátil.

# ## 1. Configurar/Instalar/usar o `vlc` no `Kali Ubuntu` [1]
# 
# Para instalar o `vlc` no `Linux Ubuntu`, você pode usar o gerenciador de pacotes `snap`. Siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Instalar o VLC:** Após a atualização, instale o VLC usando o seguinte comando: `sudo snap install vlc`
# 
#     Esse comando instalará a versão mais recente do VLC disponível nos repositórios do `Linux Ubuntu`.
# 
# 4. **Executar o VLC:** Uma vez instalado, você pode iniciar o VLC a partir do terminal digitando `vlc` ou encontrá-lo no menu de aplicações.
# 
# **Notas Adicionais:**
# 
# - **Permissões:** Como o `Linux Ubuntu` é frequentemente usado com privilégios de superusuário, tenha cuidado ao instalar software e ao conceder permissões.
# 
# - **Repositórios de Software:** Se você enfrentar problemas ao instalar o VLC, certifique-se de que os repositórios de software do `Linux Ubuntu` estejam configurados corretamente.
# 
# - **Dependências:** O gerenciador de pacotes `apt` geralmente resolve as dependências automaticamente, mas esteja atento a mensagens de erro relacionadas a dependências faltantes.
# 
# Se houver algum erro durante a instalação, a mensagem de erro específica pode ajudar a identificar a solução.

# ### 1.1 Código completo para configurar/instalar
# 
# Para configuração/instalar o `vlc` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo snap install vlc -y
#     vlc
#     ```

# ## 2. Criar um atalho manualmente
# 
# 1. **Criar um Atalho Manualmente:** Se não houver uma entrada para o VLC, você pode criar uma manualmente. Use um editor de texto para criar um arquivo chamado `vlc.desktop` em `~/.local/share/applications/` com o seguinte conteúdo:
# 
#     ```
#     [Desktop Entry]
#     Name=VLC Media Player
#     Comment=Play your media
#     Exec=vlc
#     Icon=vlc
#     Terminal=false
#     Type=Application
#     Categories=AudioVideo;Player;Recorder;
#     ```
# 
# 2. **Atualizar o Cache do Menu de Aplicações:** Às vezes, é necessário atualizar o cache do menu de aplicações para que as novas entradas apareçam. Isso pode ser feito com: `sudo update-desktop-database`
# 
# Se nenhuma dessas soluções funcionar, pode ser necessário investigar questões mais específicas do seu ambiente de desktop ou configurações do `Linux Ubuntu`.

# ## Referências
# 
# [1] OPENAI. ***Instalar vlc noLinux Ubuntu:*** https://chat.openai.com/c/09d564cf-b2d8-49a1-a461-b14a4680c49a (texto adaptado). ChatGPT. Acessado em: 11/12/2023 12:11.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 11/12/2023 12:11.
