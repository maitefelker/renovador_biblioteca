# renovador_biblioteca

Esta ferramenta permite automatizar a renovação dos livros retirados nas Bibliotecas da UFSM.
(This tool makes it possible to automate book lease renewals of books taken from UFSM's libraries.)

### Como funciona?
Usa um script em python com a biblioteca Selenium para entrar no site, realizar o login do usuário e renovar os livros que estão na data ideal de renovação.

### Como usar?
Para usar, dê fork nesse repositório, adicione sua matrícula e senha nos secrets do repositório resultante (USER e SENHA) e, após, no menu "Actions", ative os workflows. Dessa maneira, a ferramenta funcionará, e, mesmo tendo o repositório como público, suas credenciais continuarão privadas.
