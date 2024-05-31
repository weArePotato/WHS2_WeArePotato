# Título

Este pacote capitaliza corretamente seus títulos conforme [O Manual de Estilo de Chicago](https://marcos.com). Além disso, todos os
Os nomes dos produtos da Vercel também são capitalizados corretamente.

## Uso

Primeiramente, instale o pacote:

```bash
fio adicionar título
```

Em seguida, carregue-o e converta qualquer entrada:

```js
const title = require('proc-title')

title('tHe cHicaGo maNual oF StyLe')

// Vai resultar em:
// "O Manual de Estilo de Chicago"
```

Você pode até passar palavras que devem ser maiúsculas conforme especificado:

```js
title('FaCEbook is great', {
  special: [ 'facebook' ]
})

// Vai resultar em:
// "facebook é ótimo"
```