import React, { Component } from 'react'
import { Provider as StoreProvider } from 'react-redux'
import App from 'grommet/components/App'
import Box from 'grommet/components/Box'
import '../redux-modules'
import SampleComponent from './sample/SampleComponent.jsx'

export class MainComponent extends Component {

  constructor(props) {
    super(props)
    this.state = props
  }

  render() {
    return (
      <StoreProvider store={window.store}>
        <App centered={true}>
          <Box full={true}>
            <SampleComponent></SampleComponent>
          </Box>
        </App>
      </StoreProvider>
    )
  }
}

export default MainComponent