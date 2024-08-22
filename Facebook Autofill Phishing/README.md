
# Phishing por Autofill

Este repositório demonstra uma vulnerabilidade de phishing por autofill em navegadores modernos. Mostra como mesmo os navegadores mais recentes podem ser suscetíveis a esse tipo de ataque básico, que já existe há muitos anos.

![Exemplo de Phishing por Autofill](Facebook Autofill Phishing\demo-web.mp4)

## Por Que Esse Ataque Funciona

Muitos navegadores modernos oferecem recursos de preenchimento automático para melhorar a conveniência do usuário, preenchendo automaticamente os campos do formulário com dados salvos. No entanto, essa conveniência pode ser explorada devido a:

- **Campos Ocultos**: Os atacantes podem ocultar campos de entrada em uma página da web, que são preenchidos automaticamente sem o conhecimento do usuário.
- **Confiança no Preenchimento Automático**: Os usuários costumam confiar que o preenchimento automático só preencherá campos visíveis, sem saber que campos ocultos também podem ser preenchidos.

## Como Esse Ataque Funciona

Esse ataque explora o recurso de preenchimento automático dos navegadores. Aqui estão os principais passos envolvidos:

1. **Formulário Web Criado**: O atacante cria um formulário web com campos visíveis e ocultos.
2. **Interação do Usuário**: O usuário visita o site malicioso e interage com os campos visíveis do formulário.
3. **Acionamento do Preenchimento Automático**: O recurso de preenchimento automático do navegador preenche automaticamente tanto os campos visíveis quanto os ocultos com dados salvos do usuário.
4. **Extração**: Os campos ocultos capturam informações sensíveis sem o conhecimento do usuário, que são então enviadas para o atacante.

## Imagem

Veja abaixo um exemplo visual que ilustra como o formulário pode ser estruturado:

![Exemplo de Phishing por Autofill](https://github.com/0dayCTF/Autofill_Danger/assets/44453666/ab888f01-8413-4553-a413-73b75751adca)

## Tecnologias Utilizadas

Aqui estão as principais tecnologias usadas para criar o exemplo de phishing por autofill:

- **HTML**
  ![HTML Logo](https://img.icons8.com/ios/50/000000/html-5.png)
  
- **CSS**
  ![CSS Logo](https://img.icons8.com/ios/50/000000/css3.png)
  
- **JavaScript**
  ![JavaScript Logo](https://img.icons8.com/ios/50/000000/javascript.png)
  
- **Netlify**
  ![Netlify Logo](https://img.icons8.com/ios/50/000000/netlify.png)

## Referências

Inspirado por Viljami Kuosmanen - [GitHub](https://github.com/anttiviljami/browser-autofill-phishing)

---

### Explicação dos Componentes

#### **1. Formulário Web Criado**
O atacante cria um formulário com campos de entrada visíveis e ocultos. Os campos ocultos são estilizados para não serem visíveis ao usuário, mas ainda assim são preenchidos pelo navegador.

#### **2. Interação do Usuário**
O usuário interage apenas com os campos visíveis, sem perceber que há campos ocultos na mesma página.

#### **3. Acionamento do Preenchimento Automático**
Quando o navegador preenche automaticamente os campos do formulário com dados salvos (como e-mail, nome, etc.), ele preenche também os campos ocultos, que capturam essas informações sem que o usuário perceba.

#### **4. Extração**
Os dados preenchidos nos campos ocultos são enviados para o servidor controlado pelo atacante, geralmente através de uma requisição de formulário ou via JavaScript.

### **Sugestões para Proteção**

- **Revisar o HTML**: Sempre verifique o código HTML de páginas em que você insere informações sensíveis.
- **Desativar Preenchimento Automático**: Desative o preenchimento automático para sites não confiáveis.
- **Educação e Conscientização**: Esteja ciente de como os formulários são estruturados e como dados podem ser manipulados.

Espero que esta explicação detalhada e o conteúdo adicional ajudem a entender melhor o phishing por autofill e como ele pode afetar a segurança online. Se precisar de mais informações ou tiver dúvidas, sinta-se à vontade para perguntar!

--- 

Este documento utiliza ícones para tornar as seções sobre as tecnologias mais visuais e intuitivas. Adapte conforme necessário para o seu público ou objetivo específico.