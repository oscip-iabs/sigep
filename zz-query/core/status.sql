INSERT INTO public.iabs_main_geral_status (id, cod_status, previous_status, next_status, referencia, chave, texto) VALUES (101001000, 101001000, 101002000, 101001000, 'CADASTRO INICIAL DA POSSIBILIDADE', 'CADASTRO_BASICO_NOVO', 'Cadastro básico iniciado');
INSERT INTO public.iabs_main_geral_status (id, cod_status, previous_status, next_status, referencia, chave, texto) VALUES (101002000, 101002000, 101001000, 102001000, 'CADASTRO COMPLETO INICIADO', 'CADASTRO_COMPLETO_INICIADO', 'Cadastro completo iniciado');
INSERT INTO public.iabs_main_geral_status (id, cod_status, previous_status, next_status, referencia, chave, texto) VALUES (102001000, 102001000, 101002000, 101002000, 'CADASTRO DA POSSIBILIDADE CONCLUIDO', 'CADASTRO_POSSIBILIDADE_CONCLUIDO', 'Cadastro da possibilidade completo');
INSERT INTO public.iabs_main_geral_status (id, cod_status, previous_status, next_status, referencia, chave, texto) VALUES (20101000, 20101000, 102001000, 20201000, 'POSSIBILIDADE APROVADA', 'CADASTRO_POSSIBILIDADE_APROVADO', 'Novo projeto potencial ');
INSERT INTO public.iabs_main_geral_status (id, cod_status, previous_status, next_status, referencia, chave, texto) VALUES (20201000, 20201000, 20101000, 20301000, 'CADASTRO PROJETO POTENCIAL COMPLETO', 'CADASTRO_PROJETO_POTENCIAL_CONCLUIDO', 'Cadastro do projeto potencial completo');