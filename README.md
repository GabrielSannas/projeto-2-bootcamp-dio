##🛡️ Treinamento: 

##⚠️ Uso estritamente em laboratório — conteúdo para treinamento/estudo em cibersegurança.
Não contém código nem instruções para criação de keyloggers furtivos ou exfiltração. Siga sempre leis, políticas internas e obtenha consentimento explícito.

#Documentação do Teste — Ransomware Simulado (criação de arquivos de teste, criptografia/descriptografia e mensagem de “resgate”)

Aviso de responsabilidade / uso ético
Este documento descreve um teste educativo que implementa um ransomware simulado apenas em ambiente controlado (máquina virtual, sandbox ou pasta dedicada). Não execute em sistemas produtivos nem em máquinas de terceiros. Faça snapshot da VM antes de testar e não comite chaves/artefatos sensíveis.

Objetivo

Documentar passo a passo um teste prático que:

Cria arquivos de teste isolados.

Implementa um script Python que criptografa e descriptografa os arquivos na pasta de teste usando criptografia simétrica (Fernet).

Gera uma mensagem de “resgate” (ransom note) explicativa como arquivo .txt.

Fornecer procedimentos de verificação, rollback e boas práticas de segurança.

Pré-requisitos

Python 3.8+ instalado.

Ambiente de teste isolado (VM/sandbox). Recomenda-se snapshot antes de começar.

Dependências Python:

cryptography (pip install cryptography)

Espaço em disco para criar arquivos de teste.

##🧠 Keylogger Simulado:  programar captura de teclas em arquivo .txt, torná-lo mais furtivo e implementar envio automático por e-mail.

Uso: material resumido para README de repositório GitHub destinado a treinamento/estudo em cibersegurança.
Importante: não contém código nem instruções para criação/ocultação de keyloggers ou exfiltração de dados — foca em ética, defesa e boas práticas.

##🎯 Objetivo

Fornecer um panorama claro e responsável sobre captura de teclas (keylogging) para fins educativos: quando é legítimo, riscos legais/éticos e orientações para coleta segura, detecção e mitigação.

##✨ Destaques (resumo rápido)

Foi criado um scipt para mapeamento de  teclas e armazenamento em arquivo log de forma temporaria keylogger.py para execução em segundo plano devevomos renomear para pyw, assim fica rodando escondido e automatico por um tempo

segundo passo foi criar um email de teste para esses mapeamentos de teclas serem enviados via email a cada 60 segundos e de forma automatica com python o nome do arquivo utlizado keylogger_email, deixei 2 imagens do resultado

##🛡️ Resumo — Medidas de Defesa contra Keyloggers e Ransomwares

##🔒 Objetivo: apresentar de forma resumida e educativa as principais estratégias de prevenção e defesa contra keyloggers e ransomwares em treinamentos de cibersegurança.

##💀 Ameaças

Keylogger: registra teclas digitadas para roubar senhas e dados.

Ransomware: criptografa arquivos e exige pagamento (resgate).

##🧰 Principais Medidas de Defesa
##🔹 Antivírus / Antimalware

Detecta e bloqueia ameaças em tempo real.

Mantenha atualizado e habilite varredura heurística.

##🔹 Firewall

Controla conexões de rede.

Bloqueie portas e domínios suspeitos; ative logs.

##🔹 Sandboxing

Testa arquivos em ambiente isolado (VM).

Ideal para analisar comportamento suspeito com segurança.

##🔹 Conscientização do Usuário

Treinar sobre phishing, links falsos e engenharia social.

Incentivar senhas fortes e uso de autenticação multifator.

##🧱 Outras Defesas Importantes

Backup seguro: cópias offline e na nuvem.

Patching: mantenha sistemas atualizados.

Privilégios mínimos: limitar acessos.

Monitoramento contínuo: use SIEM/EDR para detectar comportamentos anormais.

##🚑 Resposta a Incidentes

Isolar o dispositivo afetado.

Preservar logs e evidências.

Restaurar backup limpo.

Comunicar equipe de segurança.

Revisar políticas de prevenção.

##🧠 Conclusão

A defesa eficaz depende da combinação de tecnologia, processos e conscientização humana.
Segurança é um processo contínuo, não uma ação única.
