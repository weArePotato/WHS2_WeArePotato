# ca-bucky-client

A client-side http client

## Features

- Server & Client side
- ES6 syntax, managed with Prettier + Eslint and Stylelint
- Unit testing via Jest

## Install

```sh
yarn add ca-bucky-client
// or
npm install ca-bucky-client
```

### Usage
```js
import {client} from 'ca-bucky-client';
import {useEffect} from 'react';

const App = () => {
  const [state, setState] = useState(null);
  useEffect(async () => {
    const data = await client.get('/my-url');
    setState(data);
  }, []);
  
  return <div>{state && <span>{state.data}</span>}</div>;
};
```
