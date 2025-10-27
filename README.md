# projeto-2-bootcamp-dio

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

🧠 #Keylogger Simulado:  programar captura de teclas em arquivo .txt, torná-lo mais furtivo e implementar envio automático por e-mail.

Uso: material resumido para README de repositório GitHub destinado a treinamento/estudo em cibersegurança.
Importante: não contém código nem instruções para criação/ocultação de keyloggers ou exfiltração de dados — foca em ética, defesa e boas práticas.

🎯 Objetivo

Fornecer um panorama claro e responsável sobre captura de teclas (keylogging) para fins educativos: quando é legítimo, riscos legais/éticos e orientações para coleta segura, detecção e mitigação.

✨ Destaques (resumo rápido)

Legitimidade: só com autorização explícita (ex.: estudos UX, acessibilidade, pesquisa autorizada).

Privacidade: minimize dados, anonimize sempre que possível, evite campos sensíveis (senhas, cartões).

Consentimento: documentado e revogável; políticas claras sobre finalidade e retenção.

Alternativas seguras: métricas agregadas, dados sintéticos, APIs oficiais com permissões.

Segurança dos dados: criptografia em trânsito e em repouso, controle de acesso, logs de auditoria.

Detecção & Resposta: EDR/antivírus, whitelisting, monitoramento de processos e plano de resposta a incidentes.

✅ Checklist rápido (use no seu README)

 Aprovação legal / compliance obtida

 Consentimento informado documentado pelos participantes

 Apenas dados mínimos são coletados (minimização)

 Campos sensíveis são mascarados / excluídos

 Criptografia e controles de acesso aplicados

 Política de retenção e exclusão definida

 Ambiente de teste isolado (VM/sandbox) com snapshot

🛡️ Boas práticas para treinamentos e laboratórios

Execute testes apenas em ambientes isolados (VMs/sandboxes).

Use dados fictícios sempre que possível.

Forneça um termo de consentimento claro aos participantes.

Documente passos, coleta e duração — mantenha trilhas de auditoria.

Ao demonstrar detecção, mostre como ferramentas (EDR/AV) registram e respondem ao comportamento suspeito, sem mostrar como criar malware.

🔍 Foco em defesa — O que ensinar no treinamento

Identificação de sinais suspeitos: processos desconhecidos, hooks de entrada, tráfego de rede inesperado.

Controles preventivos: whitelisting de aplicações, privilégios mínimos, políticas de instalação restrita.

Resposta a incidentes: isolamento do host, preservação de evidências, restauração de backups e notificação.

Auditoria contínua: logging, revisão de permissões e varreduras regulares.
