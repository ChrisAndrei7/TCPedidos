<h1 align="center"> TCFoodSystem - Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto está em desenvolvimento como atividade do Tech Challenge para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de pedidos</b>
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:8002/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appPedidos`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbPedidos`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "pedidos" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appPedidos/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o pagamento: http://localhost:8002/pedidos/create

2 - Consultar pagamentos: http://localhost:8002/pedidos/

3 - Atualizar pagamento: http://localhost:8002/pedidos/update/{id_do_pedido}

4 - Deletar pagamento: http://localhost:8002/pedidos/delete/{id_do_pedido}

# Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento. 
