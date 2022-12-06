
// Vai ser executado somente após o HTML ser Exibido na Tela
window.addEventListener('load', function() {

    // Antes de chamarmos o servidor, já vamos colocar uma loading dentro dos nossos cards
    this.document.querySelector('#totallojas').innerHTML = '<div class="spinner-border spinner-border-sm" role="status"></div>';
    this.document.querySelector('#totalusuarios').innerHTML = '<div class="spinner-border spinner-border-sm" role="status"></div>';
    
    // Inicia uma comunicação Assincrona, ou seja, é carregada em paralelo ao conteudo da Aplicação.
    (async () => {
        
        // A variável response recebe o retorno do Fetch. Await aqui é para sinalizar que a função demora a responder, e que somete depois que o fetch concluir a responsa é que o response terá os dados.
        // Através do Fetch é que passamos a URL que precisamos chamar no Servidor.
        const response = await this.fetch("/homedata", {
            // Aqui declaramos os cabeçalhos necessários para informar ao servidor que esperamos um retorno JSON
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        });

        // 200 geralmente é o status que o servidor devolve para Zero Erro durante a operção.
        if (response.status === 200) {

            // A variável content recebe o retorno do response. É aqui que já temos todos os dados que o servidor nos devolveu. E já estarão dentro da variável content.
            const content = await response.json();

            // A partir daqui já podemos devolver para o HTML as infomações do Servidor! ;-)
            this.document.querySelector('#totallojas').innerHTML = content.total_associados;
            this.document.querySelector('#totalusuarios').innerHTML = content.total_usuarios;

        } else {
            // Se houve um erro durante a requisição, poderemos printar no console do JS aqui.
            console.log(response.status);
        }
    })();
});