Feature: Gerenciamento de pedidos

  Scenario: Adicionar um novo pedido
    Given que eu tenho os detalhes do pedido
    When eu faço o cadastro de um pedido
    Then eu devo receber uma resposta com o código de status 201

  Scenario: Consultar um pedido
    When eu faço a consulta dos pedidos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um pedido existente
    Given que eu tenho os detalhes atualizados do pedido
    When eu faço uma atualização de um pedido
    Then eu devo receber uma resposta com o código de status 200
